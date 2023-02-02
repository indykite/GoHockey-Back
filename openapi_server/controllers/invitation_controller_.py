import uuid

import connexion
from indykite_sdk.indykite.identity.v1beta2 import identity_management_api_pb2 as pb2
from indykite_sdk.indykite.objects.v1beta1 import struct_pb2 as objects
from retrying import retry, RetryError

import openapi_server.controllers.security_controller_ as sec
from openapi_server.helper import format_helper, response_processor, patch_calls as patch
from openapi_server.models import InvitationCreateBody
from openapi_server.models import InvitationAcceptRequest
from openapi_server.helper.invitation_calls import check_invitation_state
from openapi_server.graphql_queries.get_address import get_address_query
from openapi_server.graphql_queries.get_children import get_children_query
from openapi_server.graphql_queries.accept_invitation import accept_invitation_mutation

from flask import g, jsonify, abort


def retry_if_reference_id_is_none(response):
    return response.get("reference_id") is None


def invitation_create(token_info):
    if connexion.request.is_json:
        invitation_create_body = InvitationCreateBody.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        resp = invitation_create_main(token_info['indykite_token'], invitation_create_body.invitee)
    except RetryError:
        return abort(404, description="Failed to send out the invitation")
    if not resp or resp["reference_id"] is None:
        return abort(422, description="Failed to create the invitation")
    else:
        patch.add_invitation_to_inviter_digital_twin_properties(token_info['indykite_token'], resp["reference_id"])
        return jsonify({"reference_id": resp["reference_id"]}), 201


@retry(stop_max_attempt_number=3, wait_fixed=1000, retry_on_result=retry_if_reference_id_is_none)
def invitation_create_main(token, invitee_email):
    reference_id = uuid.uuid4()
    try:
        introspect_response = sec.introspect_token(token)
    except Exception as e:
        return {"failure": e, "reference_id": None}

    try:
        g.indykite_client.stub.CreateInvitation(
            pb2.CreateInvitationRequest(
                tenant_id=introspect_response['tokenInfo']['subject']['tenantId'],
                message_attributes=objects.MapValue(
                    fields={
                        "inviter_id": objects.Value(string_value=introspect_response['tokenInfo']['subject']['id'])
                    }
                ),
                email=invitee_email,
                reference_id=str(reference_id)
            )
        )
    except Exception as e:
        return {"failure": e, "reference_id": None}

    return {"failure": None, "reference_id": reference_id}


def invitation_get(invitation_id):
    try:
        response = g.indykite_client.stub.CheckInvitationState(
            pb2.CheckInvitationStateRequest(
                reference_id=invitation_id
            )
        )
    except Exception:
        return None

    return format_helper.decode_response(response), 200


def invitations_get(token_info):
    invitation_information = []
    info = g.indykite_client.get_digital_twin_by_token(token_info['indykite_token'], ["nnin"])
    if not info:
      return abort(422, description="Failed to get nnin from user")
    else:
        try:
            ids = response_processor.get_all_reference_id_from_get_digital_twin_response(info)
        except Exception:
            pass

        for i in ids:
            try:
                r = invitation_get(i)
                invitation_information.append(r[0])
            except Exception:
                pass

    return jsonify(invitation_information)


def invitation_accept(token_info):
    if connexion.request.is_json:
        invitation_accept_body = InvitationAcceptRequest.from_dict(connexion.request.get_json())  # noqa: E501

    accepted = check_invitation_state(invitation_accept_body.token)
    if not accepted:
        return abort(422, "Failed to check the state of the invitation")

    digital_twin = g.indykite_client.get_digital_twin_by_token(token_info['indykite_token'], [])
    if digital_twin is None:
        return abort(404, description="Resource not found")

    response = format_helper.decode_response(accepted)

    # invitation_reference_id = response.get("invitation").get("referenceId")   # maybe we need this later
    inviter_id = response.get("invitation").get("messageAttributes").get("fields").get("inviter_id").get("stringValue")
    invitation_state = response.get("invitation").get("state")

    if invitation_state != "INVITATION_STATE_ACCEPTED":
        return abort(422, description="Invitation is in wrong state")

    address = get_address_from_inviter(inviter_id)
    if not address:
        return abort(422, description="KB error, failed to get the address of the inviter")

    children_ids = get_all_children(inviter_id)

    added_connection = []
    for child_id in children_ids:
        create_connection_body = {
              "where": {
                "externalId": str(digital_twin['digitalTwin'].id)
              },
              "connect": {
                "parent_of": [
                  {
                    "where": {
                      "node": {
                        "externalId": child_id
                      }
                    }
                  }
                ],
                "address": {
                    "where": {
                        "node": {
                            "externalId": address["addresses"][0]["externalId"]
                        }
                    }
                }
              }
            }
        response = g.indykite_graph_client.execute(accept_invitation_mutation, create_connection_body)
        added_connection.append(response)

    return True, 201


def get_address_from_inviter(inviter_id):
    get_address_params = {
        "where": {
            "receivers_SOME": {
                "externalId": inviter_id
            }
        }
    }
    response = g.indykite_graph_client.execute(get_address_query, get_address_params)
    if not response:
        return None
    return response


def get_all_children(inviter_id):
    get_children_params = {
        "where": {
            "parents_SOME": {
                "externalId": inviter_id
            },
        }
    }
    children = g.indykite_graph_client.execute(get_children_query, get_children_params)
    children_ids = []
    for i in children.get("children"):
        children_ids.append(i.get("externalId"))
    return children_ids

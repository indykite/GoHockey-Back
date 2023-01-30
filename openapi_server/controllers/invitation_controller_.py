import connexion
import uuid
from retrying import retry, RetryError

from indykite_sdk.indykite.identity.v1beta2 import identity_management_api_pb2 as pb2
from indykite_sdk.indykite.objects.v1beta1 import struct_pb2 as objects

import openapi_server.controllers.security_controller_ as sec
from openapi_server.helper import format_helper, response_processor, patch_calls as patch
from openapi_server.models import InvitationCreateBody

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
        except Exception as e:
            pass

        for i in ids:
            try:
                r = invitation_get(i)
                invitation_information.append(r[0])
            except Exception as e:
                pass

    return jsonify(invitation_information), 200

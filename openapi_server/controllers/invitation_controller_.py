import uuid
from retrying import retry

from indykite_sdk.indykite.identity.v1beta2 import identity_management_api_pb2 as pb2
from indykite_sdk.indykite.objects.v1beta1 import struct_pb2 as objects

import openapi_server.controllers.get_controller_ as get_info
import openapi_server.controllers.security_controller_ as sec
from openapi_server.helper import format_helper, response_processor

from flask import g


def retry_if_reference_id_is_none(response):
    return response.get("reference_id") is None


@retry(stop_max_attempt_number=3, wait_fixed=1000, retry_on_result=retry_if_reference_id_is_none)
def create_invitation(token, invitee_email):
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
        print("Exception: %s" % e)
        return {"failure": e, "reference_id": None}

    return {"failure": None, "reference_id": reference_id}


def get_one_invitation(invitation_id):
    try:
        response = g.indykite_client.stub.CheckInvitationState(
            pb2.CheckInvitationStateRequest(
                reference_id=invitation_id
            )
        )
    except Exception as e:
        print(e)
        return None

    return format_helper.decode_response(response)


def get_all_invitations(token):
    invitation_information = []
    info = get_info.get_digital_twin_info_by_token(token, ["nnin"])
    if info is not None:
        ids = response_processor.get_all_reference_id_from_get_digital_twin_response(format_helper.decode_response(info))

        for i in ids:
            r = get_one_invitation(i)
            if r is not None:
                invitation_information.append(r)
    return invitation_information

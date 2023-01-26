import uuid
from retrying import retry

from indykite_sdk.indykite.identity.v1beta2 import identity_management_api_pb2 as pb2
from indykite_sdk.indykite.objects.v1beta1 import struct_pb2 as objects

import openapi_server.controllers.get_controller_ as get_info
import openapi_server.controllers.security_controller_ as sec
import openapi_server.controllers.patch_controller_ as patch
import openapi_server.helper.format_helper as helper

from flask import g


def retry_if_reference_id_is_none(response):
    print("Retry function: %s" % response)
    return response.get("reference_id") is None


@retry(stop_max_attempt_number=3, wait_fixed=1000, retry_on_result=retry_if_reference_id_is_none)
def create_invitation(token, invitee_email):
    reference_id = uuid.uuid4()
    try:
        intospect_response = sec.introspect_token(token)
    except Exception as e:
        return {"failure": e, "reference_id": None}

    try:
        g.indykite_client.stub.CreateInvitation(
            pb2.CreateInvitationRequest(
                tenant_id=intospect_response['tokenInfo']['subject']['tenantId'],
                message_attributes=objects.MapValue(
                    fields={
                        "inviter_id": objects.Value(string_value=intospect_response['tokenInfo']['subject']['id'])
                    }
                ),
                email=invitee_email,
                reference_id=str(reference_id)
            )
        )
    except Exception as e:
        print("Exception: %s" % e)
        return {"failure": e, "reference_id": None}

    patch.add_invitation_to_inviter_digital_twin_properties(token, reference_id)
    r = get_info.get_digital_twin_info_by_token(token, ["extid", "email", "mobile", "nickname", "givenname", "name", "nnin"])
    print("DT info:\n%s" % r)

    return {"failure": None, "reference_id": reference_id}


def get_one_invitation(token, invitation_id):
    print(invitation_id)

    try:
        response = g.indykite_client.stub.CheckInvitationState(
            pb2.CheckInvitationStateRequest(
                reference_id=invitation_id
            )
        )
    except Exception as e:
        print(e)
        return None

    return helper.decode_response(response)

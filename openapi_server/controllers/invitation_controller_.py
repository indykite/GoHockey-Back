from indykite_sdk.indykite.identity.v1beta2 import identity_management_api_pb2 as pb2
from indykite_sdk.indykite.objects.v1beta1 import struct_pb2 as objects

import openapi_server.controllers.security_controller_ as sec
import openapi_server.helper.format_helper as helper

from flask import g


def create_invitation(token, invitee_email, reference_id):
    try:
        intospect_response = sec.introspect_token(g.client, token)
    except Exception as e:
        return e

    try:
        response = g.client.stub.CreateInvitation(
            pb2.CreateInvitationRequest(
                tenant_id=intospect_response['tokenInfo']['subject']['tenantId'],
                message_attributes=objects.MapValue(
                    fields={
                        "inviter_id": objects.Value(string_value=intospect_response['tokenInfo']['subject']['id'])
                    }
                ),
                email=invitee_email,
                reference_id=reference_id
            )
        )
    except Exception as e:
        print("Exception: %s" % e)
        return e
    return None


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

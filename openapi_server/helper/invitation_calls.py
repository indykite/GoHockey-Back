from flask import g
from indykite_sdk.indykite.identity.v1beta2 import identity_management_api_pb2 as pb2


def check_invitation_state(token):
    try:
        response = g.indykite_client.stub.CheckInvitationState(
            pb2.CheckInvitationStateRequest(
                invitation_token=token
            )
        )
    except Exception as e:
        print("Invitation state check failed" % e)
        return None
    return response

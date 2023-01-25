import openapi_server.controllers.security_controller_ as sec
import openapi_server.helper.format_helper as helper

from indykite_sdk.indykite.identity.v1beta2 import identity_management_api_pb2 as pb2
from indykite_sdk.indykite.objects.v1beta1 import struct_pb2 as objects


def create_invitation(token, invitee_email, reference_id):
  client = sec.create_identity_client_connection()
  try:
    intospect_response = sec.introspect_token(client, token)
  except Exception as e:
    return e

  try:
    response = client.stub.CreateInvitation(
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
    print("Response of the create invitation:\n%s" % response)
  except Exception as e:
    print("Exception: %s" % e)
    return e

  sec.close_identity_client_connection(client)
  return None


def get_one_invitation(token, invitation_id):
  client = sec.create_identity_client_connection()
  print(invitation_id)

  try:
    response = client.stub.CheckInvitationState(
      pb2.CheckInvitationStateRequest(
        reference_id=invitation_id
      )
    )
    print("Response of the get invitation:\n%s" % response)
  except Exception as e:
    print(e)
    return None

  sec.close_identity_client_connection(client)
  return helper.decode_response(response)

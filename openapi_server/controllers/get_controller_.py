import uuid
from retrying import retry

from indykite_sdk.indykite.identity.v1beta2 import identity_management_api_pb2 as pb2
from indykite_sdk.indykite.identity.v1beta2 import attributes_pb2 as attribute

from flask import g


def get_digital_twin_info_by_token(token, fields):
  props = []
  for f in fields:
    props.append(attribute.PropertyMask(definition=attribute.PropertyDefinition(property=f)))

  try:
    response = g.indykite_client.stub.GetDigitalTwin(
      pb2.GetDigitalTwinRequest(
        id=pb2.DigitalTwinIdentifier(access_token=token),
        properties=props
      )
    )
  except Exception as e:
    print("Exception: %s" % e)
    return e

  return response

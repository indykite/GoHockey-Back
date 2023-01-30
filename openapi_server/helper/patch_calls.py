from flask import g
from indykite_sdk.indykite.identity.v1beta2 import attributes_pb2 as attribute
from indykite_sdk.indykite.identity.v1beta2 import identity_management_api_pb2 as pb2
from indykite_sdk.indykite.objects.v1beta1 import struct_pb2 as objects


def add_invitation_to_inviter_digital_twin_properties(token, reference_id):
    try:
        response = g.indykite_client.stub.PatchDigitalTwin(
            pb2.PatchDigitalTwinRequest(
                id=pb2.DigitalTwinIdentifier(
                    access_token=token
                ),
                operations=[
                    attribute.PropertyBatchOperation(
                        add=attribute.Property(
                            definition=attribute.PropertyDefinition(property="nnin"),
                            object_value=objects.Value(string_value=str(reference_id)))
                    )
                ]
            )
        )
        print("Response for patch: %s" % response)
    except Exception as e:
        print("Patch failed with: %s" % e)
        return e
    return None

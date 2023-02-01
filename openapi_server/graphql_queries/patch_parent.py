from gql import gql

"""
Finding 
{
  "lookUpByInput": {
    "tenantId": "gid:AAAAAsbScdySjUxliRGSvMxyMiU",
    "type": "email",
    "value": "simon.thordal@indykite.com"
  },
  "propertyPatchInputs": [
    {
      "assuranceLevel": "LOW",
      "issuer": "app:3mHBgoGNS0-lW9sfO6M3_Q",
      "operation": "ADD",
      "property": "extid",
      "value": "gid:123123kadlaksd131"
    }
  ]
}
"""
patch_parent_mutation = gql(
    """
    mutation PatchDigitalTwin($lookUpByInput: LookUpByInput!, $propertyPatchInputs: [IdentityPropertyPatchInput!]!) {
    patchDigitalTwin(lookUpByInput: $lookUpByInput, propertyPatchInputs: $propertyPatchInputs) {
        index
        id
        error {
        message
        }
    }
    }
    """
)

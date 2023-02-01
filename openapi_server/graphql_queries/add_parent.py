from gql import gql

"""
{
  "input": {
    "externalId": "gid:23asda1a23fa294",
    "tenantId": "c6d271dc-928d-4c65-8911-92bccc723225",
    "givenname": "simon",
    "lastname": "thordal",
    "kind": "PERSON",
    "tags": ["Parent"],
  }
}
"""

add_parent_mutation = gql(
    """mutation CreateParents($input: [ParentCreateInput!]!) {
      createParents(input: $input) {
        parents {
          externalId
          givenname
          kind
          lastname
          digitalTwinId
          tenantId
          tags
        }
      }
    }"""
)

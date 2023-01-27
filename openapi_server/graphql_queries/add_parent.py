from gql import gql
"""
{
  "input": {
    "externalId": "simonthordal@gmail.com",
    "tenantId": "c6d271dc-928d-4c65-8911-92bccc723225",
    "email": "simonthordal",
    "givenname": "simon",
    "lastname": "thordal",
    "kind": "PERSON",
    "digitalTwinId": "1234567890",
    "tags": ["Parent"],
  }
}
"""

add_parent_mutation = gql(
  """mutation CreateParents($input: [ParentCreateInput!]!) {
    createParents(input: $input) {
      parents {
        email
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

from gql import gql
"""
Given a parent and sufficient 
{
  "input": {
    "cloth_size": 10,
    "helmet_size": 10,
    "gender": "M",
    "externalId": "123213212", // I think we'll need to generate this, maybe a UUID
    "given_name": "Sprinkles",
    "shoe_size": 10,
    "birthdate": "2020/12/12",
    "registered_by": {
      "connect": {
        "where": {
          "node": {"digitalTwinId": "1234567890"}
        }
      }
    }
    "parents": {
      "connect": {
        "where": {
          "node": {"digitalTwinId": "1234567890"}
        }
      }
    }
  }
}
"""

add_child_mutation = gql(
  """mutation CreateChildren($input: [ChildCreateInput!]!) {
    createChildren(input: $input) {
      children {
        birthdate
        cloth_size
        externalId
        gender
        given_name
        helmet_size
        shoe_size
        externalId
        registered_by {
          digitalTwinId
        }
        parents {
          digitalTwinId
        }
      }
    }
  }"""
)
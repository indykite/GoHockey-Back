from gql import gql

"""
Given a parent and sufficient 
{
  "input": {
    "cloth_size": 10,
    "helmet_size": 10,
    "gender": "M",
    "externalId": "d3f20f9e-15d6-403a-b218-a0d9883bde23"
    "given_name": "Sprinkles",
    "shoe_size": 10,
    "year_of_birth": 2020,
    "registered_by": {
      "connect": {
        "where": {
          "node": {"externalId": "gid:23asda1a23fa294"}
        }
      }
    }
    "parents": {
      "connect": {
        "where": {
          "node": {"externalId": "gid:23asda1a23fa294"}
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
          year_of_birth
          cloth_size
          gender
          given_name
          helmet_size
          shoe_size
          externalId
          registered_by {
            externalId
          }
          parents {
            externalId
          }
        }
      }
    }"""
)

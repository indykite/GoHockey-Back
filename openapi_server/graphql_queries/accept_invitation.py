from gql import gql

"""
{
  "where": {
    "externalId": parent_id
  },
  "connect": {
    "parent_of": [
      {
        "where": {
          "node": {
            "externalId": child_id
          }
        }
      }
    ],
    "address": {
      "where": {
        "node": {
          "externalId": address_id
        }
      }
    }
  }
}
"""


accept_invitation_mutation = gql(
  """mutation UpdateParents($where: ParentWhere, $connect: ParentConnectInput) {
      updateParents(where: $where, connect: $connect) {
        parents {
          externalId
        }
      }
    }"""
)

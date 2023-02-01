from gql import gql

"""
{
  "connect": {
    "parent_of": [
      {
        "where": {
          "node": {
            "externalId": null
          }
        }
      }
    ]
  },
  "where": {
    "externalId": null
  }
}
"""


accept_invitation_mutation = gql(
  """mutation UpdateParents($where: ParentWhere, $connect: ParentConnectInput) {
        updateParents(where: $where, connect: $connect) {
            parents {
                parent_of {
                    externalId
                }
            }
        }
    }"""
)

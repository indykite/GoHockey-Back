from gql import gql

"""
{
  "where": {
    "externalId": parent_id
  },
  "connect": {
    "parent_of": [
      {
        "connect": null,
        "where": {
          "node": {
            "externalId": child_id
          }
        }
      }
    ]
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

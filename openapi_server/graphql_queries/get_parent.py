from gql import gql

"""
Finding parent only based on its own id
{
  "where": {
    "externalId": "gid:AAAAFWqRpJo0E0iji-w7f57gDYU"
  }
}
"""

get_parent_query = gql(
    """
    query Parents($where: ParentWhere) {
      parents(where: $where) {
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
    """
)

"""
Finding parent based on address
{
  "where": {
    "address": {
      "receivers_SOME": {
        "externalId": "gid:AAAAFWqRpJo0E0iji-w7f57gDYU"
      }
    }
  }
}
"""

get_parent_from_address_query = gql(
    """
    query Parents($where: ParentWhere) {
      parents(where: $where) {
        givenname
        lastname
      }
    }
    """
)

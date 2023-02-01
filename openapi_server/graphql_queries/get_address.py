from gql import gql

"""
{
  "where": {
    "receivers_SOME": {
      "externalId": "gid:AAAAFWqRpJo0E0iji-w7f57gDYU"
    }
  }
}
"""

get_address_query = gql(
    """
    query Addresses($where: AddressWhere) {
      addresses(where: $where) {
        city
        country
        externalId
        state
        street
        zip
      }
    }
    """
)

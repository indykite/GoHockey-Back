from gql import gql
"""
{
  "where": {
    "externalId":"1453851837"
  }
}
"""
get_address_query= gql(
  """query Address($where: AddressWhere) {
    addresses(where: $where) {
      zip
      city
      street
      state
      country
      externalId
    }
  }"""
)
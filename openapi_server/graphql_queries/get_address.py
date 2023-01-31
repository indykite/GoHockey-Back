from gql import gql

"""
{
  "where": {
    "externalId":"c42c7722-45b2-4787-8fba-69627b088980"
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

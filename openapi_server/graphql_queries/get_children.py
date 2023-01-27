from gql import gql
"""
Given a parents digitalTwinId, get all their children
{
  "where": {
    "parents_SOME": {
      "digitalTwinId": "1234567890"
    }
  }
}
"""
get_children_query = gql(
  """query Children($where: ChildWhere) {
    children(where: $where) {
      cloth_size
      helmet_size
      shoe_size
      birthdate
      given_name
      gender
      externalId
      parents {
        email
        givenname
        lastname
        externalId
      }
    }
  }"""
)
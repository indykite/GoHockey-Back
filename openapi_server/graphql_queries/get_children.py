from gql import gql
"""
Given a parents digitalTwinId, get all their children
{
  "where": {
    "parents_SOME": {
      "externalId": "gid:AAAdas23f456a78x90"
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
      year_of_birth
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
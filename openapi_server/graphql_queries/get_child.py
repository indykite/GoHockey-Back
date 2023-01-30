from gql import gql

"""
Given a parents digitalTwinId and a childs externalId, get
the childs attributes
{
  "where": {
    "parents_SOME": {
      "digitalTwinId": "1234567890"
    },
    "externalId": "123213212"
  }
}
"""

get_child_query = gql(
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
        digitalTwinId
      }
    }
  }"""
)

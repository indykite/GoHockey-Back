from gql import gql

"""
Given a parents digitalTwinId and a childs externalId, get
the childs attributes
{
  "where": {
    "parents_SOME": {
      "externalId": "gid:AAAdas23f456a78x90"
    },
    "externalId": "c42c7722-45b2-4787-8fba-69627b088980"
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

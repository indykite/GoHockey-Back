from gql import gql

"""
Update child by externalId
{
  "where": {
    "externalId": "gid:23asda1a23fa294"
  },
  "update": {
    "cloth_size": 154,
    "helmet_size": 38,
    "shoe_size": 44
  }
}
"""

patch_child_mutation = gql(
    """
    mutation UpdateChildren($where: ChildWhere, $update: ChildUpdateInput) {
      updateChildren(where: $where, update: $update) {
        children {
          helmet_size
          shoe_size
          cloth_size
        }
      }
    }
    """
)

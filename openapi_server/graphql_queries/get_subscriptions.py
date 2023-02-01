from gql import gql

"""
Finding subscriptions based on childs externalId
{
  "where": {
    "child": {
      "parents_SOME": {
        "externalId": null
      }
    }
  }
}
"""

get_subscriptions_query = gql(
    """
    query HockeySubscriptions($where: HockeySubscriptionWhere) {
      hockeySubscriptions(where: $where) {
        valid_to
        valid_from
        sku
        child {
          given_name
          externalId
        }
        externalId
        parent {
          givenname
          lastname
          externalId
        }
      }
    }
    """
)

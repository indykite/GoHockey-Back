from gql import gql
"""
Finding subscriptions based on childs externalId
{
  "where": {
    "child": {
      "externalId": "123213212"
    }
  }
}
"""
get_subscriptions_query = gql(
  """query HockeySubscription($where: HockeySubscriptionWhere) {
    hockeySubscriptions(where: $where) {
      valid_from
      valid_to
      externalId
    }
  }"""
)
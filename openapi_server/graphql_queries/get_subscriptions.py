from gql import gql

"""
Finding subscriptions based on childs externalId
{
  "where": {
    "child": {
      "externalId": "c42c7722-45b2-4787-8fba-69627b088980"
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

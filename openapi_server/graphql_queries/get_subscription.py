from gql import gql

"""
Finding subscription only based on its own id
{
  "where": {
    "externalId": "c42c7722-45b2-4787-8fba-69627b088980"
  }
}

"""
get_subscription_query = gql(
    """query HockeySubscription($where: HockeySubscriptionWhere) {
      hockeySubscriptions(where: $where) {
        valid_from
        valid_to
        externalId
      }
    }"""
)

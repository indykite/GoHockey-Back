from gql import gql

"""
Finding subscription only based on its own id
{
  "where": {
    "externalId": "hfgqwdiugwef"
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

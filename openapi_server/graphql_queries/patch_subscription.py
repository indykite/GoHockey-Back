from gql import gql

patch_subscription_mutation = gql(
    """
    mutation UpdateHockeySubscriptions($where: HockeySubscriptionWhere, $update: HockeySubscriptionUpdateInput) {
        updateHockeySubscriptions(where: $where, update: $update) {
            hockeySubscriptions {
                valid_from
                valid_to
                externalId
            }
        }
    }
    """
)

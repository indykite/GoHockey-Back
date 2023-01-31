from gql import gql

"""
{
  "input": {
    "valid_from": "01.01.2023",
    "valid_to": "01.09.2023",
    "externalId": "ccb990a7-c22e-4dc0-ad89-a9a8c3c0b82e",
    "sku": ["SKU001"],
    "child": {
      "connect": {
        "where": { 
          "node": { "externalId": "c42c7722-45b2-4787-8fba-69627b088980"}
        }
      }
    },
     "parent": {
      "connect": {
        "where": { 
          "node": { "externalId": "ccb990a7-c22e-4dc0-ad89-a9a8c3c0b82e"}
        }
      }
    }
  }
}

"""
add_subscription_mutation = gql(
    """mutation CreateHockeySubscription($input: [HockeySubscriptionCreateInput!]!) {
      createHockeySubscriptions(input: $input) {
          hockeySubscriptions{
            valid_from
            valid_to
            externalId
            sku
            child {
              externalId
            }
            parent {
              externalId
            }
          }
        }
      }"""
)

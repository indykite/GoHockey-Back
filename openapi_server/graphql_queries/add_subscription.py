from gql import gql
"""
{
  "input": {
    "valid_from": "01.01.2023",
    "valid_to": "01.09.2023",
    "externalId": "hfgqwdiugwef",
    "child": {
      "connect": {
        "where": { 
          "node": { "externalId": "123213212"}
        }
      }
    },
     "delivers_to": {
      "connect": {
        "where": { 
          "node": { "externalId": "fdghrshshs"}
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
          child {
            externalId
          }
          delivers_to {
            externalId
          }
        }
      }
    }"""
)
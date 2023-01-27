from gql import gql
"""
{
  "input": {
    "zip": "12345",
    "number": 123,
    "city": "Anytown",
    "street": "Main St",
    "state": "CA",
    "externalId": "1453851837",
    "subscriptions":{
      "connect": {
        "where": { 
          "node": {"externalId":"hfgqwdiugwef"}
        }
      }
    },
    "receivers":{
      "connect": {
        "where": { 
          "node": {"digitalTwinId":"1234567890"}
        }
      }
    }
  }
}

"""
add_address_mutation = gql(
  """mutation CreateAddress($input: [AddressCreateInput!]!){
      createAddresses(input: $input){
          addresses{
              zip
              number
              city
              street
              state
              externalId
              subscriptions{
                  externalId
              }
              receivers{
                  digitalTwinId
              }
          }
      }
  }"""
)
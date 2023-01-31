from gql import gql

"""
{
  "input": {
    "zip": "12345",
    "number": 123,
    "city": "Anytown",
    "street": "Main St",
    "country": "USA",
    "externalId": "1453851837",
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
                country
                externalId
                receivers{
                    digitalTwinId
                }
            }
        }
    }"""
)

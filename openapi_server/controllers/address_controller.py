import uuid

import connexion
from flask import abort, g, jsonify

from openapi_server.graphql_queries.add_address import add_address_mutation
from openapi_server.graphql_queries.get_address import get_address_query
from openapi_server.models.user_address_body import UserAddressBody  # noqa: E501


def user_address_get(address_id):
    """Get the logged in user's address

     # noqa: E501
    """
    get_address_params = {
        "where": {
            "externalId": address_id
        }
    }

    address = g.indykite_graph_client.execute(get_address_query, get_address_params)
    if not address:
        return abort(422, description="KB error, failed to get the address")
    return jsonify(address), 200


def user_address_post(token_info, user_address_body=None):  # noqa: E501
    """Add a child to the logged in user

     # noqa: E501

    :rtype: None
    """
    address_id = uuid.uuid4()
    digital_twin = g.indykite_client.get_digital_twin_by_token(token_info['indykite_token'], [])
    if digital_twin is None:
        return abort(404, description="Resource not found")

    if connexion.request.is_json:
        user_address_body = UserAddressBody.from_dict(connexion.request.get_json())  # noqa: E501
    post_address_params = {
        "input": {
            "zip": user_address_body.zip,
            "city": user_address_body.city,
            "street": user_address_body.address,
            "country": user_address_body.country,
            "externalId": str(address_id),
            "receivers": {
                "connect": {
                    "where": {
                        "node": {"digitalTwinId": digital_twin['digitalTwin'].id}
                    }
                }
            }
        }
    }
    print(post_address_params)
    address = g.indykite_graph_client.execute(add_address_mutation, post_address_params)
    print(address)
    if not address:
        return abort(422, description="KB error, failed to create the address")
    return jsonify(address), 201

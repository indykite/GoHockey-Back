import connexion
from flask import g, abort

from openapi_server.graphql_queries.patch_subscription import patch_subscription_mutation
from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.models.user_subscription_body import UserSubscriptionBody  # noqa: E501


def user_subscriptions_get():  # noqa: E501
    """Get the subscriptions of the logged in user

     # noqa: E501
    """
    return [
        {
            "from": "2022-01-01T00:00:00Z",
            "to": "2022-12-31T23:59:59Z",
            "sku": [
                "SKU22005",
                "SKU22005"
            ],
            "child": "123e4567-e89b-12d3-a456-426655440000"
        },
        {
            "from": "2022-02-02T00:00:00Z",
            "to": "2022-11-30T23:59:59Z",
            "sku": [
                "SKU22006",
                "SKU22006"
            ],
            "child": "123e4567-e89b-12d3-a456-426655440000"
        }
    ]


def user_subscription_get():  # noqa: E501
    """Get the subscription of the logged in user

     # noqa: E501


    :rtype: InlineResponse2001
    """
    return {
        "from": "2022-01-01T00:00:00Z",
        "to": "2022-12-31T23:59:59Z",
        "sku": [
            "SKU22005",
            "SKU22005"
        ],
        "child": "123e4567-e89b-12d3-a456-426655440000"
    }


def user_subscription_post(user_subscription_body=None):  # noqa: E501
    """Add a subscription to the logged in user

     # noqa: E501

    :param user_subscription_body:
    :type user_subscription_body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        user_subscription_body = UserSubscriptionBody.from_dict(connexion.request.get_json())  # noqa: E501
    return {
        "from": "2022-01-01T00:00:00Z",
        "to": "2022-12-31T23:59:59Z",
        "sku": [
            "SKU22005"
        ],
        "child": "123e4567-e89b-12d3-a456-426655440000"
    }


def user_subscription_patch(token_info, subscription_id):  # noqa: E501
    """Update the subscription of the logged in user

     # noqa: E501

    :param token_info:
    :param subscription_id: Id of the subscription to update
    :type subscription_id: str

    :rtype: None
    """
    digital_twin = g.indykite_client.get_digital_twin_by_token(token_info['indykite_token'], [])
    if digital_twin is None:
        return abort(404, description="Resource not found")
    if connexion.request.is_json:
        data = UserSubscriptionBody.from_dict(connexion.request.get_json())
    patch_subscription_params = {
        "where": {
            "externalId": subscription_id
        },
        "update": {
            "valid_to": data.to
        }
    }
    child = g.indykite_graph_client.execute(patch_subscription_mutation, patch_subscription_params)
    return child

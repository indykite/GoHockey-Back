import connexion

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

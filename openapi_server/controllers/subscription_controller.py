import connexion

from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.models.user_subscription_body import UserSubscriptionBody  # noqa: E501
from openapi_server.graphql_queries.get_subscription import get_subscription_query
from flask import abort, g


def user_subscriptions_get(child_id):  # noqa: E501
    """Get the subscriptions of the logged in user

     # noqa: E501
    """
    get_subscription_param = {
          "where": {
            "child": {
              "externalId": child_id
            }
          }
        }
    subscription = g.indykite_graph_client.execute(get_subscription_query, get_subscription_param)
    return subscription


def user_subscription_get(subscription_id):  # noqa: E501
    """Get the subscription of the logged in user

     # noqa: E501


    :rtype: InlineResponse2001
    """
    get_subscription_param = {
          "where": {
            "externalId": subscription_id
          }
        }
    subscription = g.indykite_graph_client.execute(get_subscription_query, get_subscription_param)
    return subscription


def user_subscription_post(user_subscription_body=None):  # noqa: E501
    """Add a subscription to the logged in user

     # noqa: E501

    :param user_subscription_body:
    :type user_subscription_body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        user_subscription_body = UserSubscriptionBody.from_dict(connexion.request.get_json())  # noqa: E501
    subscription = g.indykite_graph_client.execute(get_subscription_query, user_subscription_body)
    return subscription

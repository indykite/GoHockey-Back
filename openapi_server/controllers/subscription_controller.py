import connexion
import datetime
import uuid

from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.models.user_subscription_body import UserSubscriptionBody  # noqa: E501
from openapi_server.graphql_queries.get_subscription import get_subscription_query
from openapi_server.graphql_queries.add_subscription import add_subscription_mutation
from openapi_server.controllers.address_controller import user_address_get
from flask import abort, g, jsonify


def user_subscriptions_get(child_id):  # noqa: E501
    """Get the subscriptions of the logged in user

     # noqa: E501
    """
    get_subscription_param = {
          "where": {
            "child": {
              "externalId": str(child_id)
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
            "externalId": str(subscription_id)
          }
        }
    subscription = g.indykite_graph_client.execute(get_subscription_query, get_subscription_param)
    return subscription


def user_subscription_post(token_info, user_subscription_body=None):  # noqa: E501
    """Add a subscription to the logged in user

     # noqa: E501

    :rtype: None
    """
    subscription_id = uuid.uuid4()
    digital_twin = g.indykite_client.get_digital_twin_by_token(token_info['indykite_token'], [])
    if digital_twin is None:
      return abort(404, description="Resource not found")

    if connexion.request.is_json:
        user_subscription_body = UserSubscriptionBody.from_dict(connexion.request.get_json())  # noqa: E501

    valid_from = user_subscription_body.valid_from
    if valid_from is None:
      valid_from = datetime.datetime.now()

    post_subscription_param = {
      "input": {
        "valid_from": str(valid_from),
        "valid_to": user_subscription_body.valid_to,
        "externalId": str(subscription_id),
        "sku": user_subscription_body.sku,
        "child": {
          "connect": {
            "where": {
              "node": {"externalId": str(user_subscription_body.child)}
            }
          }
        },
        "parent": {
          "connect": {
            "where": {
              "node": {"externalId": str(digital_twin['digitalTwin'].id)}
            }
          }
        }
      }
    }
    subscription = g.indykite_graph_client.execute(add_subscription_mutation, post_subscription_param)
    return jsonify(subscription)

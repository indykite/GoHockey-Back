import connexion
import datetime
import uuid

from openapi_server.graphql_queries.patch_subscription import patch_subscription_mutation
from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.models.user_subscription_body import UserSubscriptionBody  # noqa: E501
from openapi_server.graphql_queries.get_subscription import get_subscription_query
from openapi_server.graphql_queries.add_subscription import add_subscription_mutation
from openapi_server.controllers.child_controller import get_children_query
from flask import abort, g, jsonify


def user_subscriptions_get(token_info):  # noqa: E501
    """Get the subscriptions of the logged in user

     # noqa: E501

    :rtype: None
    """
    children = []
    digital_twin = g.indykite_client.get_digital_twin_by_token(token_info['indykite_token'], [])
    if digital_twin is None:
      return abort(404, description="Resource not found")
    get_children_params = {
      "where": {
        "parents_SOME": {
          "externalId": digital_twin['digitalTwin'].id
        },
      }
    }
    get_children = g.indykite_graph_client.execute(get_children_query, get_children_params)
    if get_children:
      for child in get_children.get("children"):
        children.append(child.get("externalId"))

    subscriptions = []
    for child in children:
      get_subscription_param = {
            "where": {
              "child": {
                "externalId": child
              }
            }
          }
      subscriptions.append(g.indykite_graph_client.execute(get_subscription_query, get_subscription_param))
    return subscriptions


def user_child_subscriptions_get(child_id):
  get_subscription_param = {
    "where": {
      "child": {
        "externalId": child_id
      }
    }
  }
  subscriptions = g.indykite_graph_client.execute(get_subscription_query, get_subscription_param)
  return subscriptions


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
            "valid_to": str(data.valid_to)
        }
    }
    child = g.indykite_graph_client.execute(patch_subscription_mutation, patch_subscription_params)
    return child

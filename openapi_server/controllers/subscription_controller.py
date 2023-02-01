import datetime
from datetime import date
import uuid
from flask import g, abort
from indykite_sdk.authorization import AuthorizationClient

import connexion
from flask import g, abort, jsonify
from indykite_sdk.authorization import AuthorizationClient

from openapi_server.graphql_queries.add_subscription import add_subscription_mutation
from openapi_server.graphql_queries.get_subscription import get_subscription_query
from openapi_server.graphql_queries.get_subscriptions import get_subscriptions_query
from openapi_server.graphql_queries.patch_subscription import patch_subscription_mutation
from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.models.user_subscription_body import UserSubscriptionBody  # noqa: E501


def user_subscriptions_get(token_info):  # noqa: E501
    """Get the subscriptions of the logged in user

     # noqa: E501

    :rtype: None
    """
    digital_twin = g.indykite_client.get_digital_twin_by_token(token_info['indykite_token'], [])
    if digital_twin is None:
        return abort(404, description="Resource not found")
    get_subscriptions_param = {
        "where": {
            "child": {
                "parents_SOME": {
                    "externalId": digital_twin['digitalTwin'].id
                }
            }
        }
    }
    subscriptions = g.indykite_graph_client.execute(get_subscriptions_query, get_subscriptions_param)
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
            "externalId": subscription_id
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
            "valid_to": str(user_subscription_body.valid_to),
            "externalId": str(subscription_id),
            "sku": user_subscription_body.sku,
            "child": {
                "connect": {
                    "where": {
                        "node": {"externalId": user_subscription_body.child}
                    }
                }
            },
            "parent": {
                "connect": {
                    "where": {
                        "node": {"externalId": digital_twin['digitalTwin'].id}
                    }
                }
            }
        }
    }
    subscription = g.indykite_graph_client.execute(add_subscription_mutation, post_subscription_param)
    return jsonify(subscription)


class Resource:
    def __init__(self, label, element):
        self.label = label
        self.id = element


def user_subscription_patch(token_info, subscription_id):  # noqa: E501
    """Update the subscription of the logged in user

     # noqa: E501

    :param token_info:
    :param subscription_id: Id of the subscription to update
    :type subscription_id: str

    :rtype: None
    """
    ac = AuthorizationClient()
    resource = Resource("HockeySubscription", subscription_id)
    res = ac.is_authorized_token(
        token_info['indykite_token'],
        [resource],
        ["patch_subscription"]
    )
    allowed = res.decisions[subscription_id].allow_action["patch_subscription"]
    if not allowed:
        return abort(404, description="Not found")
    patch_subscription_params = {
        "where": {
            "externalId": subscription_id
        },
        "update": {
            "valid_to": str(date.today())
        }
    }
    subscription = g.indykite_graph_client.execute(patch_subscription_mutation, patch_subscription_params)
    return subscription

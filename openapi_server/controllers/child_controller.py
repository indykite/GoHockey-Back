from uuid import uuid4 as uuid

import connexion
from flask import abort, g

from openapi_server.graphql_queries.add_child import add_child_mutation
from openapi_server.graphql_queries.get_child import get_child_query
from openapi_server.graphql_queries.get_children import get_children_query
from openapi_server.graphql_queries.patch_child import patch_child_mutation
from openapi_server.models.user_child_body import UserChildBody  # noqa: E501
from openapi_server.models.user_child_patch_body import UserChildPatchBody  # noqa: E501


def user_children_get(token_info):
    """Get the children of the logged in user

     # noqa: E501
    """
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
    children = g.indykite_graph_client.execute(get_children_query, get_children_params)
    return children


def user_child_child_id_get(token_info, child_id):  # noqa: E501
    """Get the child by id

     # noqa: E501

    :param token_info:
    :param child_id: Id of the child to get
    :type child_id: str

    :rtype: UserChildBody
    """
    digital_twin = g.indykite_client.get_digital_twin_by_token(token_info['indykite_token'], [])
    if digital_twin is None:
        return abort(404, description="Resource not found")
    get_child_params = {
        "where": {
            "parents_SOME": {
                "externalId": digital_twin['digitalTwin'].id
            },
            "externalId": child_id
        }
    }
    child = g.indykite_graph_client.execute(get_child_query, get_child_params)
    return child


def user_child_child_id_patch(token_info, child_id):  # noqa: E501
    """Update the child by id

     # noqa: E501

    :param token_info:
    :param child_id: Id of the child to update
    :type child_id: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserChildPatchBody.from_dict(connexion.request.get_json())  # noqa: E501
    digital_twin = g.indykite_client.get_digital_twin_by_token(token_info['indykite_token'], [])
    if digital_twin is None:
        return abort(404, description="Resource not found")
    params = {
        "where": {
            "externalId": child_id
        },
        "update": {
            "cloth_size": int(body.cloth_size),
            "helmet_size": int(body.helmet_size),
            "shoe_size": int(body.shoe_size)
        }
    }
    child = g.indykite_graph_client.execute(patch_child_mutation, params)
    if not child['updateChildren']['children']:
        return abort(404, description="Resource Child not found")
    return child


def user_child_post(token_info):  # noqa: E501
    """Add a child to the logged in user

     # noqa: E501

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserChildBody.from_dict(connexion.request.get_json())  # noqa: E501
    digital_twin = g.indykite_client.get_digital_twin_by_token(token_info['indykite_token'], [])
    if digital_twin is None:
        return abort(404, description="Resource not found")
    params = {
        "externalId": str(uuid()),
        "registered_by": {
            "connect": {
                "where": {
                    "node": {"externalId": digital_twin['digitalTwin'].id}
                }
            }
        },
        "parents": {
            "connect": {
                "where": {
                    "node": {"externalId": digital_twin['digitalTwin'].id}
                }
            }
        },
        "helmet_size": int(body.helmet_size),
        "shoe_size": int(body.shoe_size),
        "cloth_size": int(body.cloth_size),
        "year_of_birth": int(body.year_of_birth),
        "gender": body.gender,
        "given_name": body.given_name
    }
    child = g.indykite_graph_client.execute(add_child_mutation, {"input": params})
    return child

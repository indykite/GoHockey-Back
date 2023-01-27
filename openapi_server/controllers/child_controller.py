import connexion
from openapi_server.models.user_child_body import UserChildBody  # noqa: E501
from openapi_server.graphql_queries.get_child import get_child_query
from flask import abort, g


def user_children_get(token_info):
    """Get the children of the logged in user

     # noqa: E501
    """
    return [
        {
            "shoe_size": 36,
            "gender": "male",
            "cloth_size": 122,
            "helmet_size": 52,
            "given_name": "John",
            "year_of_birth": 2010
        },
        {
            "shoe_size": 37,
            "gender": "female",
            "cloth_size": 122,
            "helmet_size": 52,
            "given_name": "Jane",
            "year_of_birth": 2009
        }
    ]


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
                "digitalTwinId": digital_twin['digitalTwin'].id
            },
            "externalId": child_id
        }
    }
    child = g.indykite_graph_client.execute(get_child_query, get_child_params)
    return child


def user_child_post(user_child_body=None):  # noqa: E501
    """Add a child to the logged in user

     # noqa: E501

    :param user_child_body:
    :type user_child_body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        user_child_body = UserChildBody.from_dict(connexion.request.get_json())  # noqa: E501
    return {
        "shoe_size": 36,
        "gender": "male",
        "cloth_size": 122,
        "helmet_size": 52,
        "given_name": "John",
        "year_of_birth": 2010
    }

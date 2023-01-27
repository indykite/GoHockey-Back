from flask import abort, g
import uuid
from openapi_server.graphql_queries.add_parent import add_parent_mutation


def user_post(token_info):  # noqa: E501
    """Add a user

     # noqa: E501


    :rtype: str
    """
    digital_twin = g.indykite_client.get_digital_twin_by_token(token_info['indykite_token'], ["email", "givenname", "familyname"])
    if digital_twin is None:
        return abort(404, description="Resource not found")
    add_parent_params = {
        "input": {
            "externalId": digital_twin['digitalTwin'].id,
            "tenantId": digital_twin['tokenInfo'].subject.tenantId,
            "email": digital_twin['digitalTwin'].properties[0].value,
            "givenname": digital_twin['digitalTwin'].properties[1].value,
            "lastname": digital_twin['digitalTwin'].properties[2].value,
            "kind": "PERSON",
            "tags": ["Parent"],
        }
    }
    parent = g.indykite_graph_client.execute(add_parent_mutation, add_parent_params)
    return parent


def user_get(token_info):  # noqa: E501
    """Get Information of the logged in user

     # noqa: E501


    :rtype: str
    """
    return {
        "name": "John Doe",
        "email": "john.doe@indykite.com"
    }


def user_email_get(token_info):  # noqa: E501
    """Get the email of the logged in user

     # noqa: E501


    :rtype: str
    """
    digital_twin = g.indykite_client.get_digital_twin_by_token(token_info['indykite_token'], ["email"])
    if digital_twin is None:
        return abort(404, description="Resource not found")
    return digital_twin['digitalTwin'].properties[0].value


def user_parents_get(token_info):  # noqa: E501
    """Get the parents of the logged in user

     # noqa: E501
    """
    return [
        {
            "name": "John Doe",
            "email": "john.doe@indykite.com"
        },
        {
            "name": "Jane Doe",
            "email": "jane.doe@indykite.com"
        }
    ]

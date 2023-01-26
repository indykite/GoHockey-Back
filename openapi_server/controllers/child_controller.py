import connexion
from flask import abort, jsonify, g
from indykite_sdk.identity import IdentityClient

import openapi_server.controllers.invitation_controller_ as invitation
from openapi_server.models import InvitationCreateBody
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.models.user_address_body import UserAddressBody  # noqa: E501
from openapi_server.models.user_child_body import UserChildBody  # noqa: E501
from openapi_server.models.user_subscription_body import UserSubscriptionBody  # noqa: E501


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


def user_child_child_id_get(child_id):  # noqa: E501
    """Get the child by id

     # noqa: E501

    :param child_id: Id of the child to get
    :type child_id: str

    :rtype: UserChildBody
    """
    return {
        "shoe_size": 36,
        "gender": "male",
        "cloth_size": 122,
        "helmet_size": 52,
        "given_name": "John",
        "year_of_birth": 2010
    }


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
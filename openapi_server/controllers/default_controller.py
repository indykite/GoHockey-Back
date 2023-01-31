import connexion
from flask import abort, jsonify, g
from retrying import RetryError

import openapi_server.controllers.address_controller as address
import openapi_server.controllers.invitation_controller_ as invitation
import openapi_server.helper.patch_calls as patch
from openapi_server.models import InvitationCreateBody
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.user_address_body import UserAddressBody  # noqa: E501


def root_get():  # noqa: E501
    """Welcome to the GoGretzky API

     # noqa: E501


    :rtype: str
    """
    return 'Welcome to the GoGretzky API'

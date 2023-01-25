import connexion
import six
import openapi_server.controllers.invitation_controller_ as invitation
import openapi_server.controllers.security_controller_ as sec

from indykite_sdk.identity import IdentityClient
from flask import abort

from openapi_server.models import InvitationCreateBody
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501
from openapi_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from openapi_server.models.user_address_body import UserAddressBody  # noqa: E501
from openapi_server.models.user_child_body import UserChildBody  # noqa: E501
from openapi_server.models.user_subscription_body import UserSubscriptionBody  # noqa: E501
from openapi_server import util

def root_get():  # noqa: E501
    """Welcome to the GoGretzky API

     # noqa: E501


    :rtype: str
    """
    return 'Welcome to the GoGretzky API'


def user_address_get():  # noqa: E501
    """Get the home address of the logged in user

     # noqa: E501


    :rtype: InlineResponse200
    """
    return {
        "zip": "12345",
        "number": 123,
        "country": "USA",
        "city": "Anytown",
        "street": "Main St",
        "state": "CA"
    }


def user_address_post(user_address_body=None):  # noqa: E501
    """Add a home address to the logged in user

     # noqa: E501

    :param user_address_body: 
    :type user_address_body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        user_address_body = UserAddressBody.from_dict(connexion.request.get_json())  # noqa: E501
    return {
        "street": "Main St",
        "number": 123,
        "city": "Anytown",
        "state": "CA",
        "zip": "12345",
        "country": "USA"
    }


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


def user_email_get(token_info):  # noqa: E501
    """Get the email of the logged in user

     # noqa: E501


    :rtype: str
    """
    client = IdentityClient()
    digital_twin = client.get_digital_twin_by_token(token_info['indykite_token'], ["email"])
    if digital_twin is None:
        return abort(404, description="Resource not found")
    return digital_twin['digitalTwin'].properties[0].value


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


def invitation_get(invitation_id):  # noqa: E501
    """Get the invitation by id

     # noqa: E501

    :param invitation_id: Id of the invitation to get
    :type invitation_id: str

    :rtype: InvitationInformationBody
    """
    return {
              "tenant_id": "gid:abcdefghijklmno",
              "message_attributes": [
                "gid:aakkkkaaakkkaa"
              ],
              "reference_id": "gid:1111kkkkk1111kkkkk111",
              "accepted_by": "gid:kkkkkkiiiiiikkkkkkk",
              "expire_time": "2000-01-23T04:56:07.000+00:00",
              "invite_at_time": "2000-01-23T04:56:07.000+00:00",
              "state": "INVITATION_STATE_ACCEPTED",
              "invitee": "xxx@xxx.xx"
            }


def invitation_create(token_info, invitation_create_body=None):  # noqa: E501
    """Invite a parent by email

     # noqa: E501

    :param token_info: Bearer token of the user
    :type token_info: str
    :param invitation_create_body:
    :type invitation_create_body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        invitation_create_body = InvitationCreateBody.from_dict(connexion.request.get_json())  # noqa: E501
    i = invitation.create_invitation(token_info['indykite_token'], invitation_create_body.invitee)
    if i is None:
        return abort(404, description="Resource not found")
    return "Successfully Created"


def invitations_get(parent_id=None):  # noqa: E501
    """Gets all invitations for the parent

     # noqa: E501

     :param parent_id: The GID of the parent who's invitations should be listed
     :type parent_id: str

    :rtype: InvitationInformationBody
    """
    return [{
              "tenant_id": "gid:abcdefghijklmno",
              "message_attributes": [
                "gid:aakkkkaaakkkaa"
              ],
              "reference_id": "gid:1111kkkkk1111kkkkk111",
              "accepted_by": "gid:kkkkkkiiiiiikkkkkkk",
              "expire_time": "2000-01-23T04:56:07.000+00:00",
              "invite_at_time": "2000-01-23T04:56:07.000+00:00",
              "state": "INVITATION_STATE_ACCEPTED",
              "invitee": "xxx@xxx.xx"
            }]

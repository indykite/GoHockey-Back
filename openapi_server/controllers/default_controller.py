import connexion
from flask import abort, jsonify, g
from retrying import RetryError

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


def user_address_get(token_info):  # noqa: E501
    """Get the home address of the logged in user

     # noqa: E501


    :rtype: InlineResponse200
    """
    digital_twin = g.indykite_client.get_digital_twin_by_token(token_info['indykite_token'], ["uuid"])
    if digital_twin is None:
        return abort(404, description="Resource not found")
    success = g.knowledge_client.execute()
    if not success:
        return abort(422, description="KB error")
    return jsonify(success), 200


def user_address_post(token_info, user_address_body=None):  # noqa: E501
    """Add a home address to the logged in user

     # noqa: E501

    :param token_info: user_address_body:
    :type user_address_body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        user_address_body = UserAddressBody.from_dict(connexion.request.get_json())  # noqa: E501
    if user_address_body:
        return abort(400, description="Address empty or invalid")
    digital_twin = g.indykite_client.get_digital_twin_by_token(token_info['indykite_token'], ["uuid"])
    if digital_twin is None:
        return abort(404, description="Resource not found")
    data = {
        "street": user_address_body.street,
        "number": user_address_body.number,
        "city": user_address_body.city,
        "state": user_address_body.state,
        "zip": user_address_body.zip,
        "country": user_address_body.country,
        "subscriptions": None,
        "parent": digital_twin['digitalTwin'].properties[0].value
    }
    success = g.knowledge_client.execute()
    if not success:
        return abort(422, description="KB error")
    return jsonify(success), 200


def invitation_get(invitation_id):  # noqa: E501
    """Get the invitation by id

     # noqa: E501

    :param invitation_id: Id of the invitation to get
    :type invitation_id: str

    :rtype: InvitationInformationBody
    """
    resp = invitation.get_one_invitation(invitation_id)
    if resp is None:
        return abort(404, description="Resource not found")
    return resp


def invitation_create(token_info, invitation_create_body=None):  # noqa: E501
    """Invite a parent by email and stores the generated reference ID as an extid in the inviter's property

     # noqa: E501

    :param token_info: Bearer token of the user
    :type token_info: dict
    :param invitation_create_body:
    :type invitation_create_body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        invitation_create_body = InvitationCreateBody.from_dict(connexion.request.get_json())  # noqa: E501
    try:
        resp = invitation.create_invitation(
            token_info['indykite_token'],
            invitation_create_body.invitee
        )
        print("Response: %s" % resp)
    except RetryError:
        return abort(404, description="Failed to send out the invitation")
    if resp is None:
        return abort(404, description="Sending invitation failed")

    patch.add_invitation_to_inviter_digital_twin_properties(token_info['indykite_token'], resp["reference_id"])

    return {
        "reference_id": resp["reference_id"]
    }


def invitations_get(token_info):  # noqa: E501
    """Gets all invitations for the parent

     # noqa: E501

    :param token_info: Bearer token of the user
    :type token_info: dict

    :rtype: InvitationInformationBody
    """
    info = invitation.get_all_invitations(token_info['indykite_token'])
    return info

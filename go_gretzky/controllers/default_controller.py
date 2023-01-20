import connexion
import six

from go_gretzky.models.inline_response200 import InlineResponse200  # noqa: E501
from go_gretzky.models.inline_response2001 import InlineResponse2001  # noqa: E501
from go_gretzky.models.user_address_body import UserAddressBody  # noqa: E501
from go_gretzky.models.user_child_body import UserChildBody  # noqa: E501
from go_gretzky.models.user_subscription_body import UserSubscriptionBody  # noqa: E501
from go_gretzky import util


def user_address_get():  # noqa: E501
    """Get the home address of the logged in user

     # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def user_address_post(body=None):  # noqa: E501
    """Add a home address to the logged in user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserAddressBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_child_child_id_get(child_id):  # noqa: E501
    """Get the child by id

     # noqa: E501

    :param child_id: Id of the child to get
    :type child_id: str

    :rtype: UserChildBody
    """
    return 'do some magic!'


def user_child_post(body=None):  # noqa: E501
    """Add a child to the logged in user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserChildBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_email_get():  # noqa: E501
    """Get the email of the logged in user

     # noqa: E501


    :rtype: str
    """
    return 'do some magic!'


def user_subscription_get():  # noqa: E501
    """Get the subscription of the logged in user

     # noqa: E501


    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def user_subscription_post(body=None):  # noqa: E501
    """Add a subscription to the logged in user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = UserSubscriptionBody.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

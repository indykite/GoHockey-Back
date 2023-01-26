from indykite_sdk.indykite.identity.v1beta2 import identity_management_api_pb2 as pb2
from flask import g
import openapi_server.helper.format_helper as helper

from flask import g


def info_from_bearerAuth(token):
    """
    Check and retrieve authentication information from custom bearer token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.

    :param token: Token provided by Authorization header
    :type token: str
    :return: Decoded token information or None if token is invalid
    :rtype: dict | None
    """
    g.indykite_graph_client.set_authorization(token)
    return {'indykite_token': token}


def introspect_token(token):
    """
    Sends and introspect token request to Indykite platform via indykite-sdk-python package. Upon success, it decodes
    the response into a json dictionary for proper handling
    Args:
        token: the token to introspect

    Returns: dictionary with the response or None if there were any errors

    """
    try:
        resp = g.indykite_client.stub.TokenIntrospect(
            pb2.TokenIntrospectRequest(token=token)
        )
        formatted_response = helper.decode_response(resp)
        print("Token introspection was success for the following digital twin: %s"
              % formatted_response['tokenInfo']['subject']['id'])
    except Exception as e:
        print("Introspection failed: %s" % e)
        return None

    return formatted_response

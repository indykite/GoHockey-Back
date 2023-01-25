import openapi_server.helper.format_helper as helper

from typing import List
from indykite_sdk.identity import IdentityClient
from indykite_sdk.indykite.identity.v1beta2 import identity_management_api_pb2 as pb2


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
    return {'indykite_token': token}


def create_identity_client_connection():
    """
    Creates a client connection to Indykite platform using the indykite-sdk-python IdentityClient.
    If it managed to create the connection then it returns with the connection, otherwise it returns with None.
    Whatever will use this function need to handle the connection failure.
    Returns: connection if it established successfully, None otherwise.

    """
    try:
        client = IdentityClient()
        return client
    except Exception as e:
        print("Failed to open Client connection to Indykite: %s" % e)
        return None


def close_identity_client_connection(client):
    """
    Attempts to close the given client connection to Indykite platform. It's a courtesy method to not open too much
    connection to the platform and try to avoid unnecessary _InactiveRpc errors
    Args:
        client: The client connection to Indykite platform

    Returns: It doesn't return anything

    """
    try:
        client.channel.close()
        print("Client connection has been closed")
    except Exception as e:
        print("Failed to close the Client connection to Indykite: %s" % e)


def introspect_token(client, token):
    """
    Sends and introspect token request to Indykite platform via indykite-sdk-python package. Upon success, it decodes
    the response into a json dictionary for proper handling
    Args:
        client: the open client connection to Indykite platform
        token: the token to introspect

    Returns: dictionary with the response or None if there were any errors

    """
    try:
        resp = client.stub.TokenIntrospect(
            pb2.TokenIntrospectRequest(token=token)
        )
        formatted_response = helper.decode_response(resp)
        print("Token introspection was success for the following digital twin: %s"
                     % formatted_response['tokenInfo']['customerId'])
    except Exception as e:
        print("Introspection failed: %s" % e)
        return None

    return formatted_response

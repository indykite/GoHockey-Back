import logging
import openapi_server.helper.format_helper as helper

from typing import List
from indykite_sdk.identity import IdentityClient
from indykite_sdk.indykite.identity.v1beta2 import identity_management_api_pb2 as pb2


def info_from_bearerAuth(token):
    """
    Check and retrieve authentication information from custom bearer token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.

    :param token Token provided by Authorization header
    :type token: str
    :return: Decoded token information or None if token is invalid
    :rtype: dict | None
    """
    return {'indykite_token': token}


def create_identity_client_connection():
    try:
        client = IdentityClient(False)
        return client
    except Exception as e:
        logging.debug("Failed to open Client connection to Indykite: %s" % e)
        return e


def close_identity_client_connection(client):
    try:
        client.channel.close()
        logging.info("Client connection has been closed")
    except Exception as e:
        logging.debug("Failed to close the Client connection to Indykite: %s" % e)


def introspect_token(client, token):
    try:
        resp = client.stub.TokenIntrospect(
            pb2.TokenIntrospectRequest(token=token)
        )
        formatted_response = helper.decode_response(resp)
        logging.info("Token introspection was success for the following digital twin: %s"
                     % formatted_response['tokenInfo']['customerId'])
    except Exception as e:
        logging.info("Introspection failed: %s" % e)
        return None

    return formatted_response

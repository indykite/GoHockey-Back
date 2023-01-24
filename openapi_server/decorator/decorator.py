from indykite_sdk.identity import IdentityClient
from flask import g, abort

from openapi_server.helper.graphql_client import KnowledgeGraphqlClient


def before_request_callback():
    """
    Creates a client connection to Indykite platform using the indykite-sdk-python IdentityClient.
    If it managed to create the connection then it returns with the connection, otherwise it returns with None.
    Whatever will use this function need to handle the connection failure.
    Returns: connection if it established successfully, None otherwise.

    """
    try:
        g.indykite_graph_client = KnowledgeGraphqlClient()
        g.indykite_client = IdentityClient()
    except Exception as e:
        abort(503, "Failed to open Client connection to Indykite")


def after_request_callback(response):
    """
    Attempts to close the given client connection to Indykite platform. It's a courtesy method to not open too much
    connection to the platform and try to avoid unnecessary _InactiveRpc errors
    Args:
        client: The client connection to Indykite platform

    Returns: It doesn't return anything
    :param response:

    """
    try:
        g.indykite_client.channel.close()
    except Exception as e:
        print("Failed to close the Client connection to Indykite: %s" % e)
    return response

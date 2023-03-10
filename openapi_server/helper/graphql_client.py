import os

from flask import abort
from gql import Client
from gql.transport.requests import RequestsHTTPTransport


class KnowledgeGraphqlClient:
    def __init__(self):
        # Select your transport with a defined url endpoint
        self.addr = os.getenv('INDYKITE_KNOWLEDGE_GRAPH_ADDRESS')
        if not self.addr:
            abort(503, "Missing INDYKITE_KNOWLEDGE_GRAPH_ADDRESS environment variable")
        self.transport = None
        self.client = None

    def set_authorization(self, token):
        token = os.getenv('KNOWLEDGE_GRAPH_WORKAROUND_TOKEN')
        if not self.addr:
            abort(503, "Missing KNOWLEDGE_GRAPH_WORKAROUND_TOKEN environment variable")
        self.transport = RequestsHTTPTransport(
            url=self.addr,
            verify=True,
            retries=3,
            headers={"Authorization": token},
        )
        # Create a GraphQL client using the defined transport
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    def execute(self, query, params=None):
        if not self.client:
            abort(503, "KnowledgeGraphqlClient client is not initialized")
        return self.client.execute(query, variable_values=params)

#!/usr/bin/env python3

import connexion
from openapi_server.decorator.decorator import before_request_callback, after_request_callback
from openapi_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'GoGretzky API'},
                pythonic_params=True)
    app.app.before_request(before_request_callback)
    app.app.after_request(after_request_callback)
    app.run(port=8080)


if __name__ == '__main__':
    main()

from indykite_sdk.identity import IdentityClient
from jose import JWTError, jwt
from werkzeug.exceptions import Unauthorized
from indykite_sdk.indykite.identity.v1beta1 import identity_management_api_pb2 as pb2

JWT_ISSUER = "https://jarvis.indykite.com"
JWT_SECRET = ""
JWT_LIFETIME_SECONDS = 600
JWT_ALGORITHM = "ES256"


def check_bearerAuth(token):
    client = IdentityClient()
    response = client.stub.TokenIntrospect(pb2.TokenIntrospectRequest(token=token))
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        raise Unauthorized from e

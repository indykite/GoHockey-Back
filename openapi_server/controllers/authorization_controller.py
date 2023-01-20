from jose import JWTError, jwt
from werkzeug.exceptions import Unauthorized

JWT_ISSUER = "com.zalando.connexion"
JWT_SECRET = "change_this"
JWT_LIFETIME_SECONDS = 600
JWT_ALGORITHM = "HS256"


def check_bearerAuth(token):
    try:
        return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    except JWTError as e:
        raise Unauthorized from e

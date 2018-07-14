from rest_framework_jwt.utils import jwt_encode_handler
from rest_framework_jwt.utils import jwt_payload_handler


def get_jwt_token(user):
    return jwt_encode_handler(jwt_payload_handler(user))

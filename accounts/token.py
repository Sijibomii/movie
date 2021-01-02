import jwt
from datetime import datetime, timedelta
from decouple import config


class token():
    def get_access_token(payload):
        return jwt.encode(
            {"exp": datetime.now() + timedelta(minutes=5), **payload},
            config('SECRET_KEY'),
            algorithm="HS256"
        )

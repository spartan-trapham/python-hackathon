from datetime import datetime, timedelta, timezone
from typing import Any

import jwt

ALGORITHM = "HS256"


def create_token(data: dict, token_expire_seconds: int, jwt_secret_key: str):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(seconds=token_expire_seconds)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, jwt_secret_key, algorithm=ALGORITHM)
    return encoded_jwt


def decode_token(token: str, jwt_secret_key: str) -> Any:
    try:
        return jwt.decode(token, jwt_secret_key, ALGORITHM)
    except Exception:
        return None

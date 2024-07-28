import uuid
from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel


class User(BaseModel):
    id: uuid.UUID
    email: str
    created_at: Optional[Union[datetime, str, None]] = None
    updated_at: Optional[Union[datetime, str, None]] = None
    deleted_at: Optional[Union[datetime, str, None]] = None


def to_user(user: dict) -> User:
    return User(**user)


def to_users(users: [dict]) -> [User]:
    return [User(**user) for user in users]

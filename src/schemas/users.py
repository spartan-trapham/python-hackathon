import uuid
from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, Field


class UserCreateRequest(BaseModel):
    name: str = Field(default=None)
    email: str = Field(default=None)


class UserResponse(BaseModel):
    id: uuid.UUID = Field(default=None)
    name: str = Field(default=None)
    email: str = Field(default=None)
    created_at: Optional[Union[datetime, str, None]] = None
    updated_at: Optional[Union[datetime, str, None]] = None
    deleted_at: Optional[Union[datetime, str, None]] = None

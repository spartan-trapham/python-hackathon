from datetime import datetime
import uuid

from sqlalchemy import update
from sqlalchemy.orm import Session
from sqlalchemy.engine import Connection
from ..models import User
from ...core.app_exceptions import AppException
from ...errors.error_codes import USER_NOT_FOUND

class UserRepository:
    def by_id(self, session: Session, user_id: uuid.UUID):
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            raise AppException(USER_NOT_FOUND)
        return user

    def insert(self, session: Session, user: User):
        session.add(user)
        return user

    def soft_delete(self, connection: Connection, user_id: uuid.UUID):
        stmt = (
            update(User.__table__)
            .where(User.c.id == user_id)
            .values(deleted_at=datetime.datetime.utcnow())
        )
        return connection.execute(stmt)

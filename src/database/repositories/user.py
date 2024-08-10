import uuid
from datetime import datetime

from sqlalchemy import update, delete
from sqlalchemy.engine import Connection
from sqlalchemy.orm import Session

from src.database.models.user_roles import UserRole
from ..models import User
from ...common.errors.app_exceptions import AppException
from ...common.errors.error_codes import USER_NOT_FOUND


class UserRepository:
    async def by_id(self, session: Session, user_id: uuid.UUID):
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            raise AppException(USER_NOT_FOUND)
        return user

    async def by_email(self, session: Session, email: str) -> User:
        user = await session.query(User).filter(User.email == email).first()
        if not user:
            raise AppException(USER_NOT_FOUND)
        return user

    async def insert(self, session: Session, user: User) -> User:
        session.add(user)
        return user

    async def soft_delete(self, connection: Connection, user_id: uuid.UUID):
        stmt = (
            update(User.__table__)
            .where(User.c.id == user_id)
            .values(deleted_at=datetime.datetime.utcnow())
        )
        return await connection.execute(stmt)

    async def delete_user(self, connection: Connection, user_id: uuid.UUID):
        stmt = delete(UserRole.__table__).where(UserRole.c.user_id == user_id)
        connection.execute(stmt)
        stmt = delete(User.__table__).where(User.c.id == user_id)
        connection.execute(stmt)
        return

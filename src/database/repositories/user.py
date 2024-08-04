import uuid

from .base import BaseRepository
from ..models import User
from ...core.app_exceptions import AppException
from ...errors.error_codes import USER_NOT_FOUND


class UserRepository(BaseRepository):
    def by_id(self, user_id: uuid.UUID):
        with self.session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                raise AppException(USER_NOT_FOUND)
            return user

    def insert(self, user: User):
        with self.session() as session:
            session.add(user)
            session.commit()

        return user

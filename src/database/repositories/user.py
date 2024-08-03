import uuid

from .base import BaseRepository
from .errors import NotFoundError
from ..models import User


class UserRepository(BaseRepository):
    def by_id(self, user_id: uuid.UUID):
        with self.session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if not user:
                raise UserNotFoundError(entity_id=user)
            return user

    def insert(self, user: User):
        with self.session() as session:
            session.add(user)
            session.commit()

        return user


class UserNotFoundError(NotFoundError):
    entity_name: str = "User"

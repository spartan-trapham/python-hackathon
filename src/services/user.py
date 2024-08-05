import uuid

from .base import BaseService
from ..database.db import Database
from ..database.models import User
from ..database.repositories.user import UserRepository
from ..schemas.users import UserCreateRequest


# from ..worker.brokers.critical import usertask_remove_user


class UserService(BaseService):
    def __init__(self, db: Database, user_repo: UserRepository):
        super().__init__()
        self.user_repo = user_repo
        self.db = db

    def by_id(self, user_id: uuid.UUID) -> User:
        self.logger.info(f"Get user by ID: {user_id}")

        with self.db.session() as session:
            return self.user_repo.by_id(session, user_id)

    def insert(self, user_request: UserCreateRequest) -> User:
        self.logger.info(f"Insert a user with name: {user_request.name}")

        user = User()
        user.name = user_request.name
        user.email = user_request.email

        with self.db.session() as session:
            return self.user_repo.insert(session, user)

    def remove(self, user_id: uuid.UUID) -> None:
        self.logger.info(f"Remove user by ID: {user_id}")

        with self.db.connect() as connect:
            self.user_repo.soft_delete(connect, user_id)
            # usertask_remove_user.apply_async(user_id)

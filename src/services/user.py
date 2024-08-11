from time import sleep
import uuid

from celery import Celery

from .base import BaseService
from ..database.db import Database
from ..database.models import User
from ..database.repositories.user import UserRepository
from ..schemas.users import UserCreateRequest

class UserService(BaseService):
    def __init__(self, db: Database, user_repo: UserRepository, scheduler: Celery):
        super().__init__()
        self.user_repo = user_repo
        self.db = db
        self.scheduler = scheduler

    async def by_id(self, user_id: uuid.UUID) -> User:
        self.logger.info(f"Get user by ID: {user_id}")
        user: User
        with self.db.session() as session:
            self.logger.info(f"Send email to user ID: {user_id}")
            user = await self.user_repo.by_id(session, user_id)
        return user

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
            self.scheduler.send_task("scheduler.remove_user", [user_id])

    def remove_user(self, user_ids: list[uuid.UUID]):
        self.logger.info(f"Start to remove user ids {user_ids}".format_map(user_ids=user_ids))
        self.user_repo.delete_user(user_ids)
        self.logger.info(f"Finish remove user ids {user_ids}".format_map(user_ids=user_ids))

    def update_avatar(self, userid: uuid.UUID, image_path: str):
        self.logger.info(f"Start to upload avatar at {image_path} to user ids {userid}".format_map(userid=userid, image_path=image_path))
        sleep(5)
        self.logger.info(f"Finish upload avatar")

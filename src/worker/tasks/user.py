from logging import Logger
from time import sleep
import uuid

from src.database.repositories.user import UserRepository
from celery import Celery

class UserTask(Celery):
    def __init__(self, celery: Celery, user_repo: UserRepository, logger: Logger):
      self.user_repo = user_repo
      self.logger = logger
      self.client = celery

    def send_email(self, user_ids: list[uuid.UUID]):
        self.logger.info(f"Start to send email to user ids {user_ids}".format_map(user_ids=user_ids))

    def remove_user(self, user_ids: list[uuid.UUID]):
        self.logger.info(f"Start to remove user ids {user_ids}".format_map(user_ids=user_ids))
        self.user_repo.delete_user(user_ids)
        self.logger.info(f"Finish remove user ids {user_ids}".format_map(user_ids=user_ids))

    def update_avatar(self, userid: uuid.UUID, image_path: str):
        self.logger.info(f"Start to upload avatar at {image_path} to user ids {userid}".format_map(userid=userid, image_path=image_path))
        sleep(5)
        self.logger.info(f"Finish upload avatar")

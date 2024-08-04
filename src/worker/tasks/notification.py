from logging import Logger
from time import sleep
import uuid

from celery import Celery

class NotificationTask(Celery):
    def __init__(self, celery: Celery, logger: Logger):
      self.logger = logger
      self.client = celery

    def fire_notification(self, user_ids: list[uuid.UUID]):
        self.logger.info(f"Start to fire notification to {0}".format(user_ids))
        sleep(10)
        self.logger.info(f"Finish fire notification")

from logging import Logger
from time import sleep
import uuid

from celery import Celery

class NotificationTask:
    def __init__(self, logger: Logger):
      self.logger = logger

    def fire_notification(self, user_ids: list[uuid.UUID]):
        self.logger.info(f"Start to fire notification to {0}".format(user_ids))
        sleep(10)
        self.logger.info(f"Finish fire notification")

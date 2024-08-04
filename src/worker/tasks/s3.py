from logging import Logger
from time import sleep

from celery import Celery

class S3Task(Celery):
    def __init__(self, celery: Celery, s3: S3, logger: Logger):
      self.s3 = s3
      self.logger = logger
      self.client = celery

    def clean_up(self):
        self.logger.info(f"Start to clean up garbage files")
        sleep(10)
        self.logger.info(f"Finish clean up garbage files")

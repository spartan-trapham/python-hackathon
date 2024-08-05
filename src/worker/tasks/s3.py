from logging import Logger
from time import sleep

from src.libs.s3.client import S3Client

class S3Task:
    def __init__(self, s3: S3Client, logger: Logger):
      self.s3 = s3
      self.logger = logger

    def clean_up(self):
        self.logger.info(f"Start to clean up garbage files")
        sleep(10)
        self.logger.info(f"Finish clean up garbage files")

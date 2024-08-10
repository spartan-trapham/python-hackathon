import logging
from time import sleep

from src.libs.s3.client import S3Client


class FileService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.s3 = S3Client()

    def clean_up(self):
      self.logger.info(f"Start to clean up garbage files")
      sleep(10)
      self.logger.info(f"Finish clean up garbage files")

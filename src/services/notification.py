import logging
from time import sleep
import uuid


class NotificationService:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def send_notification(self, user_ids: list[uuid.UUID]):
        self.logger.info(f"Start to fire notification to {0}".format(user_ids))
        sleep(10)
        self.logger.info(f"Finish fire notification")

    def send_email(self, user_ids: list[uuid.UUID]):
        self.logger.info(f"Start to send email to user ids {user_ids}".format_map(user_ids=user_ids))
        sleep(10)
        self.logger.info(f"Finish send email")

    def send_sms(self, user_ids: list[uuid.UUID]):
        self.logger.info(f"Start to send sms to user ids {user_ids}".format_map(user_ids=user_ids))
        sleep(10)
        self.logger.info(f"Finish send sms")

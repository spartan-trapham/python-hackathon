from src.containers.container import Container
from src.database.repositories.user import UserRepository
from src.libs.log import logging
import uuid
from celery import Celery

from src.configs.config import Configuration
# from src.containers.container import Container
from src.libs.s3.client import S3Client
from src.worker.tasks.notification import NotificationTask
from src.worker.tasks.s3 import S3Task
from src.worker.tasks.user import UserTask

# get configuration here
logger = logging.setup_logger(__name__)

config = Configuration().get_config().celery
notif_task = NotificationTask(logger)
user_task = UserTask(UserRepository(), logger)
s3_task = S3Task(S3Client(), logger)

scheduler = Container.scheduler()

@scheduler.task()
def notificationtask_fire_notification(user_ids: list[uuid.UUID]):
    return notif_task.fire_notification(user_ids)

@scheduler.task()
def s3task_clean_up():
    return s3_task.clean_up()

@scheduler.task()
def usertask_send_email(self, user_id: list[uuid.UUID]):
    return user_task.send_email(user_id)

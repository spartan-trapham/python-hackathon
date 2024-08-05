import uuid

from celery import Celery

from src.containers.container import Container
from src.worker.tasks.notification import NotificationTask
from src.worker.tasks.s3 import S3Task
from src.worker.tasks.user import UserTask

scheduler_worker = Celery(main="scheduler", broker=celery_config.scheduler.broker_url,
                          backend=celery_config.scheduler.backend_url)


# @scheduler_worker.task(base=NotificationTask, bind=True)
def notificationtask_fire_notification(self):
    return self.fire_notification()


# @scheduler_worker.task(base=S3Task, bind=True)
def s3task_clean_up(self):
    return self.clean_up()


# @scheduler_worker.task(base=UserTask, bind=True)
def usertask_send_email(self, user_id: list[uuid.UUID]):
    return self.send_email(user_id)

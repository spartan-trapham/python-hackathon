import uuid
from celery import Celery

from src.containers.container import Container
from src.worker.tasks.notification import NotificationTask
from src.worker.tasks.s3 import S3Task
from src.worker.tasks.user import UserTask

# get configuration here
config = Container().configuration().celery

scheduler = Celery("scheduler", broker=config.scheduler.broker_url, backend=config.scheduler.backend_url)

@scheduler.task(base=NotificationTask, bind=True)
def notificationtask_fire_notification(self):
    return self.fire_notification()

@scheduler.task(base=S3Task, bind=True)
def s3task_clean_up(self):
    return self.clean_up()

@scheduler.task(base=UserTask, bind=True)
def usertask_send_email(self, user_id: list[uuid.UUID]):
    return self.send_email(user_id)

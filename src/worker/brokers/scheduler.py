from celery import Celery

from src.worker.tasks.notification import NotificationTask
from src.worker.tasks.s3 import S3Task

# get configuration here

scheduler = Celery("scheduler", broker=config.scheduler.broker_url, backend=config.scheduler.backend_url)

@scheduler.task(base=NotificationTask, bind=True)
def notificationtask_fire_notification(self):
    return self.fire_notification()

@scheduler.task(base=S3Task, bind=True)
def s3task_clean_up(self):
    return self.clean_up()

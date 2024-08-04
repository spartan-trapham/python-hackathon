import uuid
from celery import Celery

from src.worker.tasks.user import UserTask

# get configuration here

critical = Celery("critical", broker=config.critical.broker_url, backend=config.critical.backend_url)

@critical.task(base=UserTask, bind=True)
def usertask_remove_user(self, user_ids: list[uuid.UUID]):
    return self.remove_user(user_ids)

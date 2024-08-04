import uuid
from celery import Celery

from src.containers.container import Container
from src.worker.tasks.user import UserTask

# get configuration here
config = Container().configuration().celery

critical = Celery("critical", broker=config.critical.broker_url, backend=config.critical.backend_url)

@critical.task(base=UserTask, bind=True)
def usertask_remove_user(self, user_ids: list[uuid.UUID]):
    return self.remove_user(user_ids)

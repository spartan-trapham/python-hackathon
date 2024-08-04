import uuid
from celery import Celery

from src.containers.container import Container
from src.worker.tasks.user import UserTask

# get configuration here
config = Container().configuration().celery

internal = Celery("internal", broker=config.internal.broker_url, backend=config.internal.backend_url)

@internal.task(base=UserTask, bind=True)
def usertask_update_avatar(self, userid: uuid.UUID, image_path: str):
    return self.update_avatar(userid, image_path)

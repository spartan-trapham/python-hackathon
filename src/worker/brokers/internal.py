import uuid
from celery import Celery
from src.containers.container import Container
from src.worker.tasks.user import UserTask

internal_worker = Celery(main="internal", broker=celery_config.internal.broker_url, backend=celery_config.internal.backend_url)


# @internal_worker.task(base=UserTask, bind=True)
def usertask_update_avatar(self, userid: uuid.UUID, image_path: str):
    return self.update_avatar(userid, image_path)

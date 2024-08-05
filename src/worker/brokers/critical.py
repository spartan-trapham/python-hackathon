import uuid

from celery import Celery
from ..tasks.user import UserTask
from ...containers.container import Container

# critical_worker = Celery(main="critical", broker=celery_config.critical.broker_url, backend=celery_config.critical.backend_url)


# @critical_worker.task(base=UserTask, bind=True)
def usertask_remove_user(self, user_ids: list[uuid.UUID]):
    return self.remove_user(user_ids)

from src.containers.container import Container
from src.database.repositories.user import UserRepository
from src.libs.log import logging
import uuid

from src.configs.config import Configuration
# from src.containers.container import Container
from src.worker.tasks.user import UserTask

# get configuration here

logger = logging.setup_logger(__name__)

config = Configuration().get_config().celery
user_task = UserTask(UserRepository(), logger)
internal = Container.internal()

@internal.task()
def usertask_update_avatar(self, userid: uuid.UUID, image_path: str):
    return user_task.update_avatar(userid, image_path)

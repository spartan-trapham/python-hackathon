from src.containers.container import Container
from src.libs.log import logging
import uuid

# from src.containers.container import Container
from src.configs.config import Configuration
from src.database.repositories.user import UserRepository
from src.worker.tasks.user import UserTask

# get configuration here
logger = logging.setup_logger(__name__)

config = Configuration().get_config().celery
user_task = UserTask(UserRepository(), logger)
critical = Container.critical()

@critical.task()
def usertask_remove_user(user_ids: list[uuid.UUID]):
    return user_task.remove_user(user_ids)

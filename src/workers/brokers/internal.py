from celery import Celery
from src.containers.service_container import ServiceContainer
import uuid


container = ServiceContainer()
internal: Celery = container.internal()

@internal.task()
def usertask_update_avatar(userid: uuid.UUID, image_path: str):
    user_service = container.user_service()
    return user_service.update_avatar(userid, image_path)


if __name__ == "__main__":
    internal.start()

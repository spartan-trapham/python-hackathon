import uuid

from celery import Celery

from src.containers.service_container import ServiceContainer
from src.services.user import UserService

container = ServiceContainer()
critical: Celery = container.critical()

@critical.task()
def remove_user(user_ids: list[uuid.UUID]):
    user_service: UserService = container.user_service()
    return user_service.remove_user(user_ids)


if __name__ == "__main__":
    critical.start()

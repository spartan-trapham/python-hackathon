import uuid

from src.containers.container import Container

container = Container()
critical = container.critical()

@critical.task()
def remove_user(user_ids: list[uuid.UUID]):
    user_service = container.user_service()
    return user_service.remove_user(user_ids)

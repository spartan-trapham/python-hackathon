from src.containers.container import Container
import uuid


container = Container()
internal = container.internal()

@internal.task()
def usertask_update_avatar(userid: uuid.UUID, image_path: str):
    user_service = container.user_service()
    return user_service.update_avatar(userid, image_path)

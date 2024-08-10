import uuid
from src.containers.container import Container

container = Container()
scheduler = container.scheduler()

@scheduler.task()
def notificationtask_fire_notification(user_ids: list[uuid.UUID]):
    notification_service = container.notif_service()
    return notification_service.send_notification(user_ids)

@scheduler.task()
def s3task_clean_up():
    file_service = container.file_service()
    return file_service.clean_up()

@scheduler.task()
def usertask_send_email(self, user_id: list[uuid.UUID]):
    notification_service = container.notif_service()
    return notification_service.send_email(user_id)

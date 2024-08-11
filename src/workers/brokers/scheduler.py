import uuid

from celery import Celery
from src.containers.service_container import ServiceContainer

container = ServiceContainer()
scheduler: Celery = container.scheduler()

@scheduler.task(name='scheduler.notificationtask_fire_notification')
def notificationtask_fire_notification(user_ids: list[uuid.UUID]):
    notification_service = container.notif_service()
    return notification_service.send_notification(user_ids)

@scheduler.task(name='scheduler.s3task_clean_up')
def s3task_clean_up():
    file_service = container.file_service()
    return file_service.clean_up()

@scheduler.task(name='scheduler.usertask_send_email')
def usertask_send_email(user_ids: list[uuid.UUID]):
    notification_service = container.notif_service()
    return notification_service.send_email(user_ids)


if __name__ == "__main__":
    scheduler.start()

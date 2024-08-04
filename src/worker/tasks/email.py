import uuid

from .base import BaseTask
from ...containers.container import Container
from ...core.logging import setup_logger

logger = setup_logger(__name__)

app = Container.celery().client


@app.task(bind=True, base=BaseTask, autoretry_for=(Exception,), default_retry_delay=5)
def send_email(self, user_ids: list[uuid.UUID] = None, **kwargs):
    logger.info(f"Start to send email to user ids {user_ids}")

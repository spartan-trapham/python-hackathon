import uuid

from dependency_injector.wiring import (
    inject,
)
from fastapi import APIRouter
from starlette.requests import Request

from src.libs.log import logging
from src.worker.brokers.scheduler import usertask_send_email

router = APIRouter(prefix="/tasks")
logger = logging.setup_logger(__name__)


@router.get('/send-email/{user_id}', response_model=uuid.UUID)
@inject
async def get(request: Request, user_id: uuid.UUID):
    logger.info(f"Execute send email task for user id {user_id}")
    task = usertask_send_email.delay([user_id])
    return task.id

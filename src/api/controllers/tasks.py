import uuid

from celery import Celery
from dependency_injector.wiring import (
    inject,
    Provide,
)
from fastapi import APIRouter, Depends
from starlette.requests import Request

from src.containers.service_container import ServiceContainer
from src.libs.log import logging

router = APIRouter(prefix="/tasks")
logger = logging.setup_logger(__name__)


@router.get('/send-email/{user_id}', response_model=uuid.UUID)
@inject
async def get(request: Request, user_id: uuid.UUID, scheduler: Celery = Depends(Provide[ServiceContainer.scheduler])):
    logger.info(f"Execute send email task for user id {user_id}")
    task = scheduler.send_task('scheduler.usertask_send_email', args=[[user_id]])
    return task.id

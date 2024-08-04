import uuid

from dependency_injector.wiring import (
    inject,
    Provide,
)
from fastapi import APIRouter, Depends
from starlette.requests import Request

from src.containers.container import Container
from src.libs.log import logging
from src.common.errors.app_exceptions import AppException
from src.common.errors.error_codes import USER_NOT_FOUND
from src.schemas.users import UserResponse
from src.services.user import UserService

router = APIRouter(prefix="/users")
logger = logging.setup_logger(__name__)


@router.get('/{id}', response_model=UserResponse)
@inject
async def get(request: Request, id: uuid.UUID, user_service: UserService = Depends(Provide[Container.user_service])):
    logger.info(f"Get user information of user {id}")

    if id == uuid.UUID('c2667213-c3b2-4a8a-b47a-ea8bd3173e49'):
        raise AppException(USER_NOT_FOUND)

    return user_service.by_id(user_id=id)

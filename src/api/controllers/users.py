import uuid

from fastapi import APIRouter
from starlette.requests import Request

from src.api.controllers.admin.responses.users import to_user
from src.core import logging
from src.exceptions.app_exceptions import AppException
from src.exceptions.error_codes import USER_NOT_FOUND
from src.utils.response import response_item

router = APIRouter(prefix="/users")
logger = logging.setup_logger(__name__)


@router.get('/me')
async def me(request: Request):
    logger.info("Get current user information")

    return response_item(to_user({"id": uuid.uuid4(), "email": "example@example.com"}))


@router.get('/{id}')
async def get(request: Request, id: uuid.UUID):
    logger.info(f"Get user information of user {id}")

    if id == uuid.UUID('c2667213-c3b2-4a8a-b47a-ea8bd3173e49'):
        raise AppException(USER_NOT_FOUND)

    return response_item(to_user({"id": id, "email": "example@example.com"}))

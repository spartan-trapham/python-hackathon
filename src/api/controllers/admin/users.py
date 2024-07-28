import uuid

from fastapi import APIRouter
from starlette.requests import Request

from src.api.controllers.admin.responses.users import to_user
from src.core import logging
from src.utils.response import response_item

router = APIRouter(prefix="/users")
logger = logging.setup_logger(__name__)


@router.get('/me')
async def me(request: Request):
    logger.info("Get current user information")

    return response_item(to_user({"id": uuid.uuid4(), "email": "example@example.com"}))

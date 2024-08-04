from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.types import ASGIApp, Scope, Receive, Send

from src.libs.log import logging
from src.common.errors.app_exceptions import AppFieldException, AppException
from src.common.errors.error_codes import UNKNOWN_ERROR, BAD_REQUEST_ERROR, UNAUTHENTICATED_ERROR, FORBIDDEN_ERROR, \
    NOT_FOUND_ERROR
from src.utils.response import response_error

logger = logging.setup_logger(__name__)


class ExceptionHandlerMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope['type'] != 'http':
            await self.app(scope, receive, send)
            return

        try:
            await self.app(scope, receive, send)
        except Exception as exception:
            logger.error(exception)
            if isinstance(exception, RequestValidationError):
                errors = []
                for error in exception.errors():
                    error_type = error.get('type')
                    message = error.get('msg')
                    field = '.'.join(error.get('loc', []))
                    errors.append(AppFieldException(type=error_type, field=field, message=message))
                new_exception = AppException(BAD_REQUEST_ERROR, errors=errors)
            elif isinstance(exception, HTTPException):
                if exception.status_code == 400:
                    new_exception = AppException(BAD_REQUEST_ERROR)
                elif exception.status_code == 401:
                    new_exception = AppException(UNAUTHENTICATED_ERROR)
                elif exception.status_code == 403:
                    new_exception = AppException(FORBIDDEN_ERROR)
                elif exception.status_code == 404:
                    new_exception = AppException(NOT_FOUND_ERROR)
                else:
                    new_exception = AppException(UNKNOWN_ERROR)
            elif isinstance(exception, AppException):
                new_exception = exception
            else:
                new_exception = AppException(UNKNOWN_ERROR)

            await response_error(new_exception)(scope, receive, send)

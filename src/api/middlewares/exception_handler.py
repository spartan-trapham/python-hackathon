from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.types import ASGIApp, Scope, Receive, Send

from src.core import logging
from src.exceptions.app_exception import AppFieldException, AppValidationException, AppException, \
    AppBadRequestException, AppUnauthorizedException, AppForbiddenException, AppNotFoundException, AppUnknownException
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
                    error_id = error.get('type')
                    message = error.get('msg')
                    field = '.'.join(error.get('loc', []))
                    errors.append(AppFieldException(error_id=error_id, field=field, message=message))
                new_exception = AppValidationException(errors=errors)
            elif isinstance(exception, HTTPException):
                if exception.status_code == 400:
                    new_exception = AppBadRequestException()
                elif exception.status_code == 401:
                    new_exception = AppUnauthorizedException()
                elif exception.status_code == 403:
                    new_exception = AppForbiddenException()
                elif exception.status_code == 404:
                    new_exception = AppNotFoundException()
                else:
                    new_exception = AppUnknownException()
            elif isinstance(exception, AppException):
                new_exception = exception
            else:
                new_exception = AppUnknownException()

            await response_error(new_exception)(scope, receive, send)

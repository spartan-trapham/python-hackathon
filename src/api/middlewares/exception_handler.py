from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.types import ASGIApp, Scope, Receive, Send

from src.core import logging
from src.exceptions.app_exceptions import AppFieldException, AppValidationException, AppException
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
                new_exception = AppValidationException(errors=errors)
            elif isinstance(exception, HTTPException):
                if exception.status_code == 400:
                    new_exception = AppException.bad_request()
                elif exception.status_code == 401:
                    new_exception = AppException.unauthorized()
                elif exception.status_code == 403:
                    new_exception = AppException.forbidden()
                elif exception.status_code == 404:
                    new_exception = AppException.not_found()
                else:
                    new_exception = AppException.unknown_error()
            elif isinstance(exception, AppException):
                new_exception = exception
            else:
                new_exception = AppException.unknown_error()

            await response_error(new_exception)(scope, receive, send)

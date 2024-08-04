from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from src.api import routers
from src.api.middlewares.authentication import AuthenticationMiddleware
from src.api.middlewares.exception_handler import ExceptionHandlerMiddleware
from src.celery_app import app as celery_app
from src.containers.container import Container
from src.utils.request import generate_request_id


def init_exception_handlers(app_: FastAPI) -> None:
    def raise_all_exceptions(request: Request, exception: Exception):
        raise exception

    app_.add_exception_handler(HTTPException, raise_all_exceptions)
    app_.add_exception_handler(RequestValidationError, raise_all_exceptions)
    app_.add_middleware(ExceptionHandlerMiddleware)


def init_routers(app_: FastAPI) -> None:
    app_.include_router(routers.router)


def init_middlewares(app_: FastAPI) -> None:
    app_.add_middleware(CORSMiddleware,
                        allow_credentials=True,
                        allow_origins=['*'],
                        allow_methods=['*'],
                        allow_headers=['*'],
                        )
    app_.add_middleware(AuthenticationMiddleware)
    app_.add_middleware(CorrelationIdMiddleware, generator=lambda: generate_request_id())


def create_app() -> FastAPI:
    container = Container()

    app_config = container.configuration().app

    app_ = FastAPI(
        host='127.0.0.1',
        title=app_config.title,
        description=app_config.description,
    )

    app_.container = container
    app_.celery_app = celery_app

    init_exception_handlers(app_)
    init_middlewares(app_)
    init_routers(app_)
    return app_


app = create_app()

from dependency_injector.wiring import (
    inject,
    Provide,
)
from fastapi import APIRouter, Depends

from ...containers.service_container import ServiceContainer
from ...libs.log import logging
from ...schemas.auth import TokenResponse, RefreshTokenRequest, LoginRequest
from ...services.auth import AuthService

router = APIRouter(prefix="/auth")
logger = logging.setup_logger(__name__)


@router.post('/login', response_model=TokenResponse)
@inject
async def login(
        login_request: LoginRequest,
        auth_service: AuthService = Depends(Provide[ServiceContainer.auth_service])
):
    logger.info("Login")
    return auth_service.login(login_request)


@router.post('/refresh-token', response_model=TokenResponse)
@inject
async def refresh_token(
        refresh_token_request: RefreshTokenRequest,
        auth_service: AuthService = Depends(Provide[ServiceContainer.auth_service])
):
    return auth_service.refresh_token(refresh_token_request)


@router.get('/logout', response_model=None)
@inject
async def login(auth_service: AuthService = Depends(Provide[ServiceContainer.auth_service])):
    return auth_service.logout()

from datetime import datetime

from .base import BaseService
from ..common.errors.app_exceptions import AppException
from ..common.errors.error_codes import UNAUTHORIZED_ERROR
from ..configs.config import AppConfig
from ..database.db import Database
from ..database.models.users import User
from ..database.repositories.user import UserRepository
from ..schemas.auth import TokenResponse, LoginRequest, RefreshTokenRequest
from ..utils.jwt_token import create_token, decode_token
from ..utils.password import verify_pwd


class AuthService(BaseService):
    def __init__(self, db: Database, user_repo: UserRepository, app_config: AppConfig):
        super().__init__()
        self.user_repo = user_repo
        self.db = db
        self.app_config = app_config

    def login(self, login_request: LoginRequest) -> TokenResponse:
        with self.db.session() as session:
            user = self.user_repo.by_email(session, login_request.email)

            if not user or not verify_pwd(login_request.password, user.password):
                raise AppException(UNAUTHORIZED_ERROR)

            return self._generate_token(user)

    def refresh_token(self, refresh_token_request: RefreshTokenRequest) -> TokenResponse:
        claim = decode_token(refresh_token_request.refresh_token, self.app_config.jwt_secret)
        if not claim:
            raise AppException(UNAUTHORIZED_ERROR)

        # return self._generate_token(user_id)

    def logout(self) -> None:
        return None

    def _generate_token(self, user: User) -> TokenResponse:
        access_token = create_token(
            {"sub": user.email},
            self.app_config.access_token_expire_seconds,
            self.app_config.jwt_secret
        )
        refresh_token = create_token(
            {"sub": user.email},
            self.app_config.refresh_token_expire_seconds,
            self.app_config.jwt_secret
        )
        expired_time = int((datetime.utcnow()).timestamp())
        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
            expired_time=expired_time
        )

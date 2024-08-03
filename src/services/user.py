import uuid

from src.core.logging import setup_logger
from src.database.models import User
from src.database.repositories.user import UserRepository
from src.schemas.users import UserCreateRequest

logger = setup_logger(__name__)


class UserService:
    def __init__(self, user_repo: UserRepository):
        self._user_repo = user_repo

    def by_id(self, user_id: uuid.UUID) -> User:
        logger.info(f"Get user by ID: {user_id}")

        return self._user_repo.by_id(user_id)

    def insert(self, user_request: UserCreateRequest) -> User:
        logger.info(f"Insert a user with name: {user_request.name}")

        user = User()
        user.name = user_request.name
        user.email = user_request.email

        return self._user_repo.insert(user)

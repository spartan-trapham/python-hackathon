import uuid

from src.core.logging import setup_logger
from src.database.models import User
from src.database.repositories.user import UserRepository
from src.libs.db.engine import DB
from src.schemas.users import UserCreateRequest

logger = setup_logger(__name__)


class UserService:
    def __init__(self, db: DB, user_repo: UserRepository):
        self._user_repo = user_repo
        self.db = db

    def by_id(self, user_id: uuid.UUID) -> User:
        logger.info(f"Get user by ID: {user_id}")

        with self.db.session as session:
            return self._user_repo.by_id(session, user_id)

    def insert(self, user_request: UserCreateRequest) -> User:
        logger.info(f"Insert a user with name: {user_request.name}")

        user = User()
        user.name = user_request.name
        user.email = user_request.email

        with self.db.session as session:
            return self._user_repo.insert(session, user)
        
    def remove(self, user_id: uuid.UUID) -> None:
        logger.info(f"Remove user by ID: {user_id}")

        with self.db.connect as connect:
            self._user_repo.soft_delete(connect, user_id)
            # app.remove_user.task(user_id)
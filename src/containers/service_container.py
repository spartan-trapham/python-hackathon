from celery import Celery
from dependency_injector import containers, providers

from src.services.files import FileService
from src.services.notification import NotificationService

from ..configs.config import Configuration
from ..database.db import Database
from ..database.repositories.user import UserRepository
from ..services.auth import AuthService
from ..services.user import UserService

class ServiceContainer(containers.DeclarativeContainer):
    configuration = providers.Singleton(Configuration().get_config)

    # Application
    db = providers.Singleton(Database, config=configuration.provided.database)

    # Background Tasks
    critical = providers.Singleton(Celery, broker=configuration.provided.celery.critical.broker_url, backend=configuration.provided.celery.critical.backend_url)
    scheduler = providers.Singleton(Celery, broker=configuration.provided.celery.scheduler.broker_url, backend=configuration.provided.celery.scheduler.backend_url)
    internal = providers.Singleton(Celery)

    # Repositories
    user_repo = providers.Factory(UserRepository)

    # Services
    user_service = providers.Factory(UserService, db=db, user_repo=user_repo, scheduler=scheduler)
    auth_service = providers.Factory(AuthService, db=db, user_repo=user_repo, app_config=configuration.provided.app)
    notif_service = providers.Factory(NotificationService)
    file_service = providers.Factory(FileService, db=db, user_repo=user_repo, app_config=configuration.provided.app)


from celery import Celery
from dependency_injector import containers, providers

from ..configs.config import Configuration
from ..database.db import Database
from ..database.repositories.user import UserRepository
from ..services.auth import AuthService
from ..services.user import UserService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=[
            "..api",
            "..api.controllers",
            "..worker",
        ]
    )
    # Configurations
    configuration = providers.Singleton(Configuration().get_config)

    # Application
    db = providers.Singleton(Database, config=configuration.provided.database)

    # Repositories
    user_repo = providers.Factory(UserRepository)

    # Services
    user_service = providers.Factory(UserService, db=db, user_repo=user_repo)
    auth_service = providers.Factory(AuthService, db=db, user_repo=user_repo, app_config=configuration.provided.app)

    # Background services
    internal = providers.Factory(Celery, main="internal", broker=configuration.provided.celery.internal.broker_url, backend=configuration.provided.celery.internal.backend_url)
    scheduler = providers.Factory(Celery, main="scheduler", broker=configuration.provided.celery.scheduler.broker_url, backend=configuration.provided.celery.scheduler.backend_url)
    critical = providers.Factory(Celery, main="critical", broker=configuration.provided.celery.critical.broker_url, backend=configuration.provided.celery.critical.backend_url)


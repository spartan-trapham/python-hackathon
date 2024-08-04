from dependency_injector import containers, providers

from src.configs.config import Configuration
from src.core.celery import CeleryApp
from src.database.db import Database
from src.database.repositories.user import UserRepository
from src.services.user import UserService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=[
            "..api",
            "..api.controllers",
        ]
    )

    # Application
    configuration = providers.Singleton(Configuration().get_config)
    db = providers.Singleton(Database, config=configuration.provided.database)
    celery = providers.Singleton(
        CeleryApp,
        config=configuration.provided.celery,
        queue_config=configuration.provided.sqs,
        db_config=configuration.provided.database,
    )

    # Repositories
    user_repo = providers.Factory(UserRepository, session=db.provided.session)

    # Services
    user_service = providers.Factory(UserService, db=db, user_repo=user_repo)

from dependency_injector import containers, providers

from src.configs.config import Configuration
from src.database.db import Database
from src.database.repositories.user import UserRepository
from src.services.user import UserService

from src.worker.brokers.internal import internal
from src.worker.brokers.critical import critical
from src.worker.brokers.scheduler import scheduler


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        packages=[
            "..api",
            "..api.controllers",
            "..configs",
        ]
    )
    # Configurations
    configuration = providers.Singleton(Configuration().get_config)

    # Application
    db = providers.Singleton(Database, config=configuration.provided.database)
    internal = internal
    critical = critical
    scheduler = scheduler

    # Repositories
    user_repo = providers.Factory(UserRepository, session=db.provided.session)

    # Services
    user_service = providers.Factory(UserService, db=db, user_repo=user_repo)

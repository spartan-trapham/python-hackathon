from contextlib import AbstractContextManager, contextmanager
from typing import Callable

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session, scoped_session

from ..configs.config import DatabaseConfig
from ..core import logging

Base = declarative_base()
logger = logging.setup_logger(__name__)


class Database:
    def __init__(self, config: DatabaseConfig) -> None:
        self.url = "postgresql+psycopg2://{username}:{password}@{host}:{port}/{name}".format_map(config.dict())
        self._engine = create_engine(self.url)

        self._session = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session()
        try:
            yield session
        except Exception:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise
        finally:
            session.close()

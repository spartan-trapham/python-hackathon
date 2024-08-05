from contextlib import AbstractContextManager, contextmanager
from typing import Callable

from sqlalchemy import create_engine, MetaData, Connection
from sqlalchemy.orm import sessionmaker, Session, scoped_session, DeclarativeBase

from src.configs.config import DatabaseConfig
from src.libs.log import logging

logger = logging.setup_logger(__name__)


class Base(DeclarativeBase):
    pass


class Database:
    def __init__(self, config: DatabaseConfig) -> None:
        self.url = "postgresql+psycopg2://{username}:{password}@{host}:{port}/{name}".format_map(config.dict())
        self._engine = create_engine(
            self.url,
            max_overflow=config.overflow_connections,
            pool_size=config.max_connections,
        )

        self._metadata = MetaData()
        self._metadata.bind = self._engine
        self._session = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )
        logger.info("Finish initialization database")

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        """Provide a transactional scope around a series of operations."""
        session = self._session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    @contextmanager
    def connect(self) -> Callable[..., AbstractContextManager[Connection]]:
        connection = self._engine.connect()
        try:
            yield connection
        except Exception:
            logger.exception("Connection rollback because of exception")
            connection.rollback()
            raise
        finally:
            connection.close()

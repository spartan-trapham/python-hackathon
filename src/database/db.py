from contextlib import AbstractContextManager, contextmanager
from typing import Callable

from sqlalchemy import create_engine, Metadata, Connection
from sqlalchemy.orm import sessionmaker, Session, scoped_session, DeclarativeBase

from src.configs.config import DatabaseConfig
from src.core import logging

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

        self._metadata = Metadata()
        self._metadata.bind = self._engine
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

    @contextmanager
    def connect(self) -> Callable[..., AbstractContextManager[Connection]]:
        with self._engine.connect() as connection:
            try:
                yield connection
            except Exception:
                logger.exception("Connection rollback because of exception")
                connection.rollback()
                raise
            finally:
                connection.close()

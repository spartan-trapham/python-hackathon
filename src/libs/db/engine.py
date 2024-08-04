from contextlib import AbstractContextManager, contextmanager
from typing import Callable

from sqlalchemy import create_engine, text, Engine, Connection, Metadata
from sqlalchemy.orm import sessionmaker, Session, scoped_session

class DB:
    def __init__(self, connection_string: str, max_overflow=10, pool_size=5):
        self._engine: Engine = create_engine(connection_string, max_overflow=max_overflow, pool_size=pool_size)
        self._metadata: Metadata = Metadata()
        self._metadata.bind = self._engine
        self._session = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
            ),
        )

    def get_metadata(self) -> Metadata:
        return self._metadata
    
    def get_session(self) -> Session:
        return self._session()

    @contextmanager
    def connect(self) -> Callable[..., AbstractContextManager[Connection]]:
        connection = self.engine.connect()
        try:
            yield connection
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    @contextmanager
    def session(self) -> Callable[..., AbstractContextManager[Session]]:
        session: Session = self._session()
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

if __name__ == "__main__":
    connection_string = 'postgresql+psycopg2://postgres:postgres@localhost:54321/python'
    dbConn = DB(connection_string)
    connection = dbConn.connect()
    result = connection.execute(text("SELECT version()"))
    for row in result:
        print(f"PostgreSQL version: {row[0]}")

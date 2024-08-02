from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session


class BaseRepository:
    _session = None

    def __init__(self, session: Callable[..., AbstractContextManager[Session]]) -> None:
        self._session = session

    @property
    def session(self):
        return self._session

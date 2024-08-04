from sqlalchemy import Column, VARCHAR, TIMESTAMP

from ._common import IDMixin, DateTimeMixin
from src.database.db import Base


class User(Base, IDMixin, DateTimeMixin):
    __tablename__ = 'users'

    name = Column(VARCHAR(128), nullable=True)
    email = Column(VARCHAR(64), nullable=False)
    password = Column(VARCHAR, nullable=False)

from sqlalchemy import Column, VARCHAR

from ._common import IDMixin, DateTimeMixin
from ...databases.db import Base


class User(Base, IDMixin, DateTimeMixin):
    __tablename__ = 'users'

    name = Column(VARCHAR(255), nullable=False)
    email = Column(VARCHAR(255), nullable=False)

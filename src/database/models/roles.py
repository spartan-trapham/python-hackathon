from sqlalchemy import Column, VARCHAR

from ._common import IDMixin, DateTimeMixin
from src.database.db import Base


class Role(Base, IDMixin, DateTimeMixin):
    __tablename__ = 'roles'

    name = Column(VARCHAR, nullable=False)
    description = Column(VARCHAR, nullable=True)


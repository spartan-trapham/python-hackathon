from sqlalchemy import Column, VARCHAR
from sqlalchemy.dialects.postgresql import JSONB

from src.database.db import Base
from ._common import IDMixin, DateTimeMixin


class Permission(Base, IDMixin, DateTimeMixin):
    __tablename__ = 'permissions'

    name = Column(VARCHAR(255), nullable=False)
    data = Column(JSONB, nullable=True)

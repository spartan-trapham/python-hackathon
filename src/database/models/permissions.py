from sqlalchemy import Column, VARCHAR
from sqlalchemy.dialects.postgresql import JSONB

from ._common import IDMixin, DateTimeMixin
from src.database.db import Base


class Permission(Base, IDMixin, DateTimeMixin):
    __tablename__ = 'permissions'

    name = Column(VARCHAR(255), nullable=False)
    metadata = Column(JSONB, nullable=True)

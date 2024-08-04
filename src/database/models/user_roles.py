from sqlalchemy import Column, ForeignKey

from ._common import IDMixin, DateTimeMixin
from src.database.db import Base


class UserRole(Base, IDMixin, DateTimeMixin):
    __tablename__ = 'user_roles'

    Column("user_id", ForeignKey("users.id"), nullable=False),
    Column("role_id", ForeignKey("roles.id"), nullable=True),

from sqlalchemy import Column, ForeignKey

from ._common import IDMixin, DateTimeMixin
from src.database.db import Base


class RolePermission(Base, IDMixin, DateTimeMixin):
    __tablename__ = 'users'

    Column("role_id", ForeignKey("roles.id"), nullable=False),
    Column("permission_id", ForeignKey("permissions.id"), nullable=True),

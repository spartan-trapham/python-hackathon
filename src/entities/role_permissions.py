from sqlalchemy import Table, Column, Integer, String, ForeignKey
from .base import BaseEntity
from src.libs.db.engine import DB

class RolePermission(BaseEntity):
  def __init__(self, db: DB):
    self.db = db
    self.table = Table(
      "role_permissions",
      db.metadata,
      Column("id", Integer, primary_key=True),
      Column("role_id", ForeignKey("roles.id"), nullable=False),
      Column("permission_id", ForeignKey("permissions.id"), nullable=True),
      Column("status", String),
    )
    BaseEntity.__init__(self, self.table)

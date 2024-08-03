from sqlalchemy import Table, Column, Integer, String, ForeignKey
from .base import BaseEntity
from src.libs.db.engine import DB

class UserRole(BaseEntity):
  def __init__(self, db: DB):
    self.db = db
    self.table = Table(
      "user_roles",
      db.metadata,
      Column("id", Integer, primary_key=True),
      Column("user_id", ForeignKey("users.id"), nullable=False),
      Column("role_id", ForeignKey("roles.id"), nullable=True),
      Column("status", String),
    )
    BaseEntity.__init__(self, self.table)

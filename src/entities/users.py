from sqlalchemy import Table, Column, Integer, String
from .base import BaseEntity
from src.libs.db.engine import DB

class User(BaseEntity):
  def __init__(self, db: DB):
    self.db = db
    self.table = Table(
      "users",
      db.metadata,
      Column("id", Integer, primary_key=True),
      Column("name", String(30)),
      Column("email", String),
    )
    BaseEntity.__init__(self, self.table)

from sqlalchemy import insert, select
from src.utils.batch_generator import batch_generator

class BaseEntity:
  def __init__(self, db, table):
    self.table = table
    self.db = db

  def get_many(self, filters, page, relations):
    query = select(self.table).where(filters).limit(page.limit).offset(page)
    if page.order_by:
      query = query.order_by(page.order_by)
  
  
  def get_one(self, filters, relations):
    query = self.table.select().where(self.table.c.id == id)
    return self.db.execute(query)
  
  def insert_many(self, payload, limit=10):
    with self.db.session() as session:
      for batch_data in batch_generator(payload, limit):
        session.scalars(
          insert(self.table).returning(self.table),
          batch_data,
        )


    query = self.table.insert().values(name=name, email=email)
    return self.db.execute(query)
  
  def insert_one(self, payload):
    query = self.table.insert().values(payload)
    return self.db.execute(query)
  
  def update(self, id, name, email):
    query = self.table.update().where(self.table.c.id == id).values(name=name, email=email)
    return self.db.execute(query)
  
  def delete(self, id):
    query = self.table.delete().where(self.table.c.id == id)
    return self.db.execute(query)
  
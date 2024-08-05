from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import Column, func, TIMESTAMP
from sqlalchemy.orm import declared_attr


class IDMixin:
    id = Column(UUID(as_uuid=True), primary_key=True, autoincrement=False, default=uuid.uuid4)


# pylint: disable=no-self-argument
class DateTimeMixin:
    @declared_attr
    def created_at(cls):
        return Column(TIMESTAMP(timezone=True), nullable=False, default=func.now())

    @declared_attr
    def updated_at(cls):
        return Column(TIMESTAMP(timezone=True), nullable=True, onupdate=func.now())

    @declared_attr
    def deleted_at(cls):
        return Column(TIMESTAMP(timezone=True), nullable=True, default=None)

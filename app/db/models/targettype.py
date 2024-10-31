from sqlalchemy import Column, Integer, String

from app.db.models import Base


class TargetType(Base):
    __tablename__ = 'targettype'
    target_type_id = Column(Integer, primary_key=True, autoincrement=True)
    target_type_name = Column(String)
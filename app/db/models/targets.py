from sqlalchemy import Integer, Column, String

from app.db.models import Base


class City(Base):
    __tablename__ = 'cities'
    target_id = Column(Integer, primary_key=True, autoincrement=True)
    mission_id = Column(Integer)
    target_industry = Column(String)
    city_id = Column(Integer)
    target_type_id = Column(Integer)
    target_priority = Column(String)
from sqlalchemy import Integer, Column, String

from app.db.models import Base


class City(Base):
    __tablename__ = 'cities'
    city_id = Column(Integer, primary_key=True, autoincrement=True)
    city_name = Column(String)
    country_id = Column(String)
    latitude = Column(String)
    longitude = Column(String)
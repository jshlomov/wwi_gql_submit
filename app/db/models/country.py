from sqlalchemy import Integer, Column, String

from app.db.models import Base


class City(Base):
    __tablename__ = 'cities'
    country_id = Column(Integer, primary_key=True, autoincrement=True)
    country_name = Column(String)
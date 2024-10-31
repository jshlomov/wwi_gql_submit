from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .targets import Target
from .mission import Mission
from .city import City
from .country import Country
from .targettype import TargetType

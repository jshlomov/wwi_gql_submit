from returns.maybe import Maybe

from app.db.database import session_maker
from app.db.models import Target, City, Country, TargetType
from app.db.models.mission import Mission

def find_mission_by_id(mission_id: int) -> Maybe[Mission]:
    with session_maker() as session:
        return Maybe.from_optional(session.get(Mission, mission_id))

def find_mission_between_dates(start, end):
    with session_maker() as session:
        return session.query(Mission).filter(Mission.mission_date.between(start,end)).all()

def find_missions_by_country(country):
    with session_maker() as session:
        return session.query(Mission).join(Target).join(City).join(Country).filter(Country.country_name == country).all()

def find_missions_by_industry(industry):
    with session_maker() as session:
        return (session.query(Mission)
                .join(Target)
                .filter(Target.target_industry == industry)
                .all())

def find_missions_by_target_type(target_type):
    with session_maker() as session:
        return (session.query(Mission)
                .join(Target)
                .join(TargetType)
                .filter(TargetType.target_type_name == target_type)
                .all())



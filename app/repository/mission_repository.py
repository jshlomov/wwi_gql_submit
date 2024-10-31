from flask import session
from returns.maybe import Maybe, Nothing
from returns.result import Result, Failure, Success
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

from app.db.database import session_maker
from app.db.models import Target, City, Country, TargetType
from app.db.models.mission import Mission


def find_mission_by_id(mission_id: int) -> Maybe[Mission]:
    with session_maker() as session:
        return session.get(Mission, mission_id)

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

def create_mission(mission: Mission):
    with session_maker() as session:
        session.add(mission)
        session.commit()
        session.refresh(mission)
        return mission

def get_mission_max_id():
    with session_maker() as session:
        return session.query(func.max(Mission.mission_id)).scalar() + 1


def update_mission_result(mission_id: int, updated_mission: Mission):
    with session_maker() as session:
        try:
            mission = session.query(Mission).get(mission_id)
            if mission is None:
                raise SQLAlchemyError("NOT FOUND")
            mission.aircraft_returned = updated_mission.aircraft_returned
            mission.aircraft_failed = updated_mission.aircraft_failed
            mission.aircraft_damaged = updated_mission.aircraft_damaged
            mission.aircraft_lost = updated_mission.aircraft_lost
            session.commit()
            session.refresh(mission)
            return mission
        except SQLAlchemyError as e:
            session.rollback()
            return str(e)

def delete_mission(mission_id: int):
    with session_maker() as session:
        try:
            mission = find_mission_by_id(mission_id)
            if mission is None:
                raise SQLAlchemyError("NOT FOUND")
            session.delete(mission)
            session.commit()
            return mission
        except SQLAlchemyError as e:
            session.rollback()
            return str(e)



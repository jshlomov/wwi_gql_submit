from returns.maybe import Nothing
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

from app.db.database import session_maker
from app.db.models import Mission, Target
from app.repository.mission_repository import find_mission_by_id


def create_mission(target: Target):
    with session_maker() as session:
        maybe_mission = find_mission_by_id(target.mission_id)
        if maybe_mission is not Nothing:
            raise SQLAlchemyError("mission id wasn't found")
        session.add(target)
        session.commit()
        session.refresh(target)
        return target

def get_next_target_id():
    with session_maker() as session:
        return session.query(func.max(Target.target_id)).scalar() + 1
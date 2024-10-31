from returns.maybe import Maybe

from app.db.database import session_maker
from app.db.models.mission import Mission


def find_mission_by_id(mission_id: int) -> Maybe[Mission]:
    with session_maker() as session:
        return Maybe.from_optional(session.get(Mission, mission_id))

def find_mission_between_dates(start, end):
    with session_maker() as session:
        return session.query(Mission).filter(start < Mission.mission_date < end).all()

from graphene import Mutation, String, Int, Field, Date, Float

from app.db.models import Mission
from app.gql.types.types import MissionType
import app.repository.mission_repository as mr

class AddMission(Mutation):
    class Arguments:
        mission_date = Date()
        airborne_aircraft = Float()
        attacking_aircraft = Float()
        bombing_aircraft = Float()
        aircraft_returned = Float()
        aircraft_failed = Float()
        aircraft_damaged = Float()
        aircraft_lost = Float()


    mission = Field(MissionType)

    @staticmethod
    def mutate(root, info, mission_date, airborne_aircraft,
               attacking_aircraft, bombing_aircraft, aircraft_returned,
               aircraft_failed, aircraft_damaged, aircraft_lost):
        mission = Mission(
            mission_id = mr.get_mission_max_id(),
            mission_date=mission_date,
            airborne_aircraft=airborne_aircraft,
            attacking_aircraft=attacking_aircraft,
            bombing_aircraft=bombing_aircraft,
            aircraft_returned=aircraft_returned,
            aircraft_failed=aircraft_failed,
            aircraft_damaged=aircraft_damaged,
            aircraft_lost=aircraft_lost
        )
        inserted_mission = mr.create_mission(mission)
        return AddMission(inserted_mission)
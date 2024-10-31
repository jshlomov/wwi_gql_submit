from graphene import Mutation, String, Int, Field, Date, Float
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
    def mutate(root, info, mission):
        return AddMission(mr.create_mission(mission))
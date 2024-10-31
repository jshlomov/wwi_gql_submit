from graphene import ObjectType, List, Int, Field, String, Date
from graphql import GraphQLError
from returns.maybe import Nothing

from app.db.database import session_maker
import app.repository.mission_repository as mr
from app.db.models.mission import Mission
from app.gql.types.types import MissionType


class Query(ObjectType):
    missions = List(MissionType)
    mission_by_id = Field(MissionType, mission_id=Int())
    missions_by_dates = List(MissionType, start=Date(), end=Date())
    missions_by_country = List(MissionType, country=String())
    missions_by_industry = List(MissionType, industry=String())
    missions_by_target_type = List(MissionType, target_type=String())

    @staticmethod
    def resolve_missions(root, info):
       with session_maker() as session:
           return session.query(Mission).all()

    @staticmethod
    def resolve_mission_by_id(root, info, mission_id):
       res = mr.find_mission_by_id(mission_id)
       return res

    @staticmethod
    def resolve_missions_by_dates(root, info, start, end):
           return mr.find_mission_between_dates(start, end)

    @staticmethod
    def resolve_missions_by_country(root, info, country):
        return mr.find_missions_by_country(country)

    @staticmethod
    def resolve_missions_by_industry(root, info, industry):
        return mr.find_missions_by_industry(industry)

    @staticmethod
    def resolve_missions_by_target_type(root, info, target_type):
        return mr.find_missions_by_target_type(target_type)



    # @staticmethod
    # def resolve_jobs(root, info):
    #    with session_maker() as session:
    #        return session.query(Job).all()
    #
    # @staticmethod
    # def resolve_employee(root, info, emp_id):
    #     res =  r.find_employee_by_id(emp_id)
    #     if res is not Nothing:
    #         return res.unwrap()
    #     else:
    #         raise GraphQLError("emp not found")
    #
    # @staticmethod
    # def resolve_empByIndustry(root, info, industry):
    #     return r.find_employees_by_industry(industry)


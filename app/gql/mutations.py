from graphene import ObjectType

from app.gql.mutation.mission_mutations import AddMission
from app.gql.mutation.target_mutations import AddTarget


class Mutation(ObjectType):
    add_mission = AddMission.Field()
    add_target = AddTarget.Field()
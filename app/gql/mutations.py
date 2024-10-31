from graphene import ObjectType

from app.gql.mutation.mission_mutations import AddMission


class Mutation(ObjectType):
    add_mission = AddMission.Field()
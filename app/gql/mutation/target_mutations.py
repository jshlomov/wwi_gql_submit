from graphene import Mutation, String, Int, Field, Date, Float

from app.db.models import Mission, Target
from app.gql.types.types import MissionType, TargetType
import app.repository.mission_repository as mr

import app.repository.target_repository as tr


class AddTarget(Mutation):
    class Arguments:
        mission_id = Int()
        target_industry = String()
        city_id = Int()
        target_type_id = Int()
        target_priority = String()


    target = Field(TargetType)

    @staticmethod
    def mutate(root, info, mission_id, target_industry, city_id, target_type_id, target_priority):
        target = Target(
            target_id= tr.get_next_target_id(),
            mission_id=mission_id,
            target_industry=target_industry,
            city_id=city_id,
            target_type_id=target_type_id,
            target_priority=target_priority
        )
        inserted_target = mr.create_mission(target)
        return AddTarget(inserted_target)
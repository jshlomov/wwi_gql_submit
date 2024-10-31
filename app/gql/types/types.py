
from graphene import ObjectType, Int, Field, Date, Float, String, List


class TargetType(ObjectType):
   target_id = Int()
   mission_id = String()
   target_industry = String()
   city_id = String()
   target_type_id = Int()
   target_priority = Int()

   mission = Field(lambda: MissionType)
   city = Field(lambda: CityType)
   target_type = Field(lambda: CityType)

class MissionType(ObjectType):
    mission_id = Int()
    mission_date = Date()
    airborne_aircraft = Float()
    attacking_aircraft = Float()
    bombing_aircraft  = Float()
    aircraft_returned  = Float()
    aircraft_failed  = Float()
    aircraft_damaged  = Float()
    aircraft_lost  = Float()
    target = List(lambda: TargetType)

class CountryType(ObjectType):
    country_id = Int()
    country_name = String()
    cities = List(lambda: CityType)

class CityType(ObjectType):
    city_id = Int()
    city_name = String()
    country_id = String()
    latitude = String()
    longitude = String()

    country = Field(lambda: CountryType)
    targets = List(lambda: TargetType)

class TargetTypeType(ObjectType):
    target_type_id = Int()
    target_type_name = String()

    targets = List(TargetType)

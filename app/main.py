from flask import Flask
from app.db.database import init_db
from flask_graphql import GraphQLView
from graphene import Schema

from app.db.models import Mission
from app.gql.mutations import Mutation
from app.gql.query import Query
from app.repository.mission_repository import create_mission, get_mission_max_id, update_mission_result

schema = Schema(query=Query, mutation=Mutation)

app = Flask(__name__)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

if __name__ == '__main__':
    app.run()
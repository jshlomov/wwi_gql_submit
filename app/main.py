from flask import Flask
from app.db.database import init_db
from flask_graphql import GraphQLView
from graphene import Schema

from app.gql.query import Query
from app.repository.mission_repository import find_mission_by_id, find_missions_by_country

schema = Schema(query=Query)

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
    # res = find_missions_by_country("GERMANY").unwrap()
    app.run()
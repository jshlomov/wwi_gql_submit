from flask import Flask
from app.db.database import init_db
from flask_graphql import GraphQLView
from graphene import Schema

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
    init_db()
    app.run()
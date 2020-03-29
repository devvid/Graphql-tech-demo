import graphene
from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_graphql import GraphQLView

"""
Extensions
"""
db = SQLAlchemy()
migrate = Migrate()

from src.schema import Query, Mutation

"""
Application
"""
def create_app():
    app = Flask(__name__)

    # load the instance config, if it exists, when not testing
    app.config.from_object('src.config.BaseConfiguration')

    db.init_app(app)
    migrate.init_app(app, db)
    
    # noinspection PyTypeChecker
    schema_query = graphene.Schema(query=Query)

    # noinspection PyTypeChecker
    schema_mutation = graphene.Schema(query=Query, mutation=Mutation)

    # /graphql-query
    app.add_url_rule('/graphql-query', view_func=GraphQLView.as_view(
        'graphql-query',
        schema=schema_query, graphiql=True
    ))

    # /graphql-mutation
    app.add_url_rule('/graphql-mutation', view_func=GraphQLView.as_view(
        'graphql-mutation',
        schema=schema_mutation, graphiql=True
    ))

    @app.route('/')
    def hello_world():
        return 'Hello!'

    return app

from src.models import User, Post
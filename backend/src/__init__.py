import graphene
from flask import Flask, request, jsonify
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_graphql import GraphQLView
from flask_cors import CORS


"""
Extensions
"""
db = SQLAlchemy()
migrate = Migrate()

from src.schema import Query, Mutation
from src.models import User, Post, ViewHistory

"""
Application
"""
def create_app():
    app = Flask(__name__)

    # load the instance config, if it exists, when not testing
    app.config.from_object('src.config.BaseConfiguration')

    db.init_app(app)
    migrate.init_app(app, db)
    cors = CORS(app, resources={r"*": {"origins": app.config['CORS']}})
    
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

    @app.route('/api/post/all')
    def all_posts():
        posts = Post.query.join('author').all()
        
        _posts = {
            'allPosts': {
                'edges': []
            }
        }
        for p in posts:
            print(p)
            _posts['allPosts']['edges'].append(dict(node={
                'id': p.id,
                'title': p.title,
                'body': p.body,
                'author': {
                    'id': p.author.id,
                    'name': p.author.name,
                    'email': p.author.email
                }
            }))
        return jsonify(_posts)

    @app.route('/api/post/<post_id>')
    def detail_post(post_id):
        post = Post.query.filter_by(id=post_id).first()
        if post == None:
            return jsonify({'error': 'No post for the id: {}'.format(post_id)})
        _post = {
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'author': {
                'id': post.author.id,
                'name': post.author.name,
            },
            'history': {
                'edges': []
            }
        }
        for hist in post.history:
            _post['history']['edges'].append(dict(node={
                'id': hist.id,
                'ipAddress': hist.ip_address
            }))
        return jsonify({'post': _post})

    return app
# flask_sqlalchemy/models.py
from sqlalchemy import *
from src import db
from datetime import datetime 
import json

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    email = db.Column(db.String(256), index=True, unique=True)
    posts = db.relationship('Post', backref='author')

    def __repr__(self):
        return '<User %r>' % self.email


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    history = db.relationship('ViewHistory', backref='post')

    def __repr__(self):
        return '<Post %r>' % self.title


class ViewHistory(db.Model):
    __tablename__ = 'view_history'
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(32))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def __repr__(self):
        return '<View History %r>' % self.ip_address
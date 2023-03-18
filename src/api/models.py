from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    #comments = db.relationship('Comment', backref='user', passive_deletes=True)
    #posts = db.relationship('Post', backref='user', passive_deletes=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }

    
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default= datetime.now)
    #author = db.Column(db.Integer,db.ForeignKey('post.id'), nullable=False)

    def __repr__(self):
        return f'<Comment {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "text": self.text,
            "date_created": self.date_created,
            "author": self.author
        }

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default= datetime.now)
    # author = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Review {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "text": self.text,
            "date_created": self.date_created,
            "author": self.author
            # do not serialize the password, its a security breach
        }
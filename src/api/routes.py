"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Comment
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
import os


api = Blueprint('api', __name__)


@api.route('/login', methods=['POST'])
def login():
    data = request.json
    #return jsonify(list(data.keys()))
    user = User.query.filter_by(username=data.get("username", None)).first()
    email = User.query.filter_by(email=data.get("email", None)).first()
    if user: 
        if user.password == data.get("password",None):
            return jsonify(token=create_access_token(data.get("username", None)))
    if email: 
        if email.password == data.get("password",None):
            return jsonify(token=create_access_token(data.get("email", None)))
    return jsonify(message="invalid login"), 401

@api.route('/secure', methods=['GET'])
@jwt_required()
def test():
    return jsonify(message="Success!!",username=get_jwt_identity())

@api.route('/signup', methods=['POST'])
def handel_signup():
    response_body = request.get_json()
    user_name = User.query.filter_by(username=response_body.get("username", None)).first()
    user_email = User.query.filter_by(email=response_body.get("email", None)).first()
    if  not user_name and not user_email:
        user = User(
            email=response_body["email"],
            username=response_body["username"],
            password=response_body["password"],
            is_active=True
        )
        db.session.add(user) 
        db.session.commit()
        return jsonify(message="Signed up"), 200
    
    return jsonify(message="User Already Exist"), 400


@api.route('/comment', methods=['POST'])
@jwt_required()
def create_comment():
    response_body = request.get_json()
    comment = Comment(
        text= response_body["text"],
        date_created=response_body["date_created"]
    )
    db.session.add(comment)
    db.session.commit()

    payload = {
        'msg': 'Comment Made!'
    }

    return jsonify(payload), 200

    
@api.route('/review', methods=['POST'])
def review():
    response_body = request.get_json()
    profile = Review(
    first_name=response_body["first_name"],
    last_name=response_body["last_name"]
    )
    db.session.add(review)
    db.session.commit()

    payload = {
        'msg': 'Review Made!'
    }
    return jsonify(payload), 200
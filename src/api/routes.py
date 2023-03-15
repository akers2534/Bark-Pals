"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
import os


api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/login', methods=['POST'])
def login():
    data = request.json
    #return jsonify(list(data.keys()))
    user = User.query.filter_by(username=data.get("username", None)).first()
    if user: 
        if user.password == data.get("password",None):
            return jsonify(token=create_access_token(data.get("username", None)))
    return jsonify(message="invalid login"), 401

@api.route('/secure', methods=['GET'])
@jwt_required()
def test():
    return jsonify(message="hello world",username=get_jwt_identity())
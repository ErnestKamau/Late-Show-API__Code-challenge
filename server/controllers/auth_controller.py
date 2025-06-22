from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from datetime import timedelta

from models.user import User
from config import db


class Register(Resource):
    def post(self):
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return make_response({"error": "Username and password required"}, 400)

        
        if User.query.filter_by(username=username).first():
            return make_response({"error": "Username already exists"}, 409)

        
        new_user = User(username=username)
        new_user.password_hash = password  

        db.session.add(new_user)
        db.session.commit()

        return make_response({"message": "User registered successfully"}, 201)


class Login(Resource):
    def post(self):
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return make_response({"error": "Username and password required"}, 400)

        user = User.query.filter_by(username=username).first()

        if user and user.authenticate(password):
            access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=24))
            return make_response({"token": access_token}, 200)

        return make_response({"error": "Invalid username or password"}, 401)



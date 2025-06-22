#!/usr/bin/env python3

from flask import make_response, jsonify, request, session
from flask_restful import Resource
from config import app, db, api
from models import User, Guest, Episode, Appearance
from controllers.auth_controller import Register, Login
from controllers.guest_controller import GuestList
from controllers.appearance_controller import CreateAppearance
from controllers.episode_controller import Episodes, EpisodeByID

class Home(Resource):
    def get(self):
        return make_response({"message": "Welcome to the Late Show API"}, 200)


api.add_resource(Home, '/', endpoint='home')
api.add_resource(Register, '/register', endpoint='register')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(GuestList, '/guests', endpoint='guest_list')
api.add_resource(CreateAppearance, '/appearances', endpoint='create_appearance')
api.add_resource(Episodes, '/episodes', endpoint='episodes')
api.add_resource(EpisodeByID, '/episodes/<int:id>', endpoint='episode_by_id')


if __name__ == '__main__':
    app.run(port=5555, debug=True)

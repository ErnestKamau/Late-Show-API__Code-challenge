#!/usr/bin/env python3

from flask import make_response, jsonify, request, session
from flask_restful import Resource
from config import app, db, api


class Home(Resource):
    def get(self):
        return make_response({"message": "Welcome to the Late Show API"}, 200)


api.add_resource(Home, '/', endpoint='home')


if __name__ == '__main__':
    app.run(port=5555, debug=True)

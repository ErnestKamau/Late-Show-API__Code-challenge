from flask_restful import Resource
from flask import make_response
from models import Guest
from config import db


class GuestList(Resource):
    def get(self):
        guests = Guest.query.all()
        guest_data = [guest.to_dict() for guest in guests]

        return make_response(guest_data, 200)

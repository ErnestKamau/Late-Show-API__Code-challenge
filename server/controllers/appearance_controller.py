from flask import request, make_response
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity

from models import Guest, Episode, Appearance
from config import db


class CreateAppearance(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()

        rating = data.get("rating")
        guest_id = data.get("guest_id")
        episode_id = data.get("episode_id")

        if not all([rating, guest_id, episode_id]):
            return make_response({"error": "All fields required"}, 400)

        if int(rating) < 1 or int(rating) > 5:
            return make_response({"error": "Rating must be 1 to 5"}, 400)

        guest = Guest.query.get(guest_id)
        episode = Episode.query.get(episode_id)

        if not guest or not episode:
            return make_response({"error": "Invalid guest or episode ID"}, 404)

        new_appearance = Appearance(rating=rating, guest_id=guest_id, episode_id=episode_id)
        db.session.add(new_appearance)
        db.session.commit()

        return make_response(new_appearance.to_dict(), 201)

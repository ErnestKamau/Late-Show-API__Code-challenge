from flask import request, make_response, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from config import api, db
from models.episode import Episode
from models.appearance import Appearance

class Episodes(Resource):
    def get(self):
        episodes = Episode.query.all()
        response = [ep.to_dict() for ep in episodes]
        return make_response(jsonify(response), 200)

class EpisodeByID(Resource):
    def get(self, id):
        episode = Episode.query.filter_by(id=id).first()

        if not episode:
            return make_response(jsonify({"error": "Episode not found"}), 404)

        episode_dict = episode.to_dict()
        episode_dict["appearances"] = [appearance.to_dict() for appearance in episode.appearances]

        return make_response(jsonify(episode_dict), 200)

    @jwt_required()
    def delete(self, id):
        episode = Episode.query.filter_by(id=id).first()

        if not episode:
            return make_response(jsonify({"error": "Episode not found"}), 404)

        db.session.delete(episode)
        db.session.commit()

        return make_response(jsonify({"message": f"Episode {id} deleted successfully."}), 200)

from flask import request, jsonify
from flask_jwt_extended import create_access_token
from models.user import User
from config import app, db


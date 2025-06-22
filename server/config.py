import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv


load_dotenv()


app = Flask(__name__)


db_password = os.environ.get("DB_PASSWORD")
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://ernest:{db_password}@localhost:5432/late_show_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY", "super-secret-key")


db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

bcrypt = Bcrypt(app)

api = Api(app)

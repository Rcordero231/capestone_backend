
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)

CORS(app=app)
JWTManager(app=app)
app.config.from_object(Config)


db = SQLAlchemy(app)
migrate = Migrate(app,db)

from . import routes, models
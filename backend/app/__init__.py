from flask import Flask
from flask_pymongo import PyMongo
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mongo = PyMongo(app)

from app.routes.user_routes import user_bp
from app.routes.task_routes import task_bp

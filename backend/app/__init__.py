from flask import Flask
from flask_pymongo import PyMongo
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
mongo = PyMongo(app)

#import blueprints
from app.routes.user_routes import user_bp
from app.routes.task_routes import task_bp
from app.routes.tag_routes import tag_bp

#register blueprints
app.register_blueprint(user_bp)
app.register_blueprint(task_bp)
app.register_blueprint(tag_bp)

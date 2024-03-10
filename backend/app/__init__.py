from flask import Flask
from flask_pymongo import PyMongo
from config import Config
from flask_login import LoginManager
from app.models.user import User
from bson.objectid import ObjectId



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

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        return None
    return User(user['username'], user['email'], user['password_hash'], user['_id'])


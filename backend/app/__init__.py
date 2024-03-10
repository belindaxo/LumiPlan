from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt  # Add this import
from flask_login import LoginManager
from config import DevelopmentConfig, TestingConfig, ProductionConfig, Config
import os

bcrypt = Bcrypt()
mongo = PyMongo()

def create_app():
    app = Flask(__name__)

    # Initialize bcrypt and mongo with the app
    bcrypt.init_app(app)
    mongo.init_app(app)

    # Configuration setup based on environment
    env = os.getenv('FLASK_ENV', 'development')
    if env == 'development':
        app.config.from_object(DevelopmentConfig)
    elif env == 'testing':
        app.config.from_object(TestingConfig)
    elif env == 'production':
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(Config)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if not user:
            return None
        return User(user['username'], user['email'], user['password_hash'], user['_id'])

    # Blueprint registration
    from app.routes.user_routes import user_bp
    from app.routes.task_routes import task_bp
    from app.routes.tag_routes import tag_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(tag_bp)

    return app

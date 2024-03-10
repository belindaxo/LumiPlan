from flask import Blueprint, request, jsonify
from app.models.user import User
from flask_login import login_user

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/users', methods=['POST'])
def register_user():
    # Extract user info from request
    data = request.get_json()
    user = User.create_user(data['username'], data['email'], data['password_hash'])
    if user:
        return jsonify({"message": "User created successfully"}), 201
    else:
        return jsonify({"message": "Error creating user"}), 400
    

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')  # Ensure the frontend sends 'password', not 'password_hash'

    user = User.get_user_by_username(username)
    if user and User.check_password(user.password_hash, password):
        # Here, you would typically set up the user session or token
        # For simplicity, we'll just return a success response
        login_user(user)  # This logs in the user with Flask-Login
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401
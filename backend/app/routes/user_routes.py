from flask import Blueprint, request, jsonify
from app.models.user import User

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
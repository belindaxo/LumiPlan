from flask import Blueprint, request, jsonify
from app.models.user import create_user

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['POST'])
def register_user():
    # Extract user info from request
    data = request.get_json()
    create_user(data['username'], data['email'], data['password_hash'])
    return jsonify({"message": "User created successfully"}), 201

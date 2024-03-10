from flask import Blueprint, request, jsonify
from app.models.user import User
from flask_login import login_user

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    print(data)  # Add this line to debug

    if not data or 'username' not in data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Missing username, email, or password"}), 400
    # Extract user info from request
    # Use 'password' key instead of 'password_hash'
    user = User.create_user(data['username'], data['email'], data['password'])  # Change here
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
        return jsonify({"message": "Login successful", "user" : user.to_json()}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401
    
@user_bp.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    user_id = data.get('user_id')
    task = data.get('task')

    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        return jsonify({"error": "User not found"}), 404

    try:
        mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$push": {"tasks": task}})
        return jsonify({"message": "Task added successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

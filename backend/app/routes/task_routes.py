from flask import Blueprint, request, jsonify
from app import mongo
from app.models.task import create_task, get_tasks
from bson.objectid import ObjectId
from app.models.user import User

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/tasks', methods=['POST'])
def add_task():

    data = request.get_json()
    task = create_task(data['user_id'], data['course'], data['title'], data['desc'], data['due_date'], data['status'], data['priority'], data['est_time'])
    return jsonify(task), 201

@task_bp.route('/tasks/<user_id>', methods=['GET'])
def list_tasks(user_id):
    tasks = get_tasks(user_id)
    return jsonify(tasks), 200

@task_bp.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    result = mongo.db.tasks.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": data}
    )
    if result.modified_count:
        return jsonify({"message": "Task updated successfully"}), 200
    else:
        return jsonify({"message": "Task not found"}), 404

@task_bp.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    result = mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count:
        return jsonify({"message": "Task deleted successfully"}), 200
    else:
        return jsonify({"message": "Task not found"}), 404

@task_bp.route('/tasks/single/<task_id>', methods=['GET'])
def get_task(task_id):
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    if task:
        return jsonify(task), 200
    else:
        return jsonify({"message": "Task not found"}), 404
    
@task_bp.route('/addTaskWithUserUpdate', methods=['POST'])
def add_task_with_user_update():
    data = request.get_json()
    user_id = data.pop('user_id')  # Adjust based on how you're identifying users
    task = create_task(**data)
    user = User.get_user_by_username(user_id)  # or User.get_user_by_id(user_id) as applicable
    if user and task:
        user.add_task(task['_id'])  # Assuming you're storing task ID references in the user document
        return jsonify(task), 201
    else:
        return jsonify({"message": "Error creating task or finding user"}), 400


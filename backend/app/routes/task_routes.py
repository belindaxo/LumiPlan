from flask import Blueprint, request, jsonify
from app.models.task import create_task, get_tasks

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


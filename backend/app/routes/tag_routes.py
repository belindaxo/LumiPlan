from flask import Blueprint, request, jsonify
from app.models.tag import create_tag, get_tags, delete_tag
from app import mongo

tag_bp = Blueprint('tag_bp', __name__)

@tag_bp.route('/tags', methods=['POST'])
def add_tag():
    data = request.get_json()
    tag = create_tag(data['user_id'], data['name'])
    return jsonify(tag), 201

@tag_bp.route('/tags/<user_id>', methods=['GET'])
def list_tags(user_id):
    tags = get_tags(user_id)
    return jsonify([tags]), 200

@tag_bp.route('/tags/<tag_id>', methods=['DELETE'])
def remove_tag(tag_id):
    if delete_tag(tag_id):
        return jsonify({"message": "Tag deleted successfully"}), 200
    else:
        return jsonify({"message": "Tag not found"}), 404

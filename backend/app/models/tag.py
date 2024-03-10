from bson import ObjectId
from bson.errors import InvalidId
from app import mongo

def create_tag(user_id, name):
    # Attempt to validate and convert user_id to ObjectId
    try:
        valid_user_id = ObjectId(user_id)
    except InvalidId:
        # Handle invalid user_id here. For example:
        raise ValueError("Invalid user_id provided.")
    
    tag = {
        "user_id": valid_user_id,
        "name": name,
    }
    mongo.db.tags.insert_one(tag)
    return tag



def get_tags(user_id):
    tags = mongo.db.tags.find({"user_id": ObjectId(user_id)})  # Convert user_id to ObjectId for querying
    return list(tags)


def delete_tag(tag_id):
    result = mongo.db.tags.delete_one({"_id": ObjectId(tag_id)})
    return result.deleted_count > 0


def is_valid_object_id(id):
    try:
        ObjectId(id)
        return True
    except (InvalidId, TypeError):
        return False

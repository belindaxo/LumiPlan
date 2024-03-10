from app import mongo
from bson.objectid import ObjectId

def create_tag(user_id, name):
    tag = {
        "user_id": user_id,
        "name": name,
    }
    mongo.db.tags.insert_one(tag)
    return tag

def get_tags(user_id):
    tags = mongo.db.tags.find({"user_id": ObjectId(user_id)})
    return list(tags)

def delete_tag(tag_id):
    result = mongo.db.tags.delete_one({"_id": ObjectId(tag_id)})
    return result.deleted_count > 0
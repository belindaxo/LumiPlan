from app import mongo
from bson.objectid import ObjectId


def create_task(user_id, course, title, desc, due_date, status, priority, est_time):
    task = {
        "user_id": user_id,
        "course": course,
        "title": title,
        "desc": desc,
        "due_date": due_date,
        "status": status,
        "priority": priority,
        "est_time": est_time,
    }
    mongo.db.tasks.insert_one(task)
    return task

# Adjust get_tasks to query with a string if that's how it's stored
def get_tasks(user_id):
    tasks = mongo.db.tasks.find({"user_id": user_id})  # Use string directly if stored as a string
    return list(tasks)

def update_task(task_id, **updates):
    result = mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": updates})
    return result.modified_count > 0


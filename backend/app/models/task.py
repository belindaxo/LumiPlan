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

def get_tasks(user_id):
    tasks = mongo.db.tasks.find({"user_id": ObjectId(user_id)})
    return list(tasks)

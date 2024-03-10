import pytest
from mongomock import MongoClient
from bson.objectid import ObjectId
from app import mongo
from app.models.task import create_task, get_tasks, update_task

# Fixture to mock MongoDB
@pytest.fixture
def mock_db(monkeypatch):
    # Mock the MongoClient to use an in-memory database
    client = MongoClient()
    db = client['test_database']
    # Patch the mongo.db with our mock
    monkeypatch.setattr(mongo, 'db', db)
    return db

def test_create_task(mock_db):
    user_id = "5f77c6cf24e1fbd741556214"
    task = create_task(user_id, "Math", "Homework 1", "Chapter 1 Exercises", "2023-03-15", "pending", "high", 2)
    assert task['user_id'] == user_id
    assert task['course'] == "Math"
    assert task['title'] == "Homework 1"
    assert '_id' in task
    # Verify that the task is actually inserted into the mock database
    assert mock_db.tasks.find_one({"_id": task['_id']}) is not None

def test_get_tasks(mock_db):
    user_id = "5f77c6cf24e1fbd741556214"
    create_task(user_id, "Math", "Homework 1", "Chapter 1 Exercises", "2023-03-15", "pending", "high", 2)
    create_task(user_id, "Science", "Lab Report", "Gravity Experiment", "2023-03-20", "in progress", "medium", 3)
    tasks = get_tasks(user_id)
    assert len(tasks) == 2
    # Additional checks can be made here to verify the integrity of the data returned


def test_create_task_with_minimal_data(mock_db):
    user_id = "5f77c6cf24e1fbd741556214"
    # Assuming your application logic allows tasks with minimal data
    task = create_task(user_id, "", "", "", None, "", "", None)
    assert task['user_id'] == user_id
    assert '_id' in task
    # Verify it's stored
    assert mock_db.tasks.find_one({"_id": task['_id']}) is not None

def test_get_tasks_no_tasks(mock_db):
    user_id = "5f77c6cf24e1fbd741556214"
    tasks = get_tasks(user_id)
    assert len(tasks) == 0  # Expect no tasks for a new user_id

# Example of a new test function if updates/deletions are part of your module
def test_update_task(mock_db):
    # You would need an update_task function for this test
    pass

def test_delete_task(mock_db):
    # You would need a delete_task function for this test
    pass


def test_update_task_success(mock_db):
    user_id = "5f77c6cf24e1fbd741556214"
    task_id = create_task(user_id, "Math", "Homework 1", "Chapter 1 Exercises", "2023-03-15", "pending", "high", 2)['_id']
    updated = update_task(task_id, status="completed")
    assert updated is True
    updated_task = mock_db.tasks.find_one({"_id": task_id})
    assert updated_task['status'] == "completed"

def test_update_task_nonexistent(mock_db):
    task_id = ObjectId("507f1f77bcf86cd799439011")  # Assuming this ID does not exist in your test DB
    updated = update_task(task_id, status="completed")
    assert updated is False  # Assuming your update function returns False when the task doesn't exist

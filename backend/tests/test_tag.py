import pytest
from mongomock import MongoClient
from app import mongo
from app.models.tag import create_tag, get_tags, delete_tag, is_valid_object_id


import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, module="pkg_resources")

# Fixture to mock MongoDB
@pytest.fixture
def mock_db(monkeypatch):
    client = MongoClient()
    db = client['test_database']
    monkeypatch.setattr(mongo, 'db', db)
    return db

def test_create_tag(mock_db):
    user_id = "5f77c6cf24e1fbd741556214"
    name = "test_tag"
    tag = create_tag(user_id, name)
    assert str(tag['user_id']) == user_id  # Convert ObjectId to string for comparison
    assert tag['name'] == name
    assert '_id' in tag
    assert mock_db.tags.find_one({"_id": tag['_id']}) is not None


def test_get_tags(mock_db):
    user_id = "5f77c6cf24e1fbd741556214"
    create_tag(user_id, "test_tag_1")
    create_tag(user_id, "test_tag_2")
    tags = get_tags(user_id)
    assert len(tags) == 2
    assert tags[0]['name'] == "test_tag_1"
    assert tags[1]['name'] == "test_tag_2"

def test_delete_tag(mock_db):
    user_id = "5f77c6cf24e1fbd741556214"
    tag = create_tag(user_id, "test_tag")
    assert delete_tag(str(tag['_id']))
    assert mock_db.tags.find_one({"_id": tag['_id']}) is None

def test_create_tag_with_invalid_data(mock_db):
    user_id = ""  # Invalid ObjectId string
    name = "test_tag"
    with pytest.raises(ValueError):
        create_tag(user_id, name)


def test_get_tags_nonexistent_user(mock_db):
    user_id = "507f1f77bcf86cd799439011"  # This time, use a valid hex string but nonexistent ID
    tags = get_tags(user_id)
    assert len(tags) == 0  # Expect no tags for a nonexistent user


def test_delete_nonexistent_tag(mock_db):
    non_existent_tag_id = "507f1f77bcf86cd799439011"  # Assuming this ID does not exist
    result = delete_tag(non_existent_tag_id)
    assert not result  # Expect the result to be False or similar, indicating deletion was unsuccessful

def test_delete_tag_idempotency(mock_db):
    user_id = "5f77c6cf24e1fbd741556214"
    tag = create_tag(user_id, "temp_tag")
    # First deletion attempt
    assert delete_tag(str(tag['_id']))
    # Second deletion attempt, expecting the tag to no longer exist
    assert not delete_tag(str(tag['_id']))





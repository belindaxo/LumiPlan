import pytest
from app.models.user import User
from bson.objectid import ObjectId
from unittest.mock import patch

# Since bcrypt and mongo are imported within the methods, we'll need to mock these
# to ensure our tests are isolated and do not require the actual database or bcrypt setup.

# Test User.__init__
@pytest.mark.parametrize("username, email, password_hash, _id, expected_id", [
    ("testuser", "test@example.com", "hash123", None, ObjectId),  # ID-01: No ID provided, expect ObjectId to be created
    ("testuser", "test@example.com", "hash123", "customid", "customid"),  # ID-02: Custom ID provided, expect the same ID
])
def test_user_init(username, email, password_hash, _id, expected_id):
    # Arrange
    if _id is None:
        user = User(username, email, password_hash)
    else:
        user = User(username, email, password_hash, _id)

    # Act
    # No action needed as we are testing __init__

    # Assert
    assert user.username == username
    assert user.email == email
    assert user.password_hash == password_hash
    assert isinstance(user._id, expected_id) if _id is None else user._id == expected_id

# Test User.set_password
@pytest.mark.parametrize("password, mock_bcrypt_return_value", [
    ("password123", b"hashedpassword123"),  # ID-03: Simple password
    ("", b"hashedempty"),  # ID-04: Empty password
])
def test_set_password(password, mock_bcrypt_return_value):
    with patch('app.models.user.bcrypt') as mock_bcrypt:
        # Arrange
        mock_bcrypt.generate_password_hash.return_value = mock_bcrypt_return_value

        # Act
        hashed_password = User.set_password(password)

        # Assert
        mock_bcrypt.generate_password_hash.assert_called_once_with(password)
        assert hashed_password == mock_bcrypt_return_value.decode('utf-8')

# Test User.check_password
@pytest.mark.parametrize("password_hash, password, mock_bcrypt_return_value", [
    ("hashedpassword123", "password123", True),  # ID-05: Correct password
    ("hashedpassword123", "wrongpassword", False),  # ID-06: Incorrect password
])
def test_check_password(password_hash, password, mock_bcrypt_return_value):
    with patch('app.models.user.bcrypt') as mock_bcrypt:
        # Arrange
        mock_bcrypt.check_password_hash.return_value = mock_bcrypt_return_value

        # Act
        result = User.check_password(password_hash, password)

        # Assert
        mock_bcrypt.check_password_hash.assert_called_once_with(password_hash, password)
        assert result == mock_bcrypt_return_value

# Test User.create_user
@pytest.mark.parametrize("username, email, password, mock_bcrypt_return_value, mock_insert_one_result", [
    ("newuser", "new@example.com", "newpassword", b"newhashed", {"inserted_id": ObjectId()}),  # ID-07: New user creation
])
def test_create_user(username, email, password, mock_bcrypt_return_value, mock_insert_one_result):
    with patch('app.models.user.bcrypt') as mock_bcrypt, patch('app.models.user.mongo') as mock_mongo:
        # Arrange
        mock_bcrypt.generate_password_hash.return_value = mock_bcrypt_return_value
        mock_mongo.db.users.insert_one.return_value = mock_insert_one_result

        # Act
        user = User.create_user(username, email, password)

        # Assert
        mock_bcrypt.generate_password_hash.assert_called_once_with(password)
        mock_mongo.db.users.insert_one.assert_called_once()
        assert user.username == username
        assert user.email == email
        assert user.password_hash == mock_bcrypt_return_value.decode('utf-8')

# Test User.to_json
@pytest.mark.parametrize("username, email, password_hash, _id", [
    ("userjson", "json@example.com", "hashjson", ObjectId()),  # ID-08: Convert user to JSON
])
def test_to_json(username, email, password_hash, _id):
    # Arrange
    user = User(username, email, password_hash, _id)

    # Act
    user_json = user.to_json()

    # Assert
    assert user_json == {
        "_id": _id,
        "username": username,
        "email": email,
        "password_hash": password_hash
    }

# Test User.get_user_by_username
@pytest.mark.parametrize("username, mock_find_one_result, expected_result", [
    ("existinguser", {"username": "existinguser", "email": "exist@example.com", "password_hash": "existhash", "_id": ObjectId()}, True),  # ID-09: User exists
    ("nonexistinguser", None, False),  # ID-10: User does not exist
])
def test_get_user_by_username(username, mock_find_one_result, expected_result):
    with patch('app.models.user.mongo') as mock_mongo:
        # Arrange
        mock_mongo.db.users.find_one.return_value = mock_find_one_result

        # Act
        user = User.get_user_by_username(username)

        # Assert
        mock_mongo.db.users.find_one.assert_called_once_with({"username": username})
        assert (user is not None) == expected_result

from flask_login import UserMixin
from bson.objectid import ObjectId
from app import bcrypt, mongo  # Ensure these are correctly initialized elsewhere in your application

class User(UserMixin):
    def __init__(self, username, email, password_hash=None, _id=None):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self._id = _id or ObjectId()

    @staticmethod
    def set_password(password):
        # Guard clause for empty password
        if not password:
            raise ValueError("Password must be non-empty.")
        return bcrypt.generate_password_hash(password).decode('utf-8')

    @staticmethod
    def check_password(password_hash, password):
        return bcrypt.check_password_hash(password_hash, password)

    @staticmethod
    def create_user(username, email, password):
        # This method is clearly within the User class context
        password_hash = User.set_password(password)  # Hash the password
        user = User(username, email, password_hash)
        try:
            # Attempt to insert the user into the database
            result = mongo.db.users.insert_one(user.to_json())
            if result.inserted_id:
                return user  # Valid use of return within the method
        except Exception as e:
            print(f"Error creating user: {e}")
        return None  # Also a valid use of return within the method



    def to_json(self):
        return {
            "_id": str(self._id),  # Ensure conversion to string
            "username": self.username,
            "email": self.email,
            "password_hash": self.password_hash
        }

    @staticmethod
    def get_user_by_username(username):
        user_data = mongo.db.users.find_one({"username": username})
        if user_data:
            return User(user_data['username'], user_data['email'], user_data['password_hash'], user_data['_id'])
        return None

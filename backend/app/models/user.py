from flask_login import UserMixin
from bson.objectid import ObjectId
from app import bcrypt, mongo  # Ensure these are correctly initialized elsewhere in your application

class User(UserMixin):
    def __init__(self, username, email, password_hash=None, tasks =None, _id=None):
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.tasks = tasks or []
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
            print(mongo)
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
            "password_hash": self.password_hash,
            "tasks" : self.tasks
        }

    @staticmethod
    def get_user_by_username(username):
        user_data = mongo.db.users.find_one({"username": username})
        if user_data:
            return User(username = user_data['username'], email = user_data['email'], password_hash = user_data['password_hash'], _id = user_data['_id'], tasks = user_data.get('tasks',[]))
        return None
    
    def get_id(self):
        return str(self._id) #Convert ObjectID to string

def add_task(self, task_id):
    if not self.tasks:
        self.tasks = []
    self.tasks.append(task_id)
    mongo.db.users.update_one({"_id": self._id}, {"$set": {"tasks": self.tasks}})

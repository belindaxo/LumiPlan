from app import mongo

def create_user(username, email, password_hash):
    user = {
        "username": username,
        "email": email,
        "password_hash": password_hash,
    }
    mongo.db.users.insert_one(user)
    return user
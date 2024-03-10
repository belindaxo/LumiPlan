import os
import sys
# Append the path of the parent directory to ensure the 'app' module can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir)))
import unittest
from app import create_app
from flask_pymongo import PyMongo

class UserTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test application."""
        self.app = create_app()
        self.app.config.from_object('config.TestingConfig')
        self.client = self.app.test_client()
        with self.app.app_context():
            self.db = PyMongo(self.app).db
            self.db.users.delete_many({})  # Clean up the users collection

    def tearDown(self):
        """Clean up after tests."""
        with self.app.app_context():
            self.db.users.delete_many({})

    def test_user_registration(self):
        """Test user can register."""
        response = self.client.post('/register', json={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('user created', response.get_json()['message'])

if __name__ == '__main__':
    unittest.main()

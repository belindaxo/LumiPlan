import unittest
from app import app, mongo
from bson.objectid import ObjectId

class TagTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.context = app.app_context()
        self.context.push()
        self.app.testing = True
        mongo.db.tags.delete_many({})
    
    def tearDown(self):
        # Cleanup or any teardown operations after each test
        mongo.db.tags.delete_many({})
        # Pop the application context
        if self.context is not None:
            self.context.pop()

    
    def test_add_tag(self):
        response = self.app.post('/tags', json={'user_id': str(ObjectId()), 'name': 'Homework'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('name', response.json)
        self.assertEqual(response.json['name'], 'Homework')

if __name__ == '__main__':
    unittest.main()
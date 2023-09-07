import unittest
from app import app

class FlaskAppTests(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        
    def test_registration(self):
        response = self.client.post('/register', json={"username": "testuser", "password": "testpass"})
        self.assertEqual(response.status_code, 201)
        
    def test_login(self):
        # Register first
        self.client.post('/register', json={"username": "testuser", "password": "testpass"})
        
        # Now login
        response = self.client.post('/login', json={"username": "testuser", "password": "testpass"})
        self.assertEqual(response.status_code, 200)
        
    def test_create_item(self):
        self.client.post('/register', json={"username": "testuser", "password": "testpass"})
        self.client.post('/login', json={"username": "testuser", "password": "testpass"})
        
        response = self.client.post('/item', json={"id": "1", "name": "Item1"})
        self.assertEqual(response.status_code, 201)
        
    def test_read_item(self):
        self.client.post('/register', json={"username": "testuser", "password": "testpass"})
        self.client.post('/login', json={"username": "testuser", "password": "testpass"})
        self.client.post('/item', json={"id": "1", "name": "Item1"})
        
        response = self.client.get('/item/1')
        self.assertEqual(response.status_code, 200)
        
    def test_update_item(self):
        self.client.post('/register', json={"username": "testuser", "password": "testpass"})
        self.client.post('/login', json={"username": "testuser", "password": "testpass"})
        self.client.post('/item', json={"id": "1", "name": "Item1"})
        
        response = self.client.put('/item/1', json={"name": "UpdatedItem1"})
        self.assertEqual(response.status_code, 200)
        
    def test_delete_item(self):
        self.client.post('/register', json={"username": "testuser", "password": "testpass"})
        self.client.post('/login', json={"username": "testuser", "password": "testpass"})
        self.client.post('/item', json={"id": "1", "name": "Item1"})
        
        response = self.client.delete('/item/1')
        self.assertEqual(response.status_code, 200)
        
    def test_unauthorized_access(self):
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 401)

if __name__ == '__main__':
    unittest.main()

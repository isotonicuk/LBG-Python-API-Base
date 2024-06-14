import unittest
from lbg import item_builder
from flask_api import status
import requests

PORT = 8080
BASE_URL = f"http://localhost:{PORT}"

class MyLbgApiTestCase(unittest.TestCase):

    def test_item_builder_data(self):
        expected = {'name': 'Tool', 'description': 'Hammer', 'price': 10.5, '_id': 99}
        self.assertEqual(item_builder("Tool", "Hammer", 10.50, 99), expected)

    def test_item_builder_type(self):
        self.assertIsInstance(item_builder("Tool", "Hammer", 10.50, 99), dict)

    def test_create_post_request_status(self):
        response = requests.post(BASE_URL + '/create', json={'name': 'Tool', 'description': 'Hammer', 'price': 10.5})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    @unittest.skip("Skip this test for now using this decorator...")
    def test_create_post_request_type(self):
        response = requests.post(BASE_URL + '/create', json={'name': 'Vegetable', 'description': 'Leek', 'price': .7})
        self.assertIsInstance(response, object)
    
    def test_response_contains_expected_json_fields(self):
        item = requests.post(BASE_URL + '/create', json={'name': 'Vegetable', 'description': 'Leek', 'price': 0.7})
        print("POST response status:", item.status_code)
        print("POST response JSON:", item.json())

        response = requests.get(BASE_URL + '/read/2')
        print("GET response status:", response.status_code)
        print("GET response JSON:", response.json())

        self.assertEqual(response.json(), {"_id": 2, 'name': 'Vegetable', 'description': 'Leek', 'price': 0.7})
    
    @classmethod
    def tearDownClass(cls):
        requests.delete(BASE_URL + '/delete/1')
        requests.delete(BASE_URL + '/delete/2')

if __name__ == '__main__':
    unittest.main(verbosity=2)

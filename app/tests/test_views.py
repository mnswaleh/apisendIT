from app import create_app
import unittest
import json


class TestDeliveryOrders(unittest.TestCase):
    def setUp(self):
        create_app().testing = True
        self.app = create_app().test_client()
        self.data = {
            "order no": "588356",
            "pick up location": "nanyuki",
            "delivery location": "nairobi",
            "weight": "2kg",
            "price": "2000",
            "sender": 1
        }

    def test_create_order(self):
        response = self.app.post(
            '/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')

        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('pending', str(result))


if __name__ == '__main__':
    unittest.main()

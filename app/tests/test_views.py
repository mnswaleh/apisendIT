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

        self.edit_data = {
            "delivery location": "narok",
            "current location": "kikuyu",
            "status": "in transit"
        }

    def test_create_order(self):
        response = self.app.post(
            '/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        result = json.loads(response.data)
        self.assertIn('pending', str(result))

    def test_get_all_orders(self):
        response = self.app.post(
            '/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.app.get(
            '/api/v1/parcels', content_type='application/json')
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.data)
        self.assertIn('588356', str(result))

    def test_get_specific_order(self):
        response = self.app.post(
            '/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.app.get(
            '/api/v1/parcels/588356', content_type='application/json')
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.data)
        self.assertIn('588356', str(result))

    def test_get_delivery_orders_by_user(self):
        response = self.app.post(
            '/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.app.get(
            '/api/v1/users/1/parcels', content_type='application/json')
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.data)
        self.assertIn('588356', str(result))

    def test_cancel_delivery_order(self):
        response = self.app.post(
            '/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.app.put(
            '/api/v1/parcels/588356/cancel', content_type='application/json')
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.data)
        self.assertIn('canceled', str(result))

    def test_edit_delivery_order(self):
        response = self.app.post(
            '/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.app.put(
            '/api/v1/parcels/588356', data=json.dumps(self.edit_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.data)
        self.assertIn('kikuyu', str(result))

    def test_change_delivery_location(self):
        response = self.app.post(
            '/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.app.put(
            '/api/v1/parcels/588356/change-delivery', data=json.dumps(self.edit_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.data)
        self.assertIn('narok', str(result))

    def test_get_delivered_orders_for_user(self):
        response = self.app.post(
            '/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.app.get(
            '/api/v1/users/1/delivered', content_type='application/json')
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.data)
        self.assertIn('Delivered', str(result))

    def test_get_in_transit_orders_for_user(self):
        response = self.app.post(
            '/api/v1/parcels', data=json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        response = self.app.get(
            '/api/v1/users/1/in-transit', content_type='application/json')
        self.assertEqual(response.status_code, 200)

        result = json.loads(response.data)
        self.assertIn('in-transit', str(result))


if __name__ == '__main__':
    unittest.main()

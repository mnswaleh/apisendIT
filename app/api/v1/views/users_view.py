"""Users view Module"""

from flask import make_response, jsonify, request
from flask_restful import Resource
from app.api.v1.models.users_model import UsersModel
from app.api.v1.models.orders_model import OrdersModel

class Users(Resource):
    """Create Delivery Orders Object to create delivery order and fetch all orders"""

    def __init__(self):
        self.orders_db = UsersModel()

    def post(self):
        """Create delivery User"""
        data = request.get_json(force=True)
        
        result = self.orders_db.create_user(data['username'], data['first_name'],
                                             data['second_name'], data['email'], data['gender'], data['location'], data['password'])

        return make_response(jsonify(result), 201)


class UserOrders(Resource):
    """Create Users object to fetch all delivery orders"""

    def __init__(self):
        self.users_db = UsersModel()
        self.orders_db = OrdersModel()

    def get(self, userId):
        """ Fetch all delivery orders created by a specific user"""
        user = self.users_db.get_user(userId)
        result = self.orders_db.get_user_orders(userId)

        return make_response(jsonify({"Title": "Delivery orders by " + user['username'], "Delivery orders list": result}))


class UserDeliveredOrders(Resource, UsersModel):
    """Create Users object to fetch specific delivery order"""

    def __init__(self):
        self.users_db = UsersModel()
        self.orders_db = OrdersModel()

    def get(self, userId):
        """Fetch delivery orders delivered for a specific user"""
        user = self.users_db.get_user(userId)
        result = self.orders_db.get_delivered_orders(userId)

        return make_response(jsonify({"Delivered orders for " + user['username']: result}))


class UserOrdersInTransit(Resource):
    """User object to fetch orders in transit for a specific user"""

    def __init__(self):
        self.users_db = UsersModel()
        self.orders_db = OrdersModel()

    def get(self, userId):
        """Fetch delivery orders in transit for a specific user"""
        user = self.users_db.get_user(userId)
        result = self.orders_db.get_orders_in_transit(userId)

        return make_response(jsonify({"Orders in-transit for " + user['username']: result}))

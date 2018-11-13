"""Users view Module"""

from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from app.api.v1.models.users_model import UsersModel
from app.api.v1.models.orders_model import OrdersModel, ValidateInputs


class Users(Resource):
    """Create users class to create a user"""

    def __init__(self):
        self.orders_db = UsersModel()
        self.result = reqparse.RequestParser()

    def post(self):
        """Create User"""
        self.result.add_argument(
            'username', type=str, help="username is required to be a string", required=True, location='json')
        self.result.add_argument(
            'first_name', type=str, help="first name is required to be a string", required=True, location='json')
        self.result.add_argument(
            'second_name', type=str, help="second name is required to be a string", required=True, location='json')
        self.result.add_argument(
            'email', type=str, help="email", required=True, location='json')
        self.result.add_argument(
            'gender', type=str, help="gender is required to be a string", required=True, location='json')
        self.result.add_argument(
            'location', type=str, help="location is required to be a string", required=True, location='json')
        self.result.add_argument(
            'password', type=str, help="password is required to be a string", required=True, location='json')
        data = self.result.parse_args()
        inputs_validate = ValidateInputs(data, 'create_user')
        data_validation = inputs_validate.confirm_input()
        if data_validation != "ok":
            return make_response(jsonify({"Error": data_validation}), 400)
        else:
            result = self.orders_db.create_user(data)

            return make_response(jsonify(result), 201)


class UserSignin(Resource):
    """Create users class to signin a user"""

    def __init__(self):
        self.orders_db = UsersModel()

    def post(self):
        """Create delivery User"""
        result = reqparse.RequestParser()

        result.add_argument(
            'username', type=str, help="invalid useraname or password", required=True, location='json')
        result.add_argument(
            'password', type=str, help="invalid useraname or password", required=True, location='json')
        data = result.parse_args()
        inputs_validate = ValidateInputs(data, 'signin')
        data_validation = inputs_validate.confirm_input()
        if data_validation != "ok":
            return make_response(jsonify({"Error": data_validation}), 400)
        else:
            result = self.orders_db.user_login(
                data['username'], data['password'])

            return make_response(jsonify(result), 200)


class UserOrders(Resource):
    """Create Users object to fetch all delivery orders"""

    def __init__(self):
        self.users_db = UsersModel()
        self.orders_db = OrdersModel()

    def get(self, userId):
        """ Fetch all delivery orders created by a specific user"""
        user = self.users_db.get_user(1)
        result = self.orders_db.get_user_orders(1)

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

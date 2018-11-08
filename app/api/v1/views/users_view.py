from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, reqparse
from app.api.v1.models.users_model import UsersModel
from app.api.v1.models.orders_model import OrdersModel


class UserOrders(Resource, UsersModel, OrdersModel):

    def __init__(self):
        self.db = UsersModel()
        self.orders = OrdersModel()

    def get(self, userId):
        user = self.db.get_user(userId)
        result = self.orders.get_user_orders(userId)

        return make_response(jsonify({"Title": "Delivery orders by " + user['username'], "Delivery orders list": result}))


class UserDeliveredOrders(Resource, UsersModel, OrdersModel):

    def __init__(self):
        self.db = UsersModel()
        self.orders = OrdersModel()

    def get(self, userId):
        user = self.db.get_user(userId)
        result = self.orders.get_delivered_orders(userId)

        return make_response(jsonify({"Delivered orders for " + user['username'] : result}))

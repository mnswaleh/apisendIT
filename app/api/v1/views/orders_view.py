from flask import Flask, make_response, jsonify, request
from flask_restful import Resource, reqparse
from app.api.v1.models.orders_model import OrdersModel
from app.api.v1.models.users_model import UsersModel


class DeliveryOrders(Resource, OrdersModel, UsersModel):

    def __init__(self):
        self.db = OrdersModel()

    def get(self):
        result = self.db.get_orders()

        return make_response(jsonify({"Title": "Delivery orders", "Delivery orders list": result}))

    def post(self):
        
        data = request.get_json(force = True)

        result = self.db.create_order(data['order no'], data['pick up location'],
                                      data['delivery location'], data['weight'], data['price'], data['sender'])

        return make_response(jsonify(result), 201)


class DeliveryOrder(Resource, OrdersModel):

    def __init__(self):
        self.db = OrdersModel()

    def get(self, parcelId):
        result = self.db.get_order(parcelId)

        return make_response(jsonify(result))
        


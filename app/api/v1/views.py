from flask import Flask, make_response, jsonify, request
from flask_restful import Resource
from app.api.v1.models import OrdersModel


class DelieryOrders(Resource, OrdersModel):

    def __init__(self):
        self.db = OrdersModel()

    def get(self):
        result = self.db.get_orders()

        return make_response(jsonify({"message": "Delivery orders", "Delivery orders list": result}))
        
class DelieryOrder(Resource, OrdersModel):

    pass

from flask import Flask, make_response, jsonify, request
from flask_restful import Resource
from app.api.v1.models import OrdersModel


class DelieryOrders(Resource, OrdersModel):

    def __init__(self):
        pass


class DelieryOrder(Resource, OrdersModel):

    def __init__(self):
        pass


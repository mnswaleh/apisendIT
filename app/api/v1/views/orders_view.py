"""Orders View Module"""

from flask import make_response, jsonify, request
from flask_restful import Resource
from app.api.v1.models.orders_model import OrdersModel, ValidateInputs


class DeliveryOrders(Resource):
    """Create Delivery Orders Object to create delivery order and fetch all orders"""

    def __init__(self):
        self.orders_db = OrdersModel()

    def get(self):
        """Fetch all orders"""
        result = self.orders_db.get_orders()
        
        return make_response(jsonify({"Title": "Delivery orders", "Delivery orders list": result}))

    def post(self):
        """Create delivery order"""
        data = request.get_json(force=True)
        inputs_validate = ValidateInputs(data, 'create_order')
        data_validation = inputs_validate.confirm_input()
        if data_validation != "ok":
            return make_response(jsonify({"Error": data_validation}), 400)
        else:
            result = self.orders_db.create_order(data['order no'], data['pick up location'],
                                                data['delivery location'], data['weight'], data['price'], data['sender'])

            return make_response(jsonify(result), 201)


class DeliveryOrder(Resource):
    """Create Delivery Order Object to fetch a specific delivery order or update current location"""

    def __init__(self):
        self.orders_db = OrdersModel()

    def get(self, parcelId):
        """Fetch a specific delivery order"""
        result = self.orders_db.get_order(parcelId)

        return make_response(jsonify(result))

    def put(self, parcelId):
        """Update a delivery order"""
        data = request.get_json(force=True)
        inputs_validate = ValidateInputs(data, 'update_order')
        data_validation = inputs_validate.confirm_input()
        if data_validation != "ok":
            return make_response(jsonify({"Error": data_validation}), 400)
        else:
            result = self.orders_db.update_order(
                parcelId, data['current location'], data['status'])

            return make_response(jsonify(result))


class DeliveryOrderUpdate(Resource):
    """Create Delivery Orders Object to create delivery order and fetch all orders"""

    def __init__(self):
        self.orders_db = OrdersModel()

    def put(self, parcelId):
        """Cancel a delivery order"""
        result = self.orders_db.cancel_order(parcelId)

        return make_response(jsonify({"message": "order " + parcelId + " is canceled!", "Order " + parcelId: result}))


class DeliveryOrderDeliveryUpdate(Resource):
    """Create Delivery Orders Object to update delivery order details"""

    def __init__(self):
        self.orders_db = OrdersModel()

    def put(self, parcelId):
        """Change delivery location"""
        data = request.get_json(force=True)
        inputs_validate = ValidateInputs(data, 'change_delivery')
        data_validation = inputs_validate.confirm_input()
        if data_validation != "ok":
            return make_response(jsonify({"Error": data_validation}), 400)
        else:
            result = self.orders_db.change_delivery(parcelId, data['delivery location'])

            return make_response(jsonify({"message": "order " + parcelId + "Delivery location changed!", "Order " + parcelId: result}))

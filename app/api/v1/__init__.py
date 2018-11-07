from flask_restful import Api, Resource
from flask import Blueprint
from app.api.v1.views.orders_view import DeliveryOrders, DeliveryOrder, DeliveryOrderUpdate
from app.api.v1.views.users_view import UserOrders

version1 = Blueprint('sendit', __name__, url_prefix="/api/v1")

api = Api(version1)

api.add_resource(DeliveryOrders, '/parcels')
api.add_resource(DeliveryOrder, '/parcels/<parcelId>')
api.add_resource(DeliveryOrderUpdate, '/parcels/<parcelId>/cancel')
api.add_resource(UserOrders, '/users/<int:userId>/parcels')

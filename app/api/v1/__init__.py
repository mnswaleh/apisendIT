"""Initialize version 1"""

from flask_restful import Api, Resource
from flask import Blueprint
from app.api.v1.views.orders_view import DeliveryOrders, DeliveryOrder, DeliveryOrderUpdate, DeliveryOrderDeliveryUpdate
from app.api.v1.views.users_view import UserOrders, UserDeliveredOrders, UserOrdersInTransit, Users

VERSION1 = Blueprint('sendit', __name__, url_prefix="/api/v1")

API = Api(VERSION1)

"""Add resources"""

API.add_resource(DeliveryOrders, '/parcels', strict_slashes=False)
API.add_resource(DeliveryOrder, '/parcels/<parcelId>', strict_slashes=False)
API.add_resource(DeliveryOrderUpdate,
                 '/parcels/<parcelId>/cancel', strict_slashes=False)
API.add_resource(DeliveryOrderDeliveryUpdate,
                 '/parcels/<parcelId>/change-delivery', strict_slashes=False)
API.add_resource(UserOrders, '/users/<int:userId>/parcels',
                 strict_slashes=False)
API.add_resource(UserDeliveredOrders,
                 '/users/<int:userId>/delivered', strict_slashes=False)
API.add_resource(UserOrdersInTransit,
                 '/users/<int:userId>/in-transit', strict_slashes=False)
API.add_resource(Users, '/users', strict_slashes=False)

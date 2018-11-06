from flask_restful import Api, Resource
from flask import Blueprint
from app.api.v1.views import DelieryOrders, DelieryOrder

version1 = Blueprint('sendit', __name__, url_prefix="/api/v1")

api = Api(version1)

api.add_resource(DelieryOrders, '/parcels')

api.add_resource(DelieryOrder, '/parcels/<parcelId>')

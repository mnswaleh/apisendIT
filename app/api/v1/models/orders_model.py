from datetime import date
from .users_model import UsersModel
orders = [{
    "order id": 1,
    "order no": "678356",
    "date created": "23/07/2018",
    "pick up location": "nanyuki",
    "delivery location": "nairobi",
    "current location": "kikuyu",
    "weight": "2kg",
    "price": "2000",
    "status": "in transit",
    "sender": 1
}]


class OrdersModel(object):

    def __init__(self):
        self.user = UsersModel()
        self.users = self.user.get_users()

    def create_order(self, order_no, pick_up, delivery, weight, price, sender):
        today = date.today()

        created = today.strftime("%d/%m/%Y")

        order = {
            "order id": len(orders) + 1,
            "order no": order_no,
            "date created": created,
            "pick up location": pick_up,
            "delivery location": delivery,
            "current location": pick_up,
            "weight": weight,
            "price": price,
            "status": "pending",
            "sender": sender
        }

        orders.append(order)

        return order

    def get_orders(self):
        for order in orders:
            for user in self.users:
                if user['user id'] == order['sender']:
                    order['sender'] = user['username']
                    break

        return orders

    def get_order(self, order_id):
        result = {"message": "order unknown"}

        for order in orders:
            if order['order no'] == order_id:
                result = order
                break

        return result

    def update_order(self, order_id, location, status):
        result = {"message": "order unknown"}

        for order in orders:
            if order['order no'] == order_id:
                order['current location'] = location
                order['status'] = status
                result = order
                break

        return result

    def cancel_order(self, order_id):
        result = {"message": "order unknown"}

        for order in orders:
            if order['order no'] == order_id:
                order['status'] = "canceled"
                result = order
                break

        return result

    def change_delivery(self, order_id, delivery_location):
        result = {"message": "order unknown"}

        for order in orders:
            if order['order no'] == order_id:
                order['current location'] = delivery_location
                result = order
                break

        return result

    def get_user_orders(self, user_id):
        user_orders = []
        for order in orders:
            if order['sender'] == user_id:
                for user in self.users:
                    if user['user id'] == order['sender']:
                        order['sender'] = user['username']
                        break
                user_orders.append(order)

        return user_orders

    def get_delivered_orders(self, user_id):
        user_orders = [order for order in orders if (order['sender'] == user_id and order['status'] == 'delivered')]

        return len(user_orders)

    def get_orders_in_transit(self, user_id):
        user_orders = [order for order in orders if (order['sender'] == user_id and order['status'] == 'in transit')]

        return len(user_orders)

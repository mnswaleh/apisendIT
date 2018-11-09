"""Orders Models"""

from datetime import date
from .users_model import UsersModel
orders = []


class OrdersModel():
    """Create Orders Model"""

    def __init__(self):
        self.users_db = UsersModel()
        self.order_db = orders

    def create_order(self, order_no, pick_up, delivery, weight, price, sender):
        """Create order and append it to orders"""
        today = date.today()

        created = today.strftime("%d/%m/%Y")

        order = {
            "order id": len(self.order_db) + 1,
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

        self.order_db.append(order)

        return order

    def get_orders(self):
        """Get orders in database"""
        users = self.users_db.get_users()

        for order in self.order_db:
            for user in users:
                if user['user id'] == order['sender']:
                    order['sender'] = user['username']
                    break

        return self.order_db

    def get_order(self, order_id):
        """Get a specific order from database"""
        result = {"message": "order unknown"}

        for order in self.order_db:
            if order['order no'] == order_id:
                result = order
                break

        return result

    def update_order(self, order_id, location, status):
        """update order details"""
        result = {"message": "order unknown"}

        for order in self.order_db:
            if order['order no'] == order_id:
                order['current location'] = location
                order['status'] = status
                result = order
                break

        return result

    def cancel_order(self, order_id):
        """Cancel delivery order"""
        result = {"message": "order unknown"}

        for order in self.order_db:
            if order['order no'] == order_id:
                order['status'] = "canceled"
                result = order
                break

        return result

    def change_delivery(self, order_id, delivery_location):
        """change delivery location"""
        result = {"message": "order unknown"}

        for order in self.order_db:
            if order['order no'] == order_id:
                order['current location'] = delivery_location
                result = order
                break

        return result

    def get_user_orders(self, user_id):
        """Get orders created by specific order"""
        users = self.users_db.get_users()

        user_orders = []
        for order in self.order_db:
            if order['sender'] == user_id:
                for user in users:
                    if user['user id'] == order['sender']:
                        order['sender'] = user['username']
                        break
                user_orders.append(order)

        return user_orders

    def get_delivered_orders(self, user_id):
        """Get delivered orders for a specific user"""
        user_orders = [order for order in self.order_db if (
            order['sender'] == user_id and order['status'] == 'delivered')]

        return len(user_orders)

    def get_orders_in_transit(self, user_id):
        """Get orders in transit by a specific user"""
        user_orders = [order for order in self.order_db if (
            order['sender'] == user_id and order['status'] == 'in transit')]

        return len(user_orders)

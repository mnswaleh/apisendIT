"""Orders Models"""
from flask import json
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


class ValidateInputs():
    """Class to validate inputs entered by user"""

    def __init__(self, fetch_data, data_for):
        self.user_input = fetch_data
        self.data_for = data_for

    def confirm_input(self):
        """Confirm if there is user input"""
        message = "Bad request, No data entered"
        if self.user_input:
            if self.data_for == "create_user":
                message = self.create_user_inputs()
            elif self.data_for == "create_order":
                message = self.create_order_inputs()
            elif self.data_for == "update_order":
                message = self.update_order_inputs()
            else:
                message = self.change_delivery_inputs()

        return message

    def create_user_inputs(self):
        """confirm inputs for creating user"""
        if 'username' in self.user_input and 'first_name' in self.user_input and 'first_name' in self.user_input and 'second_name' in self.user_input and 'email' in self.user_input and 'location' in self.user_input and 'gender' in self.user_input and 'password' in self.user_input:
            if not self.user_input['username']:
                message = "username missing"
            elif not self.user_input['first_name']:
                message = "first name  missing"
            elif not self.user_input['second_name']:
                message = "second name  missing"
            elif not self.user_input['email']:
                message = "email  missing"
            elif not self.user_input['location']:
                message = "location  missing"
            elif not self.user_input['gender']:
                message = "gender missing"
            elif not self.user_input['password']:
                message = "password missing"
            else:
                message = "ok"
        else:
            message = "Bad request, An Entry is missing"

        return message

    def create_order_inputs(self):
        """confirm inputs for creating order"""
        if 'order no' in self.user_input and 'pick up location' in self.user_input and 'delivery location' in self.user_input and 'weight' in self.user_input and 'price' in self.user_input and 'sender' in self.user_input:
            if not self.user_input['order no']:
                message = "order no missing"
            elif not self.user_input['pick up location']:
                message = "pickup location missing"
            elif not self.user_input['delivery location']:
                message = "delivery locationv missing"
            elif not self.user_input['weight']:
                message = "weight missing"
            elif not self.user_input['price']:
                message = "price missing"
            elif not self.user_input['sender']:
                message = "sender missing"
            else:
                message = "ok"
        else:
            message = "Bad request, An Entry is missing"

        return message

    def update_order_inputs(self):
        """confirm inputs for updating order"""
        if 'current location' in self.user_input and 'status' in self.user_input:
            if not self.user_input['current location']:
                message = "current location missing"
            elif not self.user_input['status']:
                message = "status missing"
            else:
                message = "ok"
        else:
            message = "Bad request, An Entry is missing"

        return message

    def change_delivery_inputs(self):
        """confirm inputs for changing delivery location"""
        if 'delivery location' in self.user_input:
            if not self.user_input['delivery location']:
                message = "delivery location missing"
            elif not self.user_input['status']:
                message = "status missing"
            else:
                message = "ok"
        else:
            message = "Bad request, An Entry is missing"

        return message

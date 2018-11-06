from datetime import date
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

users = [{
    "user id": 1,
    "username": "tom",
    "first name": "thomas",
    "second name": "wakati",
    "email": "email@gmail.com",
    "gender": "male",
    "location": "eldoret"
}]


class OrdersModel(object):

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
            for user in users:
                if user['user id'] == order['sender']:
                    order['sender'] = user['username']
                    break

        return orders

    def get_order(self, order_id):
        result = {"message" : "order unknown"}
        for order in orders:
            if order['order no'] == order_id:
                result = order
                break

        return result
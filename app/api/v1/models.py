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
        pass
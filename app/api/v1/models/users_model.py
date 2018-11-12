users = [{
            "user id": 1,
            "username": "tom",
            "first name": "thomas",
            "second name": "wakati",
            "email": "email@gmail.com",
            "gender": "male",
            "location": "eldoret",
            "password": "123456",
            "type": "user"
        },
        {
            "user id": 2,
            "username": "tosh",
            "first name": "samwel",
            "second name": "toroka",
            "email": "tosh@gmail.com",
            "gender": "male",
            "location": "kisumu",
            "password": "123456",
            "type": "admin"
        }]


class UsersModel(object):

    def get_users(self):
        return users

    def get_user(self, user_id):
        my_user = [user for user in users if  user['user id'] == user_id]
        return my_user[0]

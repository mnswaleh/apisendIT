"""Users Module"""

users = []


class UsersModel():
    """Create Users Model"""

    def __init__(self):
        self.user_db = users

    def create_user(self, data):
        """Create user and append to users db"""
        user = {
            "user id": len(self.user_db) + 1,
            "username": data['username'],
            "first_name": data['first_name'],
            "second_name": data['second_name'],
            "email": data['email'],
            "gender": data['gender'],
            "location": data['location'],
            "password": data['password'],
            "type": "user"
        }
        self.user_db.append(user)

        return {"user name": user['username'], "user details":user}

    def user_login(self, username, password):
        """User login method"""
        my_user = [user for user in self.user_db if (
            user['username'] == username and user['password'] == password)]
        if not my_user:
            return "username or password invalid!"
        else:
            return my_user

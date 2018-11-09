"""Users Module"""
users = []


class UsersModel():
    """Create Users Model"""

    def __init__(self):
        self.user_db = users

    def create_user(self, username, first_name, second_name, email, gender, location, password):
        """Create order and append it to orders"""
        user = {
            "user id": len(self.user_db) + 1,
            "username": username,
            "first_name": first_name,
            "second_name": second_name,
            "email": email,
            "gender": gender,
            "location": location,
            "password": password,
            "type": "user"
        }

        self.user_db.append(user)

        return user

    def get_users(self):
        """Get all users in the database"""
        return self.user_db

    def get_user(self, user_id):
        """Get a specific user from the database"""
        my_user = [user for user in self.user_db if user['user id'] == user_id]
        return my_user[0]

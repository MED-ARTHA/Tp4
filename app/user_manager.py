# app/user_manager.py

class UserManager:
    def __init__(self):
        self._users = {}  # initialize the user store

    def add_user(self, username, user_data=None):
        if username in self._users:
            raise ValueError(f"User '{username}' already exists")
        self._users[username] = user_data

    def remove_user(self, username):
        if username not in self._users:
            raise ValueError(f"User '{username}' does not exist")
        del self._users[username]

    def count_users(self):
        return len(self._users)

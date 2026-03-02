# app/user_manager.py
class UserManager:
    def create_user(self, name):
        return type("User", (), {"name": name})()

"""Simple in-memory user manager used by tests."""


class UserManager:
    """Manage users in memory keyed by unique username."""

    def __init__(self):
        self._users = {}

    def add_user(self, username, user_data=None):
        """Add a new user. Raises ValueError if user exists."""
        if username in self._users:
            raise ValueError("User already exists")
        self._users[username] = user_data

    def get_user(self, username):
        """Return user data by username, or None if not found."""
        return self._users.get(username)

    def remove_user(self, username):
        """Remove user by username. Raises ValueError if not found."""
        if username not in self._users:
            raise ValueError("User not found")
        return self._users.pop(username)

    def list_users(self):
        """Return a copy of all users."""
        return dict(self._users)

    def count_users(self):
        """Return total number of users."""
        return len(self._users)
    
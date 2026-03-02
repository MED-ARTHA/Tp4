from app.user_manager import UserManager


def test_create_user():
    user = UserManager().create_user("alice")
    assert user.name == "alice"

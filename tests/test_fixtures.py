import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE]")


@pytest.fixture(scope="session")
def settings():
    print("[SESSION]")


@pytest.fixture(scope="class")
def user():
    print("[CLASS] Create data user")


@pytest.fixture(scope="function")
def user_client():
    print("[FUN]Create API client")


class TestUserFlow:
    def test_user_can_login(self, user, settings, user_client):
        ...

    def test_user_can_create_course(self,  user, settings,  user_client):
        ...


class TestAccountFlow:
    def test_user_account(self,  user, settings,  user_client):
        ...

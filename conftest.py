import pytest


@pytest.fixture(scope="function", autouse=True)
def tc_setup():
    print("Launch browser")
    print("Login")
    print("Browser products")
    # using yield to set tear down
    yield 
    print("Logoff")
    print("Close browser")
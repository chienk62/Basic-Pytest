import pytest


@pytest.fixture(scope="session", autouse=True)
def tc_setup(browser):
    if browser == "chrome":
        print("Launch chrome")
    elif browser == "ff":
        print("Launch firefox")
    else:
        print("provide valid browser")
    print("Login")
    print("Browser products")
    # using yield to set tear down
    yield 
    print("Logoff")
    print("Close browser")
    
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
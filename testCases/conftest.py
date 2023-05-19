

import pytest
from selenium import webdriver

# For Multiple Parameter

@pytest.fixture(params=[
    ("admin@yourstore.com" , "admin" , "Pass"),
    ("admin1@yourstore.com" , "admin" , "Fail"),
    ("admin@yourstore.com" , "admin1", "Fail"),
    ("admin1@yourstore.com" , "admin1", "Fail"),

])

def getLoginData(request):
    return request.param


# For Cross Browsers
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup1():
    d = webdriver.Chrome()
    d.maximize_window()
    return d


@pytest.fixture()
def setup(browser):

    if browser == 'chrome':
        print("Launching Chrome Browser...!!!")
        d = webdriver.Chrome()
        # d.get("https://admin-demo.nopcommerce.com/")

    elif browser == 'firefox':
        print("Launching Firefox Browser...!!!")
        d = webdriver.Firefox()

    elif browser == 'edge':
        print("Launching Edge Browser...!!!")
        d = webdriver.Edge()

    else:
        print("Launching Headless Browser...!!!")
        opt = webdriver.ChromeOptions()
        opt.add_argument("headless")
        d = webdriver.Chrome(options=opt)
    d.maximize_window()
    return d


def pytest_metadata(metadata):
    metadata["Envirnment"] = "Test"
    metadata["Project"] = "NonCommerse"
    metadata["Tester"] = "Rupali Pandit"

    metadata.pop("Packages", None)
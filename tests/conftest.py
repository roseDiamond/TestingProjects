import time

import pytest
from selenium import webdriver


# # this a adding a command line hook
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: type1 or type2"
    )

@pytest.fixture(scope="class")
def setup(request):

    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
        
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    
    else:
        driver = webdriver.Ie()

    driver.implicitly_wait(4)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice")
    # time.sleep(5)
    request.cls.driver = driver
    yield
    driver.quit()



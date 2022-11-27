import pytest
from selenium import webdriver


@pytest.fixture
def setupFile():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get('https://testautomationpractice.blogspot.com/')
    return driver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import pytest


@pytest.fixture()
def Setup():
    driver_path = "driver\\msedgedriver.exe"
    driver = webdriver.Edge(executable_path=driver_path)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()
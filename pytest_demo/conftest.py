import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import wait
import time


@pytest.fixture()
def setup():
    x = 2 + 3
    return x

    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # driver.get("https://www.orangehrm.com/")
    # time.sleep(5)
    # driver.close()

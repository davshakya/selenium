import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import wait
import time


@pytest.mark.usefixtures("setup")
class Test_folder:
    def test_case1(self, setup):
        # driver.find_element(By.XPATH, "//div[@class='d-flex web-menu-btn']//li[1]//a[1]").click()
        print("####",setup)
        c = 5
        assert c == setup, "not equal"


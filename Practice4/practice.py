import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.mark.runthis
def test_3rd_code():
    driver=webdriver.Chrome(service=Service(executable_path="C:/work/chromedriver.exe"))
    driver.get("https://www.w3schools.com/quiztest/quiztest.asp?qtest=PYTHON")
    print(driver.title)
    driver.maximize_window()
    time.sleep(5)
    var2=driver.find_element_by_id("label3")
    print(var2.is_selected())
    var2=driver.find_element_by_name("quiz")
    print(var2.is_selected())
    driver.close()

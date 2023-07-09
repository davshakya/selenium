from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("HTTP://masterprograming.com/")
driver.maximize_window()
print(driver.title)
time.sleep(5)
driver.get("HTTP://google.com/")
print(driver.title)
driver.back()
time.sleep(5)
driver.forward()

driver.close()  



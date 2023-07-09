from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import time
from selenium.webdriver import  ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# driver = webdriver.Chrome(service=Service("C:/Users/davsh/My Drive/Computer_Programmes/chromedriver.exe"))
driver.get("https://the-internet.herokuapp.com/context_menu")
action=ActionChains(driver)
time.sleep(5)
action.context_click(driver.find_element(By.XPATH,"//div[@id='hot-spot']")).perform()
action.double_click(driver.find_element(By.XPATH,"//div[@id='hot-spot']")).perform()
time.sleep(2)
driver.close()





import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get('https://www.google.com')  
driver.maximize_window()
driver.find_element(By.XPATH,"//a[contains(text(),'LOGIN')]").click
driver.find_element(By.XPATH,"//input[@placeholder='User Name']").send_keys('davshakya')
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys('Ranjana21#')


time.sleep(10)
# driver.quit()
 
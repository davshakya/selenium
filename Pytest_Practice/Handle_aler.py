from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element_by_xpath("//input[@id='name']").send_keys("Devendra")
driver.find_element_by_xpath("//input[@id='alertbtn']").click()
popup=driver.switch_to.alert
t=popup.text
print(t)
popup.dismiss()

time.sleep(3)
driver.close()

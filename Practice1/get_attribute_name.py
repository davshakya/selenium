from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(executable_path="C:/work/chromedriver.exe"))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
a=driver.find_element_by_xpath("//input[@id='name']").get_attribute("placeholder")
print(a)
time.sleep(2)
driver.quit()





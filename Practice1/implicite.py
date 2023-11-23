from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(service=Service(executable_path="C:/work/chromedriver.exe"))
driver.get("https://masterprograming.com/contact-us/")
print(driver.title)
driver.maximize_window()

time.sleep(20)
var=driver.find_element_by_class_name("search-field")
print(var.is_displayed())

var1=driver.find_element_by_name("s")
print(var1.is_enabled())

var2=driver.find_element_by_class_name("serach-field")
print(var2.is_selected())

driver.close()




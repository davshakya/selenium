from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
# driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# d=driver.find_elements_by_xpath("//input[@type='checkbox']")
# for i in d:
#     i.click()

static_dropdown = Select(driver.find_element_by_xpath("//select[@id='dropdown-class-example']"))
static_dropdown.select_by_index(1)

# driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[2]/fieldset[1]/input[1]").send_keys("India")
# time.sleep(5)    
# country = driver.find_elements_by_xpath("/html[1]/body[1]/ul[1]/li/div")
# for i in country:
#     print(i)
#     if i.text == "British Indian Ocean Territory":
#         i.click()
# else:
#     pass

# driver.find_element_by_xpath("//input[@id='name']").send_keys("Devendra")
# driver.find_element_by_xpath("//input[@id='alertbtn']").click()
# popup=driver.switch_to.alert
# t=popup.text
# print(t)
# popup.dismiss()

time.sleep(3)
driver.close()




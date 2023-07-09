from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://chercher.tech/practice/implicit-wait-example")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]").click()
driver.find_element_by_xpath("//div[@id='q']/input[2]").click()

time.sleep(2)
driver.close()





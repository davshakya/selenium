import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(executable_path='F:\Computer_Programmes\chromedriver.exe')
driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("admin")
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//input[@id='btnLogin']").click()
time.sleep(5)
driver.close()














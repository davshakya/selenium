from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://the-internet.herokuapp.com/upload')

driver.maximize_window()
driver.find_element_by_xpath("//input[@id='file-upload']").send_keys("F:\\test1.jpg")
driver.find_element_by_xpath("//input[@id='file-submit']").click()
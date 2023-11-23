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
driver.implicitly_wait(30)

driver.switch_to_frame(driver.find_element_by_xpath("//ul[@class='clearfix']"))
driver.find_element_by_xpath("//div[@class='nav-outer clearfix']//a[normalize-space()='Job Support']").click()
driver.switch_to_default_content()
time.sleep(2)
driver.quit()










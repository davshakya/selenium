from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.rminfotechsolutions.com/")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[2]/a[1]').click()
driver.find_element_by_xpath('/html/body/div/p[2]/a[2]').click()
time.sleep(2)
driver.find_element_by_xpath("//input[@type='text']").send_keys("narsimha@gmail.com")
driver.find_element_by_xpath("//input[@type='password']").send_keys("godgreat")
driver.find_element_by_xpath("//input[@type='submit']").click()
time.sleep(2)
driver.quit()




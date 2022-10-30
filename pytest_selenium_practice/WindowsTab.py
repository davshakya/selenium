import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service
import validators
import requests
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(5)
driver.find_element(By.XPATH, "//a[@id='opentab']").click()
tab1 = driver.window_handles[1]
time.sleep(5)
driver.find_element(By.XPATH, "//a[@id='opentab']").click()
tab2 = driver.window_handles[2]
# driver.find_element(By.XPATH, "//button[@id='openwindow']").click()
# print(driver.window_handles)
# wind2 = driver.window_handles[2]
# driver.switch_to.window(driver.window_handles[1])
# driver.find_element(By.XPATH, "//div[@class='nav-outer clearfix']//a[normalize-space()='Courses']").click()
# driver.switch_to.window(driver.window_handles[2])
# driver.find_element(By.XPATH, "//*[@id='homepage']/header/div[2]/div/nav/ul/li[5]/a").click()

print(driver.title)
print(driver.current_url)
time.sleep(2)
# driver.quit()

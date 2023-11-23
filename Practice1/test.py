from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(executable_path="C:/work/chromedriver.exe"))
driver.get("HTTP://google.com/")
driver.maximize_window()
print(driver.title)
driver.close()

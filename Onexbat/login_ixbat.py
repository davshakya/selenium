from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Initialize Chrome driver instance
driver = webdriver.Chrome(service=Service(executable_path="C:/work/chromedriver.exe"))

# Navigate to the url
driver.get('https://pythonexamples.org/tmp/selenium/index.html')
time.sleep(5)
# Close the driver
driver.quit()
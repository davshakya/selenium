import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome(service=Service(executable_path="C:/work/chromedriver.exe"))
driver.get('https://www.bing.com/account/general?ru=https%3a%2f%2fwww.bing.com%2f%3ftoWww%3d1%26redig%3d1E6F5FF0FF114E2699C3C229F80E549C&FORM=O2HV65&id=language_section#language-section')  
driver.maximize_window
dd=driver.find_element_by_id('rpp')
s=Select(dd)
# s.select_by_index(2)
# s.select_by_value("30")
p1=s.options
print(p1)
time.sleep(2)
driver.quit()
 
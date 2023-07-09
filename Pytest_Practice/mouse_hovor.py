from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
from selenium.webdriver import ActionChains

driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-perform-mouse-hover-in-selenium.html")
driver.maximize_window()
action = ActionChains(driver)
action.move_to_element(driver.find_element_by_xpath("//button[contains(text(),'Automation Tools')]")).perform()
action.move_to_element(driver.find_element_by_xpath("//a[contains(text(),'TestNG')]")).click().perform()
driver.implicitly_wait(3)
driver.close()

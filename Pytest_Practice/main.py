
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/index.php/dashboard")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="txtUsername"]').send_keys("Admin")
driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("admin123")
driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
driver.find_element_by_xpath('//*[@id="menu_pim_viewPimModule"]/b').click()
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.find_element_by_xpath("//b[contains(text(),'Directory')]").click()
d=WebDriverWait(driver,5).until(ec.presence_of_element_located((By.xpath("//tbody/tr[4]/td[1]/img[1]")))
driver.execute_script("window.scrollBy(0,2000)")
driver.execute_script("window.scrollBy(0,0)")
time.sleep(3)
driver.close()




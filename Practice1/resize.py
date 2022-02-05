import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()
driver.get('https://jqueryui.com/resizable/')  
time.sleep(8)

fr=driver.find_element_by_class_name('demo-frame')
driver.switch_to_frame(fr)
# obj=driver.find_element_by_xpath('//*[@id="resizable"]/div[1]')
obj=driver.find_element_by_xpath("//div[@class='ui-resizable-handle ui-resizable-e']")
ActionChains(driver).drag_and_drop_by_offset(obj,150,150).perform()
time.sleep(2)
driver.close()








 
 
 
 
 
 
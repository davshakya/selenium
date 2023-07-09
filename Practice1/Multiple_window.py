from selenium import webdriver
from selenium.webdriver.common.by   import By
import time
driver = webdriver.Chrome(executable_path="c:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
parrent_window=driver.current_window_handle
driver.find_element(By.XPATH,"//a[@id='opentab']").click()
chld1=driver.window_handles[1]
time.sleep(5)
driver.switch_to.window(parrent_window)
time.sleep(5)
driver.find_element(By.XPATH,"//a[@id='opentab']").click()
driver.switch_to.window(chld1)
chld2=driver.window_handles[2]
allchld=driver.window_handles
print(allchld)



# tab=driver.window_handles[1]
# driver.find_element_by_xpath("//button[@id='openwindow']").click()
# window2=driver.window_handles[2]
# driver.switch_to_window(tab)
# # driver.switch_to_window(driver.window_handles[1])
# driver.find_element_by_xpath("//div[@class='nav-outer clearfix']//a[normalize-space()='Practice']").click()
# driver.switch_to_window(window2)
# driver.find_element_by_xpath("//a[normalize-space()='Practice']").click()

time.sleep(5)
driver.quit()





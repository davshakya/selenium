from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by   import By
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.support.wait    import WebDriverWait
import time
driver = webdriver.Chrome(executable_path="c:\work\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(5)
parrent_window=driver.current_window_handle
WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.XPATH,"//a[@id='opentab']")))
# WebDriverWait(driver,11).until(ec.element_to_be_clickable((By.XPATH,"//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]")))

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





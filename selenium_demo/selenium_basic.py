from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains    import ActionChains


driver=webdriver.Chrome(executable_path="C:\work\chromedriver.exe")
driver.get("http://www.google.com")
driver.maximize_window()
time.sleep(5)
is_element_visible=driver.find_element(By.XPATH,"//div[contains(text(),'Google offered in')]").is_displayed()
print(is_element_visible)
driver.find_element(By.XPATH,"//textarea[@id='APjFqb']").send_keys("Devendra")
action=ActionChains(driver)
action.send_keys(Keys.ENTER).perform()
WebDriverWait(driver, 5).until(ec.element_to_be_clickable((By.XPATH,"//span/*[contains(text(),'Overview')]")))
driver.close()



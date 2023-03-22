import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utiles.web_xpaths import WebXpath

class Test_Ui_Practice:
    def test_switch_windows(self):
        driver = webdriver.Chrome(executable_path="c:\work\chromedriver.exe")
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        main=driver.window_handles[0]
        driver.find_element(By.XPATH, WebXpath.open_window).click()
        w1=driver.window_handles[1]
        driver.switch_to.window(w1)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//div[@id='navbarSupportedContent']//a[contains(text(),'Courses')]").click()
        time.sleep(5)
        driver.close()
        driver.switch_to.window(main)
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@id='opentab']").click()
        t1=driver.window_handles[1]
        driver.switch_to.window(t1)
        driver.find_element(By.XPATH, "//a[contains(text(),'JOIN NOW')]").click()
        driver.close()
        time.sleep(5)
        driver.quite()

    def test_checkboxes(self):
        driver = webdriver.Chrome(executable_path="c:\work\chromedriver.exe")
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        driver.find_element(By.XPATH, WebXpath.checkbox1).click()
        driver.find_element(By.XPATH, WebXpath.checkbox2).click()
        driver.find_element(By.XPATH, WebXpath.checkbox3).click()
        time.sleep(5)
        driver.quite()


    def test_set_text(self):
        driver = webdriver.Chrome(executable_path="c:\work\chromedriver.exe")
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        driver.find_element(By.XPATH, WebXpath.set_text).send_keys("Devendra Shakya")
        time.sleep(5)
        driver.quite()


    def test_set_dropdown_option(self):
        driver = webdriver.Chrome(executable_path="c:\work\chromedriver.exe")
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        driver.find_element(By.XPATH, WebXpath.dropdown).click()
        driver.find_element(By.XPATH, WebXpath.dropdown_option1).click()
        time.sleep(2)
        driver.find_element(By.XPATH, WebXpath.dropdown).click()
        driver.find_element(By.XPATH, WebXpath.dropdown_option2).click()
        time.sleep(2)
        driver.find_element(By.XPATH, WebXpath.dropdown).click()
        driver.find_element(By.XPATH, WebXpath.dropdown_option3).click()
        time.sleep(5)
        driver.quite()

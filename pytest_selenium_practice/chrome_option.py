from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import validators

opt =Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")
driver = webdriver.Chrome(executable_path="C:\work\chromedriver.exe", chrome_options=opt)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_xpath("//input[@name='enter-name']").send_keys("Devendra Shakya")

driver.find_element_by_xpath('//*[@id="checkBoxOption1"]').click()
driver.find_element_by_css_selector("input[value='radio2']").click()
driver.find_element_by_xpath("//input[@value='radio1']").click()
t = driver.find_element_by_xpath("//legend[text()='Checkbox Example']").text


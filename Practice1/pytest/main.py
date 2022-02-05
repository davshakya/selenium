from selenium import webdriver
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.close()
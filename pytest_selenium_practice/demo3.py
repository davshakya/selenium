import pytest
from selenium import webdriver

@pytest.fixture
def chrome_driver():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome(executable_path='C:\\work\\chromedriver.exe')
    yield driver
    # Teardown - close the WebDriver after the test
    driver.quit()

# Test function using the Chrome WebDriver fixture
def test_example(chrome_driver):
    chrome_driver.get("https://www.example.com")
    assert "Example Domain" in chrome_driver.title

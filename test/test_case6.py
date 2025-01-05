import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from src.pages.home_page import HomePage

@pytest.fixture
def setup():
    service = Service(ChromeDriverManager().install())  # WebDriverManager se encarga de gestionar el ChromeDriver
    driver = webdriver.Chrome(service=service)
    driver.get("https://nuxqa4.avtest.ink/") 
    #driver.get("https://nuxqa5.avtest.ink/")
    yield driver
    driver.quit()

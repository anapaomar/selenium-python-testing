import pytest
from selenium import webdriver
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

def test_booking_one_way(setup):
    driver = setup
    home_page = HomePage(driver)

    home_page.set_language("English")
    home_page.set_point_of_sale("Colombia")
    home_page.set_journey("One way")
    home_page.select_origin("CTG")
    home_page.select_destination("MAD")
    home_page.select_passengers(1,1,1,1)
    home_page.searchFlight()



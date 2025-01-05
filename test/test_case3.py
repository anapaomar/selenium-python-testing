import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.support.ui import WebDriverWait
from src.pages.home_page import HomePage
from src.pages.flight_page import FlightPage
from src.pages.login_page import LoginPage

@pytest.fixture
def setup():
    # Configura las opciones de Chrome
    service = Service(ChromeDriverManager().install()) 
    driver = webdriver.Chrome(service=service)

    driver.get("https://nuxqa.avtest.ink//")
    yield driver
    driver.quit()

def test_login_UAT1(setup):
    driver = setup
    homepage = HomePage(driver)
    flightpage = FlightPage(driver)
    loginpage = LoginPage(driver)

    homepage.select_login_button()
    driver.implicitly_wait(2)
    window_handles = driver.window_handles
    driver.switch_to.window(window_handles[-1])

    loginpage.fillin_login_form("21734198706","Lifemiles1")
    driver.implicitly_wait(2)
    driver.switch_to.window(window_handles[0])

    homepage.set_language("Français")
    homepage.set_point_of_sale("France")
    homepage.set_journey("One way")
    homepage.select_origin("CTG")
    homepage.select_destination("MAD")
    homepage.select_passengers(3,3,3,3)
    homepage.searchFlight()

    flightpage.select_journey_price()
    flightpage.select_flight_type("light")
    flightpage.select_continue()
    
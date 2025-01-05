import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from src.pages.home_page import HomePage
from src.pages.flight_page import FlightPage
from src.pages.passenger_page import PassengerPage
from src.pages.service_page import ServicePage
from src.pages.seatmap_page import SeatmapPage


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
    homepage = HomePage(driver)
    flightpage = FlightPage(driver)
    passengerspage = PassengerPage(driver)
    servicespage = ServicePage(driver)
    seatmappage = SeatmapPage(driver)

    homepage.set_language("English")
    homepage.set_point_of_sale("Colombia")
    homepage.set_journey("One way")
    homepage.select_origin("CTG")
    homepage.select_destination("MAD")
    homepage.select_passengers(1,1,1,1)
    homepage.searchFlight()

    flightpage.select_journey_price()
    flightpage.select_flight_type("light")
    flightpage.select_continue()

    passengers_list = [
        {'gender': 'M', 'name': 'Juan', 'lastname': 'Pérez'},
        {'gender': 'F', 'name': 'Martha', 'lastname': 'Pérez'},
        {'gender': 'F', 'name': 'Laura', 'lastname': 'Pérez'},
        {'gender': 'M', 'name': 'Carlos', 'lastname': 'Pérez'}
    ]
    passengerspage.fillin_passenger_form(passengers_list)
    passengerspage.fillin_reservation_holder("57","32545698","jperez@gmail.com")
    passengerspage.select_continue()

    servicespage.select_continue()

    #seatmappage.select_seat("economy")



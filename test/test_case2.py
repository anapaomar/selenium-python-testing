import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from util.db_config import result_test
from src.pages.home_page import HomePage
from src.pages.flight_page import FlightPage
from src.pages.passenger_page import PassengerPage
from src.pages.service_page import ServicePage

@pytest.fixture
def setup():
    service = Service(ChromeDriverManager().install())  # WebDriverManager se encarga de gestionar el ChromeDriver
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    time.sleep(1)
    driver.get("https://nuxqa4.avtest.ink/") 
    #driver.get("https://nuxqa5.avtest.ink/")
    yield driver
    driver.quit()

@allure.feature('Reserva de vuelo de ida y vuelta')
@allure.story('Realizar una reserva de vuelo de ida y regreso desde Colombia a España')
def test_booking_round_trip(setup):
    driver = setup
    home_page = HomePage(driver)
    flight_page = FlightPage(driver)
    passenger_page = PassengerPage(driver)
    service_page = ServicePage(driver)
    try:
        with allure.step("Establecer idioma y punto de venta"):
            home_page.set_language("English")
            home_page.set_point_of_sale("Colombia")
        
        with allure.step("Seleccionar detalles del viaje"):
            home_page.set_journey("Round")
            home_page.select_origin("CTG")
            home_page.select_destination("MAD")
            home_page.select_passengers(1,1,1,1)
            home_page.searchFlight()

        with allure.step("Seleccionar precio y tipo de vuelo"):
            flight_page.select_journey_price("One way")
            flight_page.select_flight_type("light")
            flight_page.select_journey_price("Return")
            flight_page.select_flight_type("flex")
            flight_page.select_continue()

        with allure.step("Llenar formulario de pasajeros"):
            passengers_list = [
                {'gender': 'M', 'name': 'Juan', 'lastname': 'Pérez'},
                {'gender': 'F', 'name': 'Martha', 'lastname': 'Pérez'},
                {'gender': 'F', 'name': 'Laura', 'lastname': 'Pérez'},
                {'gender': 'M', 'name': 'Carlos', 'lastname': 'Pérez'}
            ]
            passenger_page.fillin_passenger_form(passengers_list)
        
        with allure.step("Llenar datos del titular de la reserva"):
            passenger_page.fillin_reservation_holder("57","32545698","jperez@gmail.com")
            passenger_page.select_continue()

        with allure.step("No seleccionar servicios en la página de servicios"):
            service_page.select_service("Lounge")
            service_page.select_continue()

        result_test('test_booking_round_trip','PASS')
    except Exception as e:
        result_test('test_booking_round_trip',f'FAIL: {str(e)}')
        raise e



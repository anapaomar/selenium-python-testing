import pytest
import allure
import time
from util.db_config import result_test
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
    service = Service(ChromeDriverManager().install()) 
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    time.sleep(1)
    driver.get("https://nuxqa4.avtest.ink/") 
    #driver.get("https://nuxqa5.avtest.ink/")
    yield driver
    driver.quit()

@allure.feature('Reserva de vuelo de ida')
@allure.story('Realizar una reserva de vuelo de ida desde Colombia a España')
def test_booking_one_way(setup):
    driver = setup
    home_page = HomePage(driver)
    flight_page = FlightPage(driver)
    passenger_page = PassengerPage(driver)
    service_page = ServicePage(driver)
    seatmap_page = SeatmapPage(driver)
    try:
        with allure.step("Establecer idioma y punto de venta"):
            home_page.set_language("English")
            home_page.set_point_of_sale("Colombia")
        
        with allure.step("Seleccionar detalles del viaje"):
            home_page.set_journey("One way")
            home_page.select_origin("CTG")
            home_page.select_destination("MAD")
            home_page.select_passengers(1,1,1,1)
            home_page.searchFlight()

        with allure.step("Seleccionar precio y tipo de vuelo"):
            flight_page.select_journey_price("One way")
            flight_page.select_flight_type("light")
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
            service_page.select_continue()

        #seatmappage.select_seat("economy")
        result_test('test_booking_one_way','PASS')
    except Exception as e:
        result_test('test_booking_one_way',f'FAIL: {str(e)}')
        raise e



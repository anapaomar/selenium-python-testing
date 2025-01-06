import pytest
import allure
from util.db_config import result_test
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
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
    driver.maximize_window()
    time.sleep(1)
    driver.get("https://nuxqa.avtest.ink//")
    yield driver
    driver.quit()

@allure.feature('Login y reserva de vuelo')
@allure.story('Iniciar sesión y buscar vuelos desde Colombia a España')
def test_login_UAT1(setup):
    driver = setup
    home_page = HomePage(driver)
    flight_page = FlightPage(driver)
    login_page = LoginPage(driver)
    try:
        with allure.step("Hacer clic en el botón de inicio de sesión"):
            home_page.select_login_button()
        
        with allure.step("Cambiar a la ventana de login"):
            driver.implicitly_wait(2)
            window_handles = driver.window_handles
            driver.switch_to.window(window_handles[-1])

        with allure.step("Rellenar el formulario de inicio de sesión"):
            home_page.fillin_login_form("21734198706","Lifemiles1")
        
        with allure.step("Regresar a la ventana principal"):
            driver.switch_to.window(window_handles[0])

        with allure.step("Configurar idioma y punto de venta"):
            home_page.set_language("Français")
            home_page.set_point_of_sale("France")
        
        with allure.step("Seleccionar detalles del viaje"):
            home_page.set_journey("One way")
            home_page.select_origin("CTG")
            home_page.select_destination("MAD")
            home_page.select_passengers(3,3,3,3)
            home_page.searchFlight()

        with allure.step("Seleccionar precio y tipo de vuelo"):
            flight_page.select_journey_price("One way")
            flight_page.select_flight_type("light")
            flight_page.select_continue()
            result_test('test_login_UAT1','PASS')
    except Exception as e:
        result_test('test_login_UAT1',f'FAIL: {str(e)}')
        raise e
        
    
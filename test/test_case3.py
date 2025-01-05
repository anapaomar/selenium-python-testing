import pytest
import allure
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

    driver.get("https://nuxqa.avtest.ink//")
    yield driver
    driver.quit()

@allure.feature('Login y reserva de vuelo')
@allure.story('Iniciar sesión y buscar vuelos desde Colombia a España')
def test_login_UAT1(setup):
    driver = setup
    homepage = HomePage(driver)
    flightpage = FlightPage(driver)
    loginpage = LoginPage(driver)
    with allure.step("Hacer clic en el botón de inicio de sesión"):
        homepage.select_login_button()
    
    with allure.step("Cambiar a la ventana de login"):
        driver.implicitly_wait(2)
        window_handles = driver.window_handles
        driver.switch_to.window(window_handles[-1])

    with allure.step("Rellenar el formulario de inicio de sesión"):
        loginpage.fillin_login_form("21734198706","Lifemiles1")
        WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
    
    with allure.step("Regresar a la ventana principal"):
        driver.switch_to.window(window_handles[0])

    with allure.step("Configurar idioma y punto de venta"):
        homepage.set_language("Français")
        homepage.set_point_of_sale("France")
    
    with allure.step("Seleccionar detalles del viaje"):
        homepage.set_journey("One way")
        homepage.select_origin("CTG")
        homepage.select_destination("MAD")
        homepage.select_passengers(3,3,3,3)
        homepage.searchFlight()

    with allure.step("Seleccionar precio y tipo de vuelo"):
        flightpage.select_journey_price()
        flightpage.select_flight_type("light")
        flightpage.select_continue()
        
    
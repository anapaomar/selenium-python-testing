import pytest
import allure
import time
from util.db_config import result_test
from util.logger_config import setup_logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from src.pages.home_page import HomePage

@pytest.fixture
def setup():
    logger = setup_logger()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    time.sleep(1)
    url = "https://nuxqa4.avtest.ink/"
    #url = "https://nuxqa5.avtest.ink/"

    logger.info(f"Se probará en el sitio {url}")
    driver.get(url)  

    yield driver #Se pausa la ejecución de esta función para dar paso a la ejecución de los test
    logger.info("Cerrando el navegador")
    driver.quit()

@allure.feature('Selección de idioma')
@allure.story('Cambio diferentes idiomas')
@pytest.mark.parametrize("language, expected_text", [
    ("Español", "Ofertas desde"),
    ("English", "Flight deals from"),
    ("Français", "Offres de vols à partir de"),
    ("Português", "Ofertas de")
])
def test_verificar_cambio_idioma(setup,language,expected_text):
    driver = setup
    home_page = HomePage(driver)
    try:
        with allure.step(f"Seleccionar lenguaje {language}"):
            home_page.set_language(language)

        with allure.step(f"Esperar que cargue la página y validar la existencia del texto {expected_text}"):
            home_page.validate_language(language,expected_text)
            result_test('test_verificar_cambio_idioma','PASS')
    except Exception as e:
        result_test('test_verificar_cambio_idioma',f'FAIL: {str(e)}')
        raise e
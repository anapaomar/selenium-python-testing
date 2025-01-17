import pytest
import allure
from util.db_config import result_test
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from src.pages.home_page import HomePage

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

@allure.feature('Selección de pos')
@allure.story('Cambio diferentes paises')
@pytest.mark.parametrize("country, capital_city", [
    ("Otros países", "AUA"),
    ("España", "MAD"),
    ("Chile", "SCL")
])
def test_verificar_cambio_pos(setup,country,capital_city):
    driver = setup    
    home_page = HomePage(driver)
    try:
        with allure.step(f"Seleccionar pais {country}"):
            home_page.set_point_of_sale(country)

        with allure.step(f"Validar el cambio del pos, en origen debe existir {capital_city}"):
            home_page.validate_pos(capital_city)
            result_test('test_verificar_cambio_pos','PASS')
    except Exception as e:
        result_test('test_verificar_cambio_pos',f'FAIL: {str(e)}')
        raise e
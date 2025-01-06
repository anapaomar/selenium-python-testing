import pytest
import allure
from util.db_config import result_test
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from src.pages.home_page import HomePage
from src.pages.base_page import BasePage
from util.logger_config import setup_logger
#base_url = "https://nuxqa4.avtest.ink/"
base_url = "https://nuxqa5.avtest.ink/"
logger = setup_logger()

@pytest.fixture
def setup():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    time.sleep(1)    
    driver.get(base_url) 
    yield driver
    driver.quit()

@allure.feature('Barra de navegación')
@allure.story('Cambio diferentes opciones dentro del Navbar')
@pytest.mark.parametrize("column_number", [
    (0),
    (1),
    (2),
    (3)
])
def test_footer_redirects(setup,column_number):
    driver = setup    
    home_page = HomePage(driver)
    base_page = BasePage(driver)
    url_site = ""

    try:
        with allure.step(f"Seleccionar columna {column_number} del footer"):
            home_page.set_language("English")
            url_site = home_page.select_option_footer(column_number)

        with allure.step(f"Validar la url {url_site} del sitio y que la página carga correctamente"):
            base_page.validate_current_url(url_site)
            result_test('test_footer_redirects','PASS')
    except Exception as e:
        result_test('test_footer_redirects',f'FAIL: {str(e)}')
        raise e

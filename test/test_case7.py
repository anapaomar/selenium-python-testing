import pytest
import allure
import sqlite3
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
    service = Service(ChromeDriverManager().install())  # WebDriverManager se encarga de gestionar el ChromeDriver
    driver = webdriver.Chrome(service=service)    
    driver.get(base_url) 
    yield driver
    driver.quit()

def result_test(name, result):
    conn = sqlite3.connect('resultados.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO resultados (nombre, resultado)
        VALUES (?, ?)
    ''', (name, result))
    
    conn.commit()
    conn.close()

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
            result_test('header_redirects','PASS')
    except Exception as e:
        result_test('header_redirects',f'FAIL: {str(e)}')
        raise e
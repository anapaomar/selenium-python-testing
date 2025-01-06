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
base_url = "https://nuxqa4.avtest.ink/"
#base_url = "https://nuxqa5.avtest.ink/"
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
@pytest.mark.parametrize("option_nav_bar,url_site, expected_url", [
    ("Ofertas","/pt/ofertas-destinos/novos-voos/", f"pt/ofertas-destinos/novos-voos/"),
    ("Sua reserva","/pt/sua-reserva/personalize-sua-viagem/", f"pt/sua-reserva/personalize-sua-viagem/"),
    ("Informação","/pt/informacao-e-assistencia/taxas-e-tarifas/", f"pt/informacao-e-assistencia/taxas-e-tarifas/")
])
def test_header_redirects(setup,option_nav_bar,url_site,expected_url):
    driver = setup    
    home_page = HomePage(driver)
    base_page = BasePage(driver)
    full_expected_url = f"{base_url}{expected_url}"
    logger.info(f"url_full {full_expected_url}")
    try:
        with allure.step(f"Seleccionar opción {option_nav_bar} del navbar y el sitio {url_site}"):
            home_page.set_language("Português")
            home_page.select_option_nav_bar(option_nav_bar,url_site)

        with allure.step(f"Validar la url {full_expected_url} del sitio y que la página carga correctamente"):
            base_page.validate_current_url(full_expected_url)
            result_test('header_redirects','PASS')
    except Exception as e:
        result_test('header_redirects',f'FAIL: {str(e)}')
        raise e

import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from src.pages.home_page import HomePage


@pytest.fixture
def setup():
    service = Service(ChromeDriverManager().install())  # WebDriverManager se encarga de gestionar el ChromeDriver
    driver = webdriver.Chrome(service=service)
    driver.get("https://nuxqa4.avtest.ink/") 
    #driver.get("https://nuxqa5.avtest.ink/")
    yield driver
    driver.quit()

@allure.feature('Selección de idioma')
@allure.story('Cambio diferentes idiomas')
@pytest.mark.parametrize("language, expected_text", [
    ("Español", "Ofertas desde"),
    ("English", "Flight deals from"),
    ("Français", "Offres de vols à partir de"),
    ("Português", "Ofertas de")
])
def testcase4(setup,language,expected_text):
    driver = setup
    homepage = HomePage(driver)
    with allure.step(f"Seleccionar lenguaje {language}"):
        homepage.set_language(language)

    with allure.step(f"Esperar que cargue la página y validar la existencia del texto {expected_text}"):
        homepage.validate_language(language,expected_text)
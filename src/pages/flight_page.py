from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
import time
import logging
from src.pages.base_page import BasePage 

logger = logging.getLogger(__name__)

class FlightPage:
    """
    Esta clase representa la página de selección de vuelos y contiene métodos
    para interactuar con los elementos de la página relacionados con los precios Y
    tipos de vuelo y la continuación del proceso de compra.
    """
        
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)  
    
    def select_journey_price(self,type):
        """
        Selecciona el primer precio disponible para el viaje.
        Espera hasta que el primer botón de precio sea clickeable y luego hace clic en él.
        """
        wait = WebDriverWait(self.driver, 30)
        #Se selecciona el primer precio que aparezca
        price_button = ""
        self.base_page.wait_while_exist_loading()

        if type == "One way":
            price_button = (By.XPATH,"//button[contains(@class, 'journey_price_button')][1]")
        else:
            price_button = (By.XPATH,"//div[@id='journeysContainerId_1']//button[contains(@class, 'journey_price_button')][1]")

        # Esperar a que el botón de precio sea clickeable
        journey_price_button_element = wait.until(EC.element_to_be_clickable(price_button))
        # Intentar hacer clic en el botón
        journey_price_button_element.click()

    def select_flight_type(self,type):
        """
        Selecciona un tipo de vuelo.

        Parámetros:
        type (str): Tipo de vuelo a seleccionar (ej. "light","classic","flex").
        """
        wait = WebDriverWait(self.driver, 30)
        flight_type = (By.XPATH, f'//span[@class="fare_name" and contains(text(), "{type}")]/ancestor::div[@role="button" and contains(@class,"fare-control")]')
        flight_type_button_element = self.driver.find_element(*flight_type)
        button = wait.until(EC.element_to_be_clickable(flight_type_button_element))
        button.click()
    
    def select_continue(self):
        """
        Espera hasta que el botón 'Continuar' sea visible y clickeable, luego hace clic en él
        para continuar con el proceso.
        """
        wait = WebDriverWait(self.driver, 30)
        self.base_page.wait_while_exist_loading()
        edit_button = (By.CLASS_NAME,"journey-select_modifier-edit_button")
        wait.until(EC.visibility_of_element_located(edit_button))        
        continue_button = (By.XPATH, "//button[contains(@class, 'page_button')]")
        continue_button_element = self.driver.find_element(*continue_button)
        button = wait.until(EC.element_to_be_clickable(continue_button_element))
        button.click()
        self.base_page.wait_while_exist_loading()

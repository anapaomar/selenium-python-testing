from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class FlightPage:
    def __init__(self, driver):
        self.driver = driver  
    
    def select_journey_price(self):
        wait = WebDriverWait(self.driver, 30)
        #Se selecciona el primer precio que aparezca
        price_button = (By.XPATH,"//button[contains(@class, 'journey_price_button')][1]")
        journey_price_button_element = self.driver.find_element(*price_button)
        button = wait.until(EC.element_to_be_clickable(journey_price_button_element))
        button.click()

    def select_flight_type(self,type):
        wait = WebDriverWait(self.driver, 30)
        flight_type = (By.XPATH, f'//span[@class="fare_name" and contains(text(), "{type}")]/ancestor::div[@role="button" and contains(@class,"fare-control")]')
        flight_type_button_element = self.driver.find_element(*flight_type)
        button = wait.until(EC.element_to_be_clickable(flight_type_button_element))
        button.click()
    
    def select_continue(self):
        wait = WebDriverWait(self.driver, 30)
        edit_button = (By.CLASS_NAME,"journey-select_modifier-edit_button")
        wait.until(EC.visibility_of_element_located(edit_button))
        time.sleep(10) #Es la única forma que se me ocurre porque las anteriores no existen para esperar el botón continuar
        continue_button = (By.XPATH, "//button[contains(@class, 'page_button')]")
        continue_button_element = self.driver.find_element(*continue_button)
        button = wait.until(EC.element_to_be_clickable(continue_button_element))
        button.click()
        time.sleep(10)

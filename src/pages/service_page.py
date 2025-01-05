from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ServicePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)  


    def select_continue(self):
        """
        Permite seleccionar el botón continuar
        """        
        continue_button = (By.XPATH, "//button[contains(@class, 'page_button')]")
        continue_button_element = self.driver.find_element(*continue_button)
        button = self.wait.until(EC.element_to_be_clickable(continue_button_element))
        button.click()
        time.sleep(30)#Mala practica, espera el cambio de página
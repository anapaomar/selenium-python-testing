from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from src.pages.base_page import BasePage 
from selenium.webdriver.support import expected_conditions as EC

class ServicePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.wait = WebDriverWait(self.driver, 30)  


    def select_continue(self):
        """
        Permite seleccionar el botón continuar
        """        
        continue_button = (By.XPATH, "//button[contains(@class, 'page_button')]")
        continue_button_element = self.driver.find_element(*continue_button)
        button = self.wait.until(EC.element_to_be_clickable(continue_button_element))
        button.click()
        self.base_page.wait_while_exist_loading()

    def select_service(self,service_type):
        """
        Permite seleccionar un servicio específico y añadir el sevicio a todos los pasajeros
        Parametros:
        service_type (str): Servicio a elegir, por ejemplo "Priority","Lounge","SpecialAssistance","MedicalInsurance"
        """ 
        service_option = (By.XPATH, f"//button[contains(@id, '{service_type}')]")
        service_modal = (By.XPATH, "//div[contains(@class,'modal-service_selector')]")
        add_service_buton = (By.XPATH,"//label[contains(@class,'service_item_button')]")
        confirm_button = (By.XPATH, "//ds-button[contains(@class,'amount-summary_button--action')]") 
        #Clicamos el select para escoger el lenguaje
        service_option_element = self.wait.until(EC.element_to_be_clickable(service_option))
        service_option_element.click()

        self.wait.until(EC.visibility_of_element_located(service_modal))

        add_service_button_list = self.driver.find_elements(*add_service_buton)

        for button in add_service_button_list:
            button.click()

        confirm_button_element = self.driver.find_element(*confirm_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", confirm_button_element)
        confirm_button_element.click()
        self.base_page.wait_while_exist_loading()



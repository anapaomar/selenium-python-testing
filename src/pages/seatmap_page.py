from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.pages.base_page import BasePage 
import time

class SeatmapPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)
        self.wait = WebDriverWait(self.driver, 30)

    def select_seat(self,type):
        passengers_list = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'pax-selector_item')]")

        for passenger in passengers_list:
            time.sleep(15)
            select_passenger_element = passenger.find_element(By.XPATH, ".//button")
            select_passenger_element.click()
            time.sleep(5)
            seats = self.driver.find_elements(By.XPATH, "//li[contains(@class,'seatmap_group--economy')]//button[contains(@class, 'seat') and not(contains(@class, 'unavailable')) and not(contains(@class, 'selected'))]")
            time.sleep(15)
            if seats:
                select_seat = seats[0]
                select_seat.click()
                time.sleep(15)
                print("Asiento seleccionado con éxito")
            else:
                print("No se encontraron asientos disponibles")
        
        button_next_flight = None

        try:
            button_next_flight = self.wait.until(EC.presence_of_element_located((By.XPATH, "//ds-button[contains(@class,'nextflight')]")))
        except:
            button_next_flight = None

        if button_next_flight:
            button_next_flight.click()
            time.sleep(5)
            #volvemos a llamar el método recursivamente
            select_seat(type)
        else:
            button_go_pay = self.wait.until(EC.presence_of_element_located((By.XPATH, "//ds-button[contains(@class,'skipstep')]")))
            button_go_pay.click()

            time.sleep(20)
    
    def select_continue(self):
        """
        Permite seleccionar el botón continuar
        """        
        continue_button = (By.XPATH, "//button[contains(@class, 'page_button')]")
        continue_button_element = self.driver.find_element(*continue_button)
        button = self.wait.until(EC.element_to_be_clickable(continue_button_element))
        button.click()
        self.base_page.wait_while_exist_loading()
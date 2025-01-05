from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

class PassengerPage:
    def __init__(self, driver):
        self.driver = driver

    def fillin_passenger_form(self,passenger_list):
        wait = WebDriverWait(self.driver, 30)
        
        for i, passenger in enumerate(passenger_list):
            passenger_form = (By.XPATH, f"(//div[contains(@class, 'passenger_data_block')])[{i+1}]")
            passenger_form_element = self.driver.find_element(*passenger_form)

            #Gender
            select_gender = passenger_form_element.find_element(By.XPATH, ".//button[contains(@id,'IdPaxGender')]")
            select_gender.click()
            gender_option = passenger_form_element.find_element(By.XPATH, f".//span[contains(text(),\"{passenger['gender']}\")]")
            gender_option.click()

            #name
            field_name = passenger_form_element.find_element(By.XPATH, ".//input[contains(@id,'IdFirstName')]")
            field_name.clear()
            field_name.send_keys(passenger['name'])

            #lastname
            field_name = passenger_form_element.find_element(By.XPATH, ".//input[contains(@id,'IdLastName')]")
            field_name.clear()
            field_name.send_keys(passenger['lastname'])

            #birthday
            #day
            select_day = passenger_form_element.find_element(By.XPATH, ".//button[@role='combobox' and contains(@id,'dateDayId')]")
            select_day.click()

            birth_day = passenger_form_element.find_element(By.XPATH, ".//button[@role='option' and contains(@id,'dateDayId')][1]")
            birth_day.click()
            #month
            select_month = passenger_form_element.find_element(By.XPATH, ".//button[@role='combobox' and contains(@id,'dateMonthId')]")
            select_month.click()

            birth_month = passenger_form_element.find_element(By.XPATH, ".//button[@role='option' and contains(@id,'dateMonthId')][1]")
            birth_month.click() 
            #year
            select_year = passenger_form_element.find_element(By.XPATH, ".//button[@role='combobox' and contains(@id,'dateYearId')]")
            select_year.click()

            birth_year = passenger_form_element.find_element(By.XPATH, ".//button[@role='option' and contains(@id,'dateYearId')][1]")
            birth_year.click()

            #nacionality
            select_nacionality = passenger_form_element.find_element(By.XPATH, ".//button[@role='combobox' and contains(@id,'IdDocNationality')]")
            select_nacionality.click()

            option_nacionality = passenger_form_element.find_element(By.XPATH, ".//button[@role='option' and contains(@id,'IdDocNationality')][1]")
            option_nacionality.click()

            #customer_program. Aqui se valida si existe el campo, de lo conrtario se maneja la excepción
            try:
                select_customer_program = passenger_form_element.find_element(By.XPATH, ".//button[@id='customerPrograms']")
                select_customer_program.click()

                option_customer_program = passenger_form_element.find_element(By.XPATH, ".//ul[@id='listId_customerPrograms']//button[@class='ui-dropdown_item_option'][1]")
                option_customer_program.click()
            except NoSuchElementException:
                # Si el campo no existe, no hacemos nada o lo dejamos en blanco
                print("El campo 'Programa de viajero frecuente' no está presente en este formulario.")

    def fillin_reservation_holder(self,prefix,phone_number,email):
        contact_data = (By.CLASS_NAME, "contact_data")
        contact_data_element = self.driver.find_element(*contact_data)

        select_prefix_number = contact_data_element.find_element(By.ID,"phone_prefixPhoneId")
        select_prefix_number.click()
        
        option_prefix_number = contact_data_element.find_element(By.XPATH, f".//button[@role='option' and contains(@id,'phone_prefixPhoneId')]//span[contains(text(), '{prefix}')]")
        option_prefix_number.click()
        field_phone_number = contact_data_element.find_element(By.ID,"phone_phoneNumberId")
        field_phone_number.send_keys(phone_number)

        field_email = contact_data_element.find_element(By.ID,"email")
        field_email.send_keys(email)

        try:
            field_confirm_email = contact_data_element.find_element(By.ID,"confirmEmail")
            field_confirm_email.send_keys(email)
        except NoSuchElementException:
                # Si el campo no existe, no hacemos nada o lo dejamos en blanco
                print("El campo 'confirmación de email' no está presente en este formulario.")
    
    def select_continue(self):
        wait = WebDriverWait(self.driver, 30)
        continue_button = (By.XPATH, "//button[contains(@class, 'page_button')]")
        continue_button_element = self.driver.find_element(*continue_button)
        button = wait.until(EC.element_to_be_clickable(continue_button_element))
        button.click()
        time.sleep(50)

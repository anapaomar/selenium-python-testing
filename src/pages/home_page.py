from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver   
    
    def set_language(self,language):
        wait = WebDriverWait(self.driver, 30)
        self.language_select = (By.XPATH, "//*[starts-with(@id, 'languageListTriggerId_')]")
        language_select_element = self.driver.find_element(*self.language_select)
        select = wait.until(EC.element_to_be_clickable(language_select_element))
        select.click()
       
        self.language_button = (By.XPATH, f'//span[@class="button_label" and contains(text(), "{language}")]/parent::button')
        language_button_element = self.driver.find_element(*self.language_button)
        button = wait.until(EC.element_to_be_clickable(language_button_element))
        button.click()

    def set_point_of_sale(self,country):
        wait = WebDriverWait(self.driver, 30)
        self.pos_select = (By.ID, "pointOfSaleSelectorId")
        pos_select_element = self.driver.find_element(*self.pos_select)
        pos_select_option = wait.until(EC.element_to_be_clickable(pos_select_element))
        pos_select_option.click()
       
        self.pos_button = (By.XPATH, f'//span[@class="points-of-sale_list_item_label" and contains(text(), "{country}")]/parent::button')
        pos_button_element = self.driver.find_element(*self.pos_button)
        pos_option = wait.until(EC.element_to_be_clickable(pos_button_element))
        pos_option.click()

        self.apply_pos_button = (By.XPATH,"//button[contains(@class,'points-of-sale_footer_action_button')]")
        apply_pos_button_element = self.driver.find_element(*self.apply_pos_button)
        apply_button = wait.until(EC.element_to_be_clickable(apply_pos_button_element))
        apply_button.click()
    
    def set_journey(self,type):
        wait = WebDriverWait(self.driver, 10)
        # Comprobamos el tipo de viaje y asignamos el ID correspondiente
        if "Round" in type:
            print(f"Entra a Round")
            option = 'journeytypeId_0'
        elif "One way" in type:
            print(f"Entra a One way")
            option = 'journeytypeId_1'
        else:
            raise ValueError(f"Tipo de viaje desconocido: {type}")

        try:
            # Encontramos el elemento
            
            self.journey_type_combo = (By.XPATH, f"//label[@for='{option}']")
            journey_type_element = self.driver.find_element(*self.journey_type_combo)
            
            if not journey_type_element.is_displayed():
                print(f"El elemento con ID {option} no está visible.")
            elif not journey_type_element.is_enabled():
                print(f"El elemento con ID {option} está deshabilitado.")
            else:
                # Esperamos hasta que el elemento esté clickeable
                combo = wait.until(EC.element_to_be_clickable(journey_type_element))
        
                # Hacemos clic en el combo
                combo.click()

                # Esperamos un poco si es necesario para que la UI se actualice
            

                print(f"Tipo de viaje '{type}' seleccionado correctamente.")

        except Exception as e:
            print(f"Error al intentar seleccionar el tipo de viaje '{type}': {e}")

    def select_origin(self,key_city):
        wait = WebDriverWait(self.driver, 10)

        self.origin_city1 = (By.XPATH,"//div[@id='originDiv']")
        origin_element1 = self.driver.find_element(*self.origin_city1)
        origin_text1 = wait.until(EC.element_to_be_clickable(origin_element1))
        origin_text1.click()

        self.origin_city = (By.XPATH,"//div[@id='originDiv']//input[@class='control_field_input']")
        origin_element = self.driver.find_element(*self.origin_city)
        origin_text = wait.until(EC.element_to_be_clickable(origin_element))
        origin_text.clear()
        origin_text.send_keys(key_city) 

        self.specific_city = (By.ID,f"{key_city}")
        specific_city_element = self.driver.find_element(*self.specific_city)
        city = wait.until(EC.element_to_be_clickable(specific_city_element))
        city.click()


    def select_destination(self,key_city):
            wait = WebDriverWait(self.driver, 10)
            self.origin_city = (By.XPATH,"//div[@id='arrivalStationInputLabel']/following-sibling::input[@class='control_field_input']")
            origin_element = self.driver.find_element(*self.origin_city)
            origin_text = wait.until(EC.element_to_be_clickable(origin_element))
            origin_text.send_keys({key_city})

            self.specific_city = (By.ID,f"{key_city}")
            specific_city_element = self.driver.find_element(*self.specific_city)
            city = wait.until(EC.element_to_be_clickable(specific_city_element))
            city.click()
            

    def select_passengers(self,number_adult,number_teen,number_child,number_infant):
        wait = WebDriverWait(self.driver, 10) 
        #"//div[@id='originDiv']//input[@class='control_field_input']"
        self.select_passenger = (By.XPATH,"//div[@class='pax-control']//button[@class='control_field_button']")
        passenger_element = self.driver.find_element(*self.select_passenger)
        select = wait.until(EC.element_to_be_clickable(passenger_element))
        select.click()

        if number_adult > 1:
            print("Entra a adultos")
            self.button_plus_adult = (By.XPATH, "//input[@id='inputPax_ADT']/following::button[@class='ui-num-ud_button plus']")
            button_plus_adult_element = self.driver.find_element(*self.button_plus_adult)
            button__plus_adult_number = wait.until(EC.element_to_be_clickable(button_plus_adult_element))
            for _ in range(number_adult - 1):
                button__plus_adult_number.click()
                time.sleep(1)

            self.input_adult = (By.XPATH,"//input[@id='inputPax_ADT']")
            input_adult_element = self.driver.find_element(*self.input_adult)
            input_adult_number = wait.until(EC.element_to_be_clickable(input_adult_element)) 
            input_adult_value = input_adult_number.get_attribute("value")
            assert int(input_adult_value) == int(number_adult), f"El valor para adulto es incorrecto, se esperaba {number_adult}"
        
        else:
            print("No se definen adultos para este test")

        if number_teen > 0:
            print("Entra a teen")
            self.button_plus_teen = (By.XPATH, "//input[@id='inputPax_TNG']/following::button[@class='ui-num-ud_button plus']")
            button_plus_teen_element = self.driver.find_element(*self.button_plus_teen)
            button__plus_teen_number = wait.until(EC.element_to_be_clickable(button_plus_teen_element))
            for _ in range(number_teen):
                button__plus_teen_number.click()
                time.sleep(1)

            self.input_teen = (By.XPATH,"//input[@id='inputPax_TNG']")
            input_teen_element = self.driver.find_element(*self.input_teen)
            input_teen_number = wait.until(EC.element_to_be_clickable(input_teen_element)) 
            input_teen_value = input_teen_number.get_attribute("value")
            assert int(input_teen_value) == int(number_teen), f"El valor joven es incorrecto, se esperaba {number_teen}"
        
        else:
            print("No se definen jovenes para este test")

        if number_child > 0:
            print("Entra a child")
            self.button_plus_child = (By.XPATH, "//input[@id='inputPax_CHD']/following::button[@class='ui-num-ud_button plus']")
            button_plus_child_element = self.driver.find_element(*self.button_plus_child)
            button__plus_child_number = wait.until(EC.element_to_be_clickable(button_plus_child_element))
            for _ in range(number_child):
                button__plus_child_number.click()
                time.sleep(1)

            self.input_child = (By.XPATH,"//input[@id='inputPax_CHD']")
            input_child_element = self.driver.find_element(*self.input_child)
            input_child_number = wait.until(EC.element_to_be_clickable(input_child_element)) 
            input_child_value = input_child_number.get_attribute("value")
            assert int(input_child_value) == int(number_child), f"El valor niño es incorrecto, se esperaba {number_child}"
        
        else:
            print("No se definen niños para este test")

        if number_infant > 0:
            print("Entra a infant")
            self.button_plus_infant = (By.XPATH, "//input[@id='inputPax_INF']/following::button[@class='ui-num-ud_button plus']")
            button_plus_infant_element = self.driver.find_element(*self.button_plus_infant)
            button__plus_infant_number = wait.until(EC.element_to_be_clickable(button_plus_infant_element))
            for _ in range(number_infant):
                button__plus_infant_number.click()
                time.sleep(1)

            self.input_infant = (By.XPATH,"//input[@id='inputPax_INF']")
            input_infant_element = self.driver.find_element(*self.input_infant)
            input_infant_number = wait.until(EC.element_to_be_clickable(input_infant_element)) 
            input_infant_value = input_infant_number.get_attribute("value")
            assert int(input_infant_value) == int(number_infant), f"El valor infante es incorrecto, se esperaba {number_infant}"
        
        else:
            print("No se definen niños para este test")

        self.button_confirm = (By.XPATH,"//div[@id='paxControlSearchId']//button[@class='button control_options_selector_action_button']")
        button_confirm_element = self.driver.find_element(*self.button_confirm)
        button = wait.until(EC.element_to_be_clickable(button_confirm_element)) 
        button.click()
        
    def searchFlight(self):
        wait = WebDriverWait(self.driver, 10) 
        self.button_search = (By.ID,"searchButton")
        button_search_element = self.driver.find_element(*self.button_search)
        button = wait.until(EC.element_to_be_clickable(button_search_element)) 
        button.click()
        time.sleep(10)

    def select_login_button(self):
        wait = WebDriverWait(self.driver, 30)
        self.login_button = (By.ID, "auth-component")
        login_button_element = self.driver.find_element(*self.login_button)
        button = wait.until(EC.element_to_be_clickable(login_button_element))
        button.click()

    def validate_language(self,language,expected_text):
        title_div_text = (By.XPATH, "//div[@class='routes-lowest-price-header_title_text']//h2")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(title_div_text))    
        title_div_text_element = self.driver.find_element(*title_div_text)

        language_selected_element = self.driver.find_element(By.XPATH, "//*[starts-with(@id, 'languageListTriggerId_')]")
        aria_label_value = language_selected_element.get_attribute("aria-label")
            
        assert title_div_text_element.text == expected_text, f"Se esperaba '{expected_text}', pero se encontró '{title_div_text_element.text}'"
        assert language in aria_label_value, f"Se esperaba que '{aria_label_value}' contuviera el idioma '{language}', pero no fue así."

        print(f"Correcta validación del idioma {language}")

    def validate_pos(self,capital_city):
        origin_button_code = (By.XPATH, "//button[@id='originBtn']//span[contains(@class,'ontrol_value-station-code')]")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(origin_button_code)) 
        origin_button_code_element = self.driver.find_element(*origin_button_code)

        assert capital_city in origin_button_code_element.text, f"Se esperaba '{expected_text}', pero se encontró '{origin_button_code_element.text}'"

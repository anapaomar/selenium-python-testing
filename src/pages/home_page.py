from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from util.logger_config import setup_logger

class HomePage:
    """
    Esta clase representa la página principal del sitio de reservas de vuelos.
    """
    def __init__(self, driver):
        self.driver = driver   
        self.logger = setup_logger()
        self.wait = WebDriverWait(self.driver, 30)
    
    def set_language(self,language):
        """
        Establece el idioma de la página seleccionando el idioma especificado.

        Parámetros:
        language (str): El idioma que se desea establecer (por ejemplo, "Español").
        """
        language_select = (By.XPATH, "//*[starts-with(@id, 'languageListTriggerId_')]")
        language_button = (By.XPATH, f'//span[@class="button_label" and contains(text(), "{language}")]/parent::button')
        #Clicamos el select para escoger el lenguaje
        language_select_element = self.wait.until(EC.element_to_be_clickable(language_select))
        language_select_element.click()
        #Seleccionamos el lenguaje
        language_button_element = self.wait.until(EC.element_to_be_clickable(language_button))
        language_button_element.click()

    def set_point_of_sale(self,country):
        """
        Establece el POS especificado.

        Parámetros:
        country (str): El país o región a seleccionar.
        """
        pos_select = (By.ID, "pointOfSaleSelectorId")
        pos_button = (By.XPATH, f'//span[@class="points-of-sale_list_item_label" and contains(text(), "{country}")]/parent::button')
        apply_pos_button = (By.XPATH,"//button[contains(@class,'points-of-sale_footer_action_button')]")
        #Clicamos en el elemento para escoger el pos
        pos_select_element = self.wait.until(EC.element_to_be_clickable(pos_select))
        pos_select_element.click()
        #Seleccionamos el pais
        pos_button_element = self.wait.until(EC.element_to_be_clickable(pos_button))
        pos_button_element.click()
        #Aplicamos los cambios        
        apply_pos_button_element = self.wait.until(EC.element_to_be_clickable(apply_pos_button))
        apply_pos_button_element.click()
    
    def set_journey(self,type):
        """
        Establece el tipo de viaje (ida y vuelta o solo ida).

        Parámetros:
        type (str): El tipo de viaje (por ejemplo, "Round" para ida y vuelta o "One way" para solo ida).
        """
        # Comprobamos el tipo de viaje y asignamos el ID correspondiente
        if "Round" in type:
            self.logger.info(f"Entra a Round")
            option = 'journeytypeId_0'
        elif "One way" in type:
            self.logger.info(f"Entra a One way")
            option = 'journeytypeId_1'
        else:
            raise ValueError(f"Tipo de viaje desconocido: {type}")

        try:#Buscamos el elemento label por su atributo for, haciendo uso del id obtenido anteriormente            
            journey_type_combo = (By.XPATH, f"//label[@for='{option}']")
            journey_type_element = self.driver.find_element(*journey_type_combo)
            
            if not journey_type_element.is_displayed():
                self.logger.info(f"El elemento con ID {option} no está visible.")
            elif not journey_type_element.is_enabled():
                self.logger.info(f"El elemento con ID {option} está deshabilitado.")
            else:
                # Esperamos hasta que el elemento esté clickeable
                combo = self.wait.until(EC.element_to_be_clickable(journey_type_element))
                combo.click()      
                self.logger.info(f"Tipo de viaje '{type}' seleccionado correctamente.")
        except Exception as e:
            self.logger.error(f"Error al intentar seleccionar el tipo de viaje '{type}': {e}")

    def select_origin(self,key_city):
        """
        Selecciona la ciudad de origen para el viaje.

        Parámetros:
        key_city (str): La ciudad de origen que se desea seleccionar.
        """
        origin_div = (By.XPATH,"//div[@id='originDiv']")
        origin_input = (By.XPATH,"//div[@id='originDiv']//input[@class='control_field_input']")
        specific_city = (By.ID,f"{key_city}")

        #Dado que por defecto se tiene seleccionada una ciudad, para poder editar hay que dar clic previamente al div que contiene el input
        origin_div_element = self.wait.until(EC.element_to_be_clickable(origin_div))
        origin_div_element.click()

        #Ahora sí digitamos el valor del origen que queremos        
        origin_input_element = self.wait.until(EC.element_to_be_clickable(origin_input))
        origin_input_element.clear()
        origin_input_element.send_keys(key_city) 

        #Seleccionamos la ciudad origen        
        specific_city_element = self.wait.until(EC.element_to_be_clickable(specific_city))
        specific_city_element.click()


    def select_destination(self,key_city): 
            """
            Selecciona la ciudad de destino para el viaje.

            Parámetros:
            key_city (str): La ciudad de destino  que se desea seleccionar.
            """          
            destination_city = (By.XPATH,"//div[@id='arrivalStationInputLabel']/following-sibling::input[@class='control_field_input']")            
            specific_city = (By.ID,f"{key_city}")
            #digitamos el valor del destino
            destination_city_element = self.wait.until(EC.element_to_be_clickable(destination_city))
            destination_city_element.send_keys({key_city})
            #Seleccionamos la ciudad destino            
            specific_city_element = self.wait.until(EC.element_to_be_clickable(specific_city))
            specific_city_element.click()
            

    def select_passengers(self,number_adult,number_teen,number_child,number_infant):
        """
        Establece la cantidad de pasajeros (adultos, niños, etc.)

        Parámetros:
        number_adult (int): Cantidad de adultos a seleccionar
        number_teen (int): Cantidad de jóvenes a seleccionar
        number_child (int): Cantidad de niños a seleccionar
        number_infant (int): Cantidad de infantes a seleccionar
        """
        select_passenger = (By.XPATH,"//div[@class='pax-control']//button[@class='control_field_button']")
        button_plus_adult = (By.XPATH, "//input[@id='inputPax_ADT']/following::button[@class='ui-num-ud_button plus']")
        button_plus_teen = (By.XPATH, "//input[@id='inputPax_TNG']/following::button[@class='ui-num-ud_button plus']")
        button_plus_child = (By.XPATH, "//input[@id='inputPax_CHD']/following::button[@class='ui-num-ud_button plus']")
        button_plus_infant = (By.XPATH, "//input[@id='inputPax_INF']/following::button[@class='ui-num-ud_button plus']")
        input_adult = (By.XPATH,"//input[@id='inputPax_ADT']")        
        input_teen = (By.XPATH,"//input[@id='inputPax_TNG']")        
        input_child = (By.XPATH,"//input[@id='inputPax_CHD']")        
        input_infant = (By.XPATH,"//input[@id='inputPax_INF']")
        button_confirm = (By.XPATH,"//div[@id='paxControlSearchId']//button[@class='button control_options_selector_action_button']")
        #Clicamos en el elemento para escoger la cantidad de pasajeros
        passenger_element = self.wait.until(EC.element_to_be_clickable(select_passenger))
        passenger_element.click()
        #Validamos si el numero de adultos es mayor a 1 ya que por defecto se tiene seleccionado un adulto
        if number_adult > 1:
            self.logger.info(f"Se seleccionaran {number_adult} adultos")           
            button_plus_adult_element = self.wait.until(EC.element_to_be_clickable(button_plus_adult))
            for _ in range(number_adult - 1):
                button_plus_adult_element.click()
                time.sleep(1)
            #Se valida que se hayan seleccionado la cantidad correcta
            input_adult_element = self.wait.until(EC.element_to_be_clickable(input_adult)) 
            input_adult_value = input_adult_element.get_attribute("value")
            assert int(input_adult_value) == int(number_adult), f"El valor para adulto es incorrecto, se esperaba {number_adult}"        
        else:
            self.logger.info("No se definen adultos para este test")
        #Validamos si el numero de jóvenes es mayor a 0
        if number_teen > 0:
            self.logger.info(f"Se seleccionaran {number_teen} jóvenes")             
            button_plus_teen_element = self.wait.until(EC.element_to_be_clickable(button_plus_teen))
            for _ in range(number_teen):
                button_plus_teen_element.click()
                time.sleep(1)
            input_teen_element = self.wait.until(EC.element_to_be_clickable(input_teen)) 
            input_teen_value = input_teen_element.get_attribute("value")
            assert int(input_teen_value) == int(number_teen), f"El valor joven es incorrecto, se esperaba {number_teen}"        
        else:
            self.logger.info("No se definen jóvenes para este test")

        if number_child > 0:
            self.logger.info(f"Se seleccionaran {number_child} niños")
            button_plus_child_element = self.wait.until(EC.element_to_be_clickable(button_plus_child))
            for _ in range(number_child):
                button_plus_child_element.click()
                time.sleep(1)            
            input_child_element = self.wait.until(EC.element_to_be_clickable(input_child)) 
            input_child_value = input_child_element.get_attribute("value")
            assert int(input_child_value) == int(number_child), f"El valor niño es incorrecto, se esperaba {number_child}"        
        else:
            self.logger.info("No se definen niños para este test")

        if number_infant > 0:
            self.logger.info(f"Se seleccionaran {number_infant} infantes")            
            button_plus_infant_element = self.wait.until(EC.element_to_be_clickable(button_plus_infant))
            for _ in range(number_infant):
                button_plus_infant_element.click()
                time.sleep(1)
            input_infant_element = self.wait.until(EC.element_to_be_clickable(input_infant)) 
            input_infant_value = input_infant_element.get_attribute("value")
            assert int(input_infant_value) == int(number_infant), f"El valor infante es incorrecto, se esperaba {number_infant}"        
        else:
            self.logger.info("No se definen infantes para este test")
        
        #Se confirma la asignación de cantidad de pasajeros
        button_confirm_element = self.wait.until(EC.element_to_be_clickable(button_confirm)) 
        button_confirm_element.click()
        
    def searchFlight(self):
        """
        Realiza la búsqueda de vuelos haciendo clic en el botón buscar.
        """
        button_search = (By.ID,"searchButton")
        button_search_element = self.wait.until(EC.element_to_be_clickable(button_search)) 
        button_search_element.click()
        time.sleep(10)#Se hace una espera por el cambio de página. Esto es una mala practica

    def select_login_button(self):
        """
        Inicia el proceso de inicio de sesión.
        """
        login_button = (By.ID, "auth-component")
        login_button_element = self.wait.until(EC.element_to_be_clickable(login_button))
        login_button_element.click()

    def validate_language(self,language,expected_text):
        """
        Valida que el idioma seleccionado se haya aplicado correctamente.

        Parámetros:
        language (str): El idioma seleccionado.
        expected_text (str): El texto esperado en el idioma seleccionado.
        """
        title_div_text = (By.XPATH, "//div[@class='routes-lowest-price-header_title_text']//h2")
        title_div_text_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(title_div_text))    
        language_selected_element = self.driver.find_element(By.XPATH, "//*[starts-with(@id, 'languageListTriggerId_')]")
        aria_label_value = language_selected_element.get_attribute("aria-label")
            
        assert title_div_text_element.text == expected_text, f"Se esperaba '{expected_text}', pero se encontró '{title_div_text_element.text}'"
        assert language in aria_label_value, f"Se esperaba que '{aria_label_value}' contuviera el idioma '{language}', pero no fue así."

        self.logger.info(f"Correcta validación del idioma {language}")

    def validate_pos(self,capital_city):
        """
        Valida que el punto de venta esté seleccionado
        """
        origin_button_code = (By.XPATH, "//button[@id='originBtn']//span[contains(@class,'ontrol_value-station-code')]")
        origin_button_code_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(origin_button_code)) 
        
        assert capital_city in origin_button_code_element.text, f"Se esperaba '{capital_city}', pero se encontró '{origin_button_code_element.text}'"

    def select_option_nav_bar(self,option,url_submenu):
        """
        Permite seleccionar opciones de la barra de navegación del header

        Parametros:
        option (str): se refiere a la opción del menú de la barra de navegación
        url_submenu (str): se refiere a la opción del sub menú a elegir dentro de las opciones de cada menu
        """
        main_navegation_bar = (By.XPATH, "//nav[@class='main-header_nav-primary_nav']")
        option_nav_bar_button = (By.XPATH, f"//span[contains(text(),'{option.strip()}')]")
        submenu_option = (By.XPATH, f'//a[@href="{url_submenu}"]')

        self.wait.until(EC.element_to_be_clickable(main_navegation_bar))
        #Se selecciona la opción enviada por parámetro
        option_nav_bar_button_element = self.wait.until(EC.element_to_be_clickable(option_nav_bar_button))
        option_nav_bar_button_element.click()

        self.logger.info(f"Se accede a la opción {option}")
        #Se selecciona el submenú indicado        
        submenu_option = (By.XPATH, f'//a[@href="{url_submenu}"]')       
        submenu_option_element = self.wait.until(EC.element_to_be_clickable(submenu_option))
        submenu_option_element.click()

        self.logger.info(f"Se accede a la opción {url_submenu}")


    def select_option_footer(self,num_column):
        """
        Permite seleccionar opciones de la barra de navegación del footer

        Parametros:
        num_column (int): como existen 4 columnas en el footer, se va a tomar un link de cada columna cuyo número llegue por parámetro
        """
        items_column_list = self.driver.find_elements(By.XPATH, f"//ul[@id='footerNavListId-{num_column}']/li")
        href = ""
        
        for item_column in items_column_list:
            # Verifica si el <span> con clase 'icon-external' está presente. Esto lo hago porque se deben tratar diferentes los que abren otra pesa de los que no.
            external_icon = item_column.find_elements(By.XPATH, ".//span[contains(@class, 'icon-external')]")
        
            # Si no tiene el <span> con clase 'icon-external', hacer clic en el <a> y obtener el href
            if not external_icon:
                link = item_column.find_element(By.TAG_NAME, "a")
                href = link.get_attribute("href")#Se obtiene el href para validar
                self.logger.info(f"En la columna número {num_column}, se da click en el enlace con href: {href}")
                link.click()
                break #Solo se da clic en el primer elemento. Como es una lista, se rompe el ciclo para que no siga validando

        return href
       
      

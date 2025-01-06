from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from util.logger_config import setup_logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver   
        self.logger = setup_logger()
        self.wait = WebDriverWait(self.driver, 30)

    def validate_current_url(self,expected_url):
        self.wait.until(EC.url_to_be(expected_url))
        current_url = self.driver.current_url
        self.logger.info(f"La url actual es {current_url}")

        assert current_url == expected_url, f"Se esperaba '{expected_url}', pero se encontró '{current_url}'"


    def wait_while_exist_loading(self):
        max_wait_time=30
        check_interval=1

        start_time = time.time()  # Guardamos el tiempo de inicio

        while True:
            elapsed_time = time.time() - start_time  # Calculamos el tiempo transcurrido

            if elapsed_time > max_wait_time:  # Si el tiempo máximo ha pasado, rompemos el ciclo
                print(f"Tiempo máximo de espera alcanzado ({max_wait_time} segundos).")
                break

            try:
                # Esperar hasta que el div con la clase 'loading' no esté visible
                loading_element = self.driver.find_element(By.CLASS_NAME, "loading")
                if not loading_element.is_displayed():  # Si ya no está visible
                    print("El cargador ha desaparecido.")
                    break
                else:
                    print("Cargando... avioncito volando.")
                    
            except Exception as e:
                # Si no se encuentra el elemento o alguna otra excepción, consideramos que se ha completado la carga
                print(f"No se encontró el elemento de carga.")
                break
            
            time.sleep(check_interval) 
    
        
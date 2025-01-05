from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def fillin_login_form(self,username,password): 
            """
            Este método rellena los campos de nombre de usuario y contraseña y luego hace clic en el botón de confirmación.
            
            Parámetros:
            username: Nombre de usuario para iniciar sesión
            password: Contraseña para iniciar sesión
            """         
            username_field = (By.ID,"u-username")
            username_field_element = self.wait.until(EC.element_to_be_clickable(username_field))
            username_field_element.send_keys(username)

            password_field = (By.ID,"u-password")
            pass_field_element = self.wait.until(EC.element_to_be_clickable(password_field))
            pass_field_element.send_keys(password)

            confirm_button = (By.ID, "Login-confirm")
            confirm_button_element = self.wait.until(EC.element_to_be_clickable(confirm_button))
            confirm_button_element.click()
            time.sleep(5)            
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def fillin_login_form(self,username,password):
           #auth-component
            wait = WebDriverWait(self.driver, 30)
            
            self.username_field = (By.ID,"u-username")
            wait.until(EC.element_to_be_clickable(self.username_field))
            username_field_element = self.driver.find_element(*self.username_field)
            username_field_element.send_keys(username)

            self.password_field = (By.ID,"u-password")
            password_field_element = self.driver.find_element(*self.password_field)
            pass_field = wait.until(EC.element_to_be_clickable(password_field_element))
            pass_field.send_keys(password)

            self.confirm_button = (By.ID, "Login-confirm")
            confirm_button_element = self.driver.find_element(*self.confirm_button)
            confirm = wait.until(EC.element_to_be_clickable(confirm_button_element))
            confirm.click()            
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
        #self.wait.until(EC.url_to_be(expected_url))
        time.sleep(5)
        current_url = self.driver.current_url
        self.logger.info(f"La url actual es {current_url}")

        assert current_url == expected_url, f"Se esperaba '{expected_url}', pero se encontró '{current_url}'"
        
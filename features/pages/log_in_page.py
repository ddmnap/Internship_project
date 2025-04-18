from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class LoginPage(BasePage):
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD_FIELD = (By.ID, 'field')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "a[wized='loginButton']")

    def log_in(self, email, password):
        logging.info("Waiting for email input field...")
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.EMAIL_FIELD)
        )

        logging.info("Entering email...")
        self.input_text(self.EMAIL_FIELD, email)

        logging.info("Entering password...")
        self.input_text(self.PASSWORD_FIELD, password)

        logging.info("Clicking login button...")
        self.click(self.LOGIN_BUTTON)

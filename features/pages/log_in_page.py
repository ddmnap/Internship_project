from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
class LoginPage(BasePage):
    EMAIL_FIELD = (By.ID, "email-2")
    PASSWORD_FIELD = (By.ID, "field")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".login-button")
    def log_in(self, email, password):
        self.input_text(self.EMAIL_FIELD, email)
        self.input_text(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)



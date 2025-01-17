from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class PasswordPage(BasePage):
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".submit-button-2")
    PASSWORD_FORM = (By.CSS_SELECTOR, ".w-form")


    def click_change_password(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CHANGE_PASSWORD_BUTTON))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CHANGE_PASSWORD_BUTTON)).click()


    def is_password_form_displayed(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.PASSWORD_FORM)
        )
        return self.find_element(self.PASSWORD_FORM).is_displayed()

    def is_change_password_button_enabled(self):
        return self.find_element(self.CHANGE_PASSWORD_BUTTON).is_enabled()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

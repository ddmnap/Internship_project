from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".login-button")
    SETTINGS_BUTTON = (By.CSS_SELECTOR, "a[href='/settings']")
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "a[href='/set-new-password']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_main_page(self):
        self.driver.get("https://soft.reelly.io")

    def click_sign_in(self):
        self.click(self.SIGN_IN_BUTTON)

    def click_settings(self):
        self.click(self.SETTINGS_BUTTON)

    def click_change_password(self):
        self.click(self.CHANGE_PASSWORD_BUTTON)

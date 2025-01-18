from selenium.webdriver.common.by import By
from .base_page import BasePage
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class MainPage(BasePage):
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".login-button")
    SETTINGS_BUTTON = (By.XPATH, "//div[@class='menu-button-text' and text()='Settings']")
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "a[href='/set-new-password']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_main_page(self):
        self.driver.get("https://soft.reelly.io")

    def click_sign_in(self):
        self.click(self.SIGN_IN_BUTTON)

    def click_settings(self):
        logging.info("Waiting for the settings button to be clickable...")
        locator = self.SETTINGS_BUTTON
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator)
        ).click()
        logging.info("Settings button clicked successfully.")

    def click_change_password(self):
        self.click(self.CHANGE_PASSWORD_BUTTON)

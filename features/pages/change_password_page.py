from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import logging


class PasswordPage(BasePage):
    CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".submit-button-2")
    # PASSWORD_FORM = (By.CSS_SELECTOR, ".w-form")
    PASSWORD_FORM = (By.CSS_SELECTOR, "a[wized='changePasswordButton']")



    def click_change_password(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CHANGE_PASSWORD_BUTTON))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CHANGE_PASSWORD_BUTTON)).click()


    def is_password_form_displayed(self):
        WebDriverWait(self.driver, 15).until(
            EC.visibility_of_element_located(self.PASSWORD_FORM)
        )
        return self.find_element(self.PASSWORD_FORM).is_displayed()

    def is_change_password_button_enabled(self):
        logging.info("Scrolling to the bottom of the page before checking the Change Password button...")

        # Scroll to the bottom
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)  # Wait for the UI to update

        logging.info("Checking if the Change Password button exists...")

        elements = self.driver.find_elements(*self.CHANGE_PASSWORD_BUTTON)
        if not elements:
            logging.error("Change password button NOT FOUND!")
            self.driver.save_screenshot("debug_change_password_button.png")  # Save a screenshot for debugging
            return False  # Fail gracefully if button is not found

        logging.info(f"Found {len(elements)} elements for CHANGE_PASSWORD_BUTTON.")

        logging.info("Waiting for the Change Password button to be visible...")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CHANGE_PASSWORD_BUTTON)

        )

        return elements[0].is_enabled()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

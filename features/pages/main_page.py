from selenium.webdriver.common.by import By
from .base_page import BasePage
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions
from time import sleep


class MainPage(BasePage):
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".login-button")
    # SETTINGS_BUTTON = (By.XPATH, "//div[@class='menu-button-text' and text()='Settings']")  # Web only
    # CHANGE_PASSWORD_BUTTON = (By.CSS_SELECTOR, "a[href='/set-new-password']")  # Web only

    # Mobile-specific elements
    ASSISTANT_BUTTON = (By.CSS_SELECTOR, ".assistant-button.w-inline-block")
    MOBILE_CHANGE_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/set-new-password']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_main_page(self):
        self.driver.get("https://soft.reelly.io")

    def click_sign_in(self):
        self.click(self.SIGN_IN_BUTTON)

    def click_assistant_button(self):
        logging.info("Waiting for the Assistant button to be clickable on mobile...")
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.ASSISTANT_BUTTON)
        ).click()
        logging.info("Assistant button clicked successfully.")

    def scroll_and_click_change_password(self):
        logging.info("Scrolling to the bottom of the page on mobile...")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)  # Wait for elements to load

        logging.info("Ensuring the change password link is visible...")
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.MOBILE_CHANGE_PASSWORD_LINK)
        )

        logging.info("Scrolling precisely to the change password link...")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        sleep(1)  # Wait a bit after scrolling

        logging.info("Waiting for the change password link to be clickable...")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MOBILE_CHANGE_PASSWORD_LINK)
        )

        logging.info("Clicking the change password link...")
        element.click()
        logging.info("Change password link clicked successfully.")


# Mobile Emulation Setup
def get_mobile_driver():
    mobile_emulation = {
        "deviceName": "Pixel 5"
    }
    options = ChromeOptions()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = Chrome(options=options)
    return driver


if __name__ == "__main__":
    driver = get_mobile_driver()
    main_page = MainPage(driver)

    try:
        main_page.open_main_page()
        main_page.click_sign_in()
        main_page.click_assistant_button()  # Clicks Assistant button instead of Settings
        main_page.scroll_and_click_change_password()  # Scrolls and clicks "Change Password"
    finally:
        driver.quit()

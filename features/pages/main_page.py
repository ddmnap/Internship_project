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
    ASSISTANT_BUTTON = (By.CSS_SELECTOR, ".settings-link.w-inline-block")
    MOBILE_CHANGE_PASSWORD_LINK = (By.CSS_SELECTOR, "a[href='/set-new-password']")
    CONNECT_COMPANY_BTN = (By.CSS_SELECTOR, "a[href='/buy-plan-company']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_main_page(self):
        self.driver.get("https://soft.reelly.io")

    def click_sign_in(self):
        self.click(self.SIGN_IN_BUTTON)

    def click_assistant_button(self):
        logging.info("Waiting for Assistant button to be clickable...")
        assistant_btn = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.ASSISTANT_BUTTON)
        )
        assistant_btn.click()
        logging.info("Assistant button clicked.")

    def scroll_and_click_change_password(self):
        logging.info("Scrolling to the bottom of the page...")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(1)

        logging.info("Ensuring the change password link is visible...")
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.MOBILE_CHANGE_PASSWORD_LINK)
        )

        logging.info("Scrolling to the change password link...")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        sleep(1)

        logging.info("Waiting for the change password link to be clickable...")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MOBILE_CHANGE_PASSWORD_LINK)
        )

        logging.info("Clicking the change password link...")
        element.click()

    def verify_connect_company_button(self):
        logging.info("Looking for 'Connect the company' button...")
        connect_btns = self.find_elements(*self.CONNECT_COMPANY_BTN)

        assert len(connect_btns) > 1, f"Expected at least 2 elements, but found {len(connect_btns)}"

        target_btn = connect_btns[1]
        assert target_btn.is_displayed() and target_btn.is_enabled(), "Connect the company button is not available"
        logging.info("'Connect the company' button is visible and enabled.")

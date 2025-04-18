from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def input_text(self, locator, text):
        field = self.find_element(locator)
        field.clear()
        field.click()  # focus before typing
        field.send_keys(text)
        print(f"Entered text into: {locator}")


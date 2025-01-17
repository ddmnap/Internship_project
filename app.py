from features.pages import LoginPage
from features.pages.change_password_page import PasswordPage
from features.pages import MainPage, LoginPage


class App:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage (driver)
        self.log_in_page = LoginPage(driver)
        self.change_password_page = PasswordPage(driver)




    def quit(self):
        if self.driver:
            self.driver.quit()

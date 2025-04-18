from features.pages.main_page import MainPage
from features.pages.log_in_page import LoginPage
from features.pages.change_password_page import PasswordPage



class App:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage (driver)
        self.log_in_page = LoginPage(driver)
        self.change_password_page = PasswordPage(driver)




    def quit(self):
        if self.driver:
            self.driver.quit()

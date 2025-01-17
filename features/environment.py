from app import App
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging


def before_all(context):
    logging.basicConfig(level=logging.INFO)
    logging.info("Initializing the browser and application...")

    # Initialize the WebDriver
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Maximize browser window
    context.driver.maximize_window()

    # Initialize the app object
    context.app = App(context.driver)


def after_all(context):
    logging.info("Closing the browser...")
    # Quit the WebDriver
    context.driver.quit()





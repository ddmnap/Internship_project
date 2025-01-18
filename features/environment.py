from app import App
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Import Options for Chrome
from selenium.webdriver.firefox.service import Service as FirefoxService  # Import Service for Firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions  # Import Options for Firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager  # Import GeckoDriverManager for Firefox
import logging
import os  # For reading environment variables

def before_all(context):
    logging.basicConfig(level=logging.INFO)
    logging.info("Initializing the browser and application...")

    browser = os.getenv('BROWSER', 'chrome').lower()  # Default to Chrome if no environment variable is set

    if browser == 'chrome':
        # Set up Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Enable headless mode
        chrome_options.add_argument("--disable-gpu")  # Optional for better performance
        chrome_options.add_argument("--window-size=1920x1080")  # Optional for specific screen size

        # Initialize the WebDriver with Chrome options
        context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    elif browser == 'firefox':
        # Set up Firefox options for headless mode
        firefox_options = FirefoxOptions()
        firefox_options.headless = True  # Enable headless mode for Firefox
        firefox_options.set_preference("dom.webdriver.enabled", False)  # Avoid issues with Firefox WebDriver

        # Initialize the WebDriver with Firefox options
        context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)

    else:
        logging.error(f"Unsupported browser: {browser}")
        raise Exception(f"Unsupported browser: {browser}")

    # Initialize the app object
    context.app = App(context.driver)

def after_all(context):
    logging.info("Closing the browser...")
    # Quit the WebDriver
    context.driver.quit()

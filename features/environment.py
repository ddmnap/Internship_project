from app import App
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Import Options for Chrome
from selenium.webdriver.firefox.service import Service as FirefoxService  # Import Service for Firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions  # Import Options for Firefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager  # Import GeckoDriverManager for Firefox
import logging
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os  # For reading environment variables

# Set up logging
logging.basicConfig(level=logging.INFO)

def browser_init(context,scenario_name):
    """
    :param context: Behave context
    """


# def before_all(context):
#     logging.info("Setting up the browser and application...")
#
#     # Set up the WebDriver (Chrome example)
#     driver_path = ChromeDriverManager().install()
#     service = Service(driver_path)
#     options = Options()
#     options.add_argument("--headless")  # Use headless mode if desired
#     context.driver = webdriver.Chrome(service=service, options=options)
#
#     # Initialize the App object with the driver
#     context.app = App(context.driver)
#     logging.info("Browser and application setup complete.")
#
#
# def after_all(context):
#     logging.info("Closing the browser...")
#     # Quit the WebDriver
#     if hasattr(context, 'driver'):
#         context.driver.quit()

def before_scenario(context, scenario):
    logging.info(f"Starting scenario: {scenario.name}")
    browser_init(context, scenario.name)


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)


    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'darianapoleonova_NT1jEw'
    bs_key = 'E8PmFxeenm1pnbsgqd6y'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    options = Options()
    bstack_options = {

        "os": "OS X",
        "osVersion": "Monterey",
        'browserName': 'Safari',
        'browserVersion': 15.6,
        'sessionName': scenario_name,
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    def before_scenario(context, scenario):
        print('\nStarted scenario: ', scenario.name)
        browser_init(context, scenario.name)

    def before_step(context, step):
        print('\nStarted step: ', step)

    def after_step(context, step):
        if step.status == 'failed':
            print('\nStep failed: ', step)

    def after_scenario(context, feature):
        context.driver.quit()

    # Initialize the app object
    context.app = App(context.driver)

# def before_all(context):
#     logging.basicConfig(level=logging.INFO)
#     logging.info("Initializing the browser and application...")
#
#
#     if browser == 'chrome':
#         Set up Chrome options for headless mode
#         chrome_options = Options()
#         chrome_options.add_argument("--headless")  # Enable headless mode
#         chrome_options.add_argument("--disable-gpu")  # Optional for better performance
#         chrome_options.add_argument("--window-size=1920x1080")  # Optional for specific screen size
#         Initialize the WebDriver with Chrome options
#         context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
#     elif browser == 'firefox':
#         Set up Firefox options for headless mode
#         firefox_options = FirefoxOptions()
#         firefox_options.headless = True  # Enable headless mode for Firefox
#         firefox_options.set_preference("dom.webdriver.enabled", False)  # Avoid issues with Firefox WebDriver
#         Initialize the WebDriver with Firefox options
#         context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
#
#
#     else:
#         logging.error(f"Unsupported browser: {browser}")
#         raise Exception(f"Unsupported browser: {browser}")

# def after_all(context):
#     logging.info("Closing the browser...")
#     # Quit the WebDriver
#     if hasattr(context, 'driver'):
#         context.driver.quit()

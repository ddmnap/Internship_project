import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
from app import App

# Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/features/tests/change_password.feature

# Set up logging
logging.basicConfig(level=logging.INFO)


def browser_init(context, scenario_name, browser='chrome', use_browserstack=False):
    """
    Initialize the browser based on the specified type.
    :param context: Behave context
    :param scenario_name: Name of the scenario
    :param browser: Type of the browser (chrome/firefox)
    :param use_browserstack: Whether to use BrowserStack for remote testing
    """
    logging.info(f"Initializing browser: {browser} for scenario: {scenario_name}")

    # ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = 'darianapoleonova_NT1jEw'
    # bs_key = 'E8PmFxeenm1pnbsgqd6y'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #
    #     "os": "OS X",  # Specify OS
    #     "osVersion": "Monterey",  # Specify OS version
    #     'browserName': 'Safari',  # Specify browser
    #     'browserVersion': '15.6',  # Specify browser version
    #     'sessionName': scenario_name,  # Name the session
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    if not use_browserstack:
        if browser == 'chrome':
            # Set up Chrome options for headless mode and mobile emulation
            chrome_options = Options()
            # chrome_options.add_argument("--headless")  # Enable headless mode
            chrome_options.add_argument("--disable-gpu")  # Optional for better performance
            chrome_options.add_argument("--window-size=1920x1080")  # Optional for specific screen size

            # Mobile emulation for iPhone 6 (this keeps the mobile testing configuration intact)
            mobile_emulation = {"deviceName": "iPhone 6"}
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

            # Initialize the WebDriver with Chrome options
            context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        # Firefox section commented out since we're focusing on mobile testing with Chrome
        # elif browser == 'firefox':
        #     # Set up Firefox options for headless mode
        #     firefox_options = FirefoxOptions()
        #     firefox_options.headless = True  # Enable headless mode for Firefox
        #     firefox_options.set_preference("dom.webdriver.enabled", False)  # Avoid issues with Firefox WebDriver
        #     # Initialize the WebDriver with Firefox options
        #     context.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
        #
        # else:
        #     logging.error(f"Unsupported browser: {browser}")
        #     raise Exception(f"Unsupported browser: {browser}")


def before_all(context):
    logging.info("Setting up the browser and application...")
    browser_init(context, scenario_name=None)  # Set up the browser for the first time
    context.app = App(context.driver)  # Initialize the app object
    logging.info("Browser and application setup complete.")


def after_all(context):
    logging.info("Closing the browser...")
    # Quit the WebDriver
    if hasattr(context, 'driver'):
        context.driver.quit()


def before_scenario(context, scenario):
    logging.info(f"Starting scenario: {scenario.name}")
    browser_init(context, scenario.name)  # Re-initialize browser for each scenario


def after_scenario(context, scenario):
    logging.info(f"Ending scenario: {scenario.name}")
    context.driver.quit()  # Ensure driver quits after scenario


def before_step(context, step):
    logging.info(f"Starting step: {step.name}")


def after_step(context, step):
    if step.status == 'failed':
        logging.error(f"Step failed: {step.name}")

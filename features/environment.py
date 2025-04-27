import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app import App

# Set up logging
logging.basicConfig(level=logging.INFO)

def browser_init(context, scenario_name, browser='chrome'):
    logging.info(f"Initializing browser: {browser} for scenario: {scenario_name}")

    if browser == 'chrome':
        chrome_options = Options()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1600,1000")  # Desktop layout
        # If you want mobile, uncomment these:
        # mobile_emulation = {"deviceName": "iPhone X"}
        # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        context.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )
    else:
        raise Exception(f"Unsupported browser: {browser}")  # ← make sure this is in place

def before_all(context):
    logging.info("Global test setup complete.")

def after_all(context):
    logging.info("Closing the browser...")
    if hasattr(context, 'driver'):
        context.driver.quit()

def before_scenario(context, scenario):
    logging.info(f"Starting scenario: {scenario.name}")
    browser_init(context, scenario.name)
    context.app = App(context.driver)
    logging.info("Browser and application setup complete.")

def after_scenario(context, scenario):
    logging.info(f"Ending scenario: {scenario.name}")
    context.driver.quit()

def before_step(context, step):
    logging.info(f"Starting step: {step.name}")

def after_step(context, step):
    if step.status == 'failed':
        logging.error(f"Step failed: {step.name}")

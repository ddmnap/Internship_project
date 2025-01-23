from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
import logging
from time import sleep
from dotenv import load_dotenv
import os



logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)


@given("I open the Reelly main page")
def open_main_page(context):
    context.app.main_page.open_main_page()


@given('I log in with valid credentials')
def log_in_with_valid_credentials(context):
    email = os.getenv("REELLY_EMAIL")
    password = os.getenv("REELLY_PASSWORD")

    if not email or not password:
        raise ValueError("Environment variables for credentials are not set.")

    context.app.log_in_page.log_in(email, password)


@when("I click on the settings button")
def click_settings_button(context):
    logging.info("Clicking on the settings button...")
    context.app.main_page.click_settings()
    sleep(2)

@when("I click on the change password button")
def click_change_password_button(context):
    logging.info("Clicking on the change password button...")
    context.app.main_page.click_change_password()

@then("I should see the change password form")

def verify_change_password_form(context):
    logging.info("Verifying that the change password form is displayed...")
    assert context.app.change_password_page.is_password_form_displayed(), "Change password form is not displayed."

@then('the "Change password" button should be available')
def verify_change_password_button(context):
    logging.info("Checking if the 'Change password' button is enabled...")
    assert context.app.change_password_page.is_change_password_button_enabled(), "Change password button is not enabled."
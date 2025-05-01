from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


@when('I click on the "Off-plan" option from the left menu')
def step_click_off_plan_menu(context):
    logging.info("Clicking Off-plan from the left menu...")

    # First click on "Secondary" to load the correct menu context
    secondary_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Secondary"))
    )
    secondary_button.click()

    # Then click old "Off-plan" button
    off_plan_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/off-plan'].menu-button-block.w-inline-block"))
    )
    off_plan_button.click()

@then('The "Off-plan" page should be displayed')
def step_verify_off_plan_page(context):
    logging.info("Verifying Off-plan page is loaded...")
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cards-properties"))
    )
    logging.info("Verified Off-plan page loaded.")

@when("I click on the last pagination button")
def step_click_last_page(context):
    logging.info("Clicking last pagination button...")
    try:
        last_page_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[wized="nextPageProperties"]'))
        )
        last_page_button.click()
    except Exception as e:
        raise AssertionError("Could not click last pagination button. Message: " + str(e))

@when("I click on the first pagination button")
def step_click_first_page(context):
    logging.info("Clicking first pagination button...")
    try:
        first_page_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[wized="previousPageProperties"]'))
        )
        first_page_button.click()
    except Exception as e:
        raise AssertionError("Could not click first pagination button. Message: " + str(e))

@then("The first page should be displayed")
def step_verify_first_page(context):
    logging.info("Verifying first page is displayed...")
    try:
        current_url = context.driver.current_url
        assert "page=1" in current_url or "page" not in current_url
        logging.info("Successfully navigated back to the first page.")
    except Exception as e:
        raise AssertionError("Page validation failed: " + str(e))
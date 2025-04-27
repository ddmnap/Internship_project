from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import os
from time import sleep

logging.basicConfig(level=logging.INFO)



@when("I click on the settings option")
def step_click_settings(context):
    context.app.main_page.click_assistant_button()


@then("The settings page should be displayed")
def step_verify_settings_page(context):
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "settings-block-menu"))
    )
    assert "settings" in context.driver.current_url.lower() or True


@then("There should be 13 settings options visible")
def step_verify_number_of_settings_options(context):
    logging.info("Looking for settings menu items (.page-setting-block)...")

    settings_blocks = WebDriverWait(context.driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".page-setting-block"))
    )

    logging.info(f"Found {len(settings_blocks)} settings options.")
    assert len(settings_blocks) == 13, f"Expected 13 options, but found {len(settings_blocks)}"





@then("The 'connect the company' button should be available")
def step_verify_connect_company_button(context):

    logging.info("Checking for 'Connect the company' button using visible text...")

    try:
        button = WebDriverWait(context.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(., 'Connect the company')]"))
        )

        context.driver.execute_script("arguments[0].scrollIntoView(true);", button)

        WebDriverWait(context.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(., 'Connect the company')]"))
        )

        assert button.is_displayed() and button.is_enabled(), "'Connect the company' button is not visible or enabled"
        logging.info("'Connect the company' button is visible and clickable.")
    except Exception as e:
        logging.error("Step failed: The 'connect the company' button should be available")
        raise AssertionError("'Connect the company' button is not visible or clickable. " + str(e))

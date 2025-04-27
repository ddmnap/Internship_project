import logging
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from time import sleep



@when('I click on the "Secondary" option from the left menu')
def step_click_secondary(context):
    logging.info("Clicking on the Secondary menu option...")
    try:
        secondary_option = WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='g-menu-text' and text()='Secondary']"))
        )
        context.driver.execute_script("arguments[0].scrollIntoView(true);", secondary_option)
        secondary_option.click()
        logging.info("Clicked the 'Secondary' option successfully.")
    except Exception as e:
        logging.error("Step failed: I click on the 'Secondary' option from the left menu")
        raise AssertionError("Could not click on the 'Secondary' option. " + str(e))

@then('The "Secondary" page should be displayed')
def step_verify_secondary_page(context):
    logging.info("Verifying Secondary page is loaded...")
    try:
        WebDriverWait(context.driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'page-title') and contains(text(), 'Listings')]"))
        )
        logging.info("Verified: 'Listings' page title found. Secondary page loaded.")
    except Exception as e:
        logging.error("Step failed: The 'Secondary' page should be displayed")
        raise AssertionError("Secondary page did not load properly. " + str(e))


@when("I click on Filters")
def step_click_filters(context):

    logging.info("Clicking on Filters button...")

    try:
        filter_button = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.filter-button"))
        )
        context.driver.execute_script("arguments[0].scrollIntoView(true);", filter_button)

        WebDriverWait(context.driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.filter-button"))
        )

        context.driver.execute_script("arguments[0].click();", filter_button)

        logging.info("Clicked Filters button via JavaScript.")
    except Exception as e:
        logging.error("Step failed: I click on Filters")
        raise AssertionError("Could not click on Filters button. " + str(e))


@when('I filter the products by "Want to buy"')
def step_select_want_to_buy_filter(context):

    logging.info("Selecting 'Want to buy' filter...")

    try:
        want_to_buy_button = WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'switcher-button') and .//div[text()='Want to buy']]"))
        )

        context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", want_to_buy_button)

        want_to_buy_button.click()

        logging.info("Clicked 'Want to buy' filter.")

        sleep(2)  # let the products refresh
    except Exception as e:
        logging.error("Step failed: I filter the products by 'Want to buy'")
        raise AssertionError("Could not select 'Want to buy' filter properly. Message: " + str(e))


@when('I click on Apply Filter')
def step_click_apply_filter(context):
    logging.info("Clicking on Apply Filter button...")

    try:
        apply_filter_button = WebDriverWait(context.driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//a[@wized='applyFilterButtonMLS']"))
        )


        context.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", apply_filter_button)

        time.sleep(2)

        context.driver.execute_script("arguments[0].click();", apply_filter_button)

        logging.info("Clicked Apply Filter button.")
    except Exception as e:
        logging.error("Step failed: I click on Apply Filter")
        raise AssertionError("Could not click on Apply Filter button. " + str(e))


@then('All product cards should have the "Want to buy" tag')
def step_verify_all_product_tags(context):
    wait = WebDriverWait(context.driver, 15)

    # Scroll down to force load more products
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)  # Let page load more
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    # Very important: Wait until old "For sale" listings are gone
    try:
        wait.until_not(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.for-sale-block"), "For sale"))
    except:
        pass  # Ignore if timeout, continue anyway

    sleep(2)  # Wait for new cards to appear

    all_products = context.driver.find_elements(By.CLASS_NAME, "listing-card")
    assert all_products, "No product cards found!"

    wrong_tags = []

    for product in all_products:
        try:
            tag = product.find_element(By.CSS_SELECTOR, "div.for-sale-block").text.strip()
            if tag != "Want to buy":
                wrong_tags.append(tag)
        except Exception as e:
            raise AssertionError(f"No 'Want to buy' tag found inside product card: {str(e)}")

    if wrong_tags:
        raise AssertionError(f"Found wrong tags: {wrong_tags}")
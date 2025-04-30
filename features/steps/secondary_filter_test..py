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

    # Wait until old "For sale" listings are gone
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

# -------------------- Price Range Filter Test Steps --------------------

import logging
import time
import re
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then


@when('I filter the products by price range from 1200000 to 2000000 AED')
def step_filter_by_price_range(context):
    logging.info("Filtering products by price range 1200000 - 2000000 AED...")
    try:
        time.sleep(1)

        # Wait for and input the min price
        min_input = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[wized='unitPriceFromFilter']"))
        )
        min_input.click()
        min_input.clear()
        min_input.send_keys("1200000")

        time.sleep(1)

        # Wait for and input the max price
        max_input = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[wized='unitPriceToFilter']"))
        )
        max_input.click()
        max_input.clear()
        max_input.send_keys("2000000")

        logging.info("Entered price range successfully.")
    except Exception as e:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"price_filter_failure_{timestamp}.png"
        context.driver.save_screenshot(screenshot_name)
        logging.error(f"Step failed: I filter the products by price range from 1200000 to 2000000 AED\nScreenshot saved as: {screenshot_name}")
        raise AssertionError("Could not set price range. Screenshot saved as: " + screenshot_name)


@when('I click Apply Filter after setting price range')
def step_click_apply_filter_after_price(context):
    logging.info("Clicking Apply Filter after setting price range...")
    try:
        apply_button = WebDriverWait(context.driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@wized='applyFilterButtonMLS']"))
        )
        apply_button.click()
        logging.info("Clicked Apply Filter button.")
    except Exception as e:
        raise AssertionError("Could not click Apply Filter after price range. " + str(e))


@then('All product cards should have prices within the selected range')
def step_verify_prices_within_range(context):
    logging.info("Verifying all products have prices in the range 1200000 - 2000000 AED...")
    try:
        time.sleep(2)

        product_prices = context.driver.find_elements(By.CLASS_NAME, "number-price-text")
        assert product_prices, "No product cards found after filtering!"

        for price_element in product_prices:
            raw = price_element.text
            cleaned = re.sub(r"[^\d]", "", raw)
            if not cleaned.isdigit():
                raise AssertionError(f"Price '{raw}' is not a valid number.")
            price = int(cleaned)
            if not (1200000 <= price <= 2000000):
                raise AssertionError(f"Found product price {price} outside the range 1200000-2000000.")
        logging.info("All prices are within the selected range.")
    except Exception as e:
        raise AssertionError("Price verification failed. " + str(e))
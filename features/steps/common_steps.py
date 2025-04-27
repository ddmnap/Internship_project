from behave import given
import os
import logging

@given("I open the main page")
def step_open_main_page(context):
    context.driver.get("https://soft.reelly.io")

@given("I log in to the page")
def step_login(context):
    email = os.getenv("REELLY_EMAIL")
    password = os.getenv("REELLY_PASSWORD")
    logging.info(f"Logging in with email: {email}")
    context.app.log_in_page.log_in(email, password)

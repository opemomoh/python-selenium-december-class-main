from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep





@when('Click on Sign in')
def click_sign_in(context):
    sign_in_dropdown = context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()


@when('From right side navigation menu, click Sign In')
def click_signin_on_the_right(context):
    target_sign_in = context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then('Verify Sign In form opened')
def verify_cart_is_empty(context, ):
    sign_in_verification = context.driver.find_element(By.CSS_SELECTOR, '#login').text
    assert 'Sign in' in sign_in_verification

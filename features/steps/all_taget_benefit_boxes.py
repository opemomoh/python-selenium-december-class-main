from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on target circle')
def click_target_circle_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[href='/circle']").click()
    sleep(4)


@then('Verify all {number} benefit boxes are present')
def verify_benefit_boxes_are_present(context, number):
    print(type(number))
    number = int(number)
    print(type(number))
    verify_number_of_boxes = context.driver.find_elements(By.CSS_SELECTOR, "[class*='styles__BenefitsGrid'] li")
    print(verify_number_of_boxes)
    assert len(verify_number_of_boxes) == number

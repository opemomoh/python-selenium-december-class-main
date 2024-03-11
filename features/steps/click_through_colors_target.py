from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

target_color_selector = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
color_selector = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")


@given('Open Target link to product first product')
def open_target_link(context):
    context.driver.get('https://www.target.com/p/A-81540287')
    sleep(7)


@then('Verify user can click on colors first product')
def verify_colors_are_clickable(context):
    expected_colors = ['Black', 'Deep Olive', 'White']
    actual_color = []
    colors = context.driver.find_elements(*target_color_selector)
    for color in colors:
        color.click()
        color_selected = context.driver.find_element(*color_selector).text.split('\n')[1]
        actual_color.append(color_selected)
    assert actual_color == expected_colors
    sleep(5)


@given('Open Target link to product second product')
def open_target_link(context):
    context.driver.get('https://www.target.com/p/A-54551690')
    sleep(7)


@then('Verify user can click on colors second product')
def verify_colors_are_clickable(context):
    expected_colors_second_product = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    actual_color_second_product = []
    colors = context.driver.find_elements(*target_color_selector)
    for color in colors:
        color.click()
        color_selected = context.driver.find_element(*color_selector).text.split('\n')[1]
        actual_color_second_product.append(color_selected)
    assert actual_color_second_product == expected_colors_second_product
    sleep(5)
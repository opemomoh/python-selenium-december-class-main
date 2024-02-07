from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

#amazon_signup_page
amazon_logo_signup_page = driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')
create_account_logo = driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
signup_your_name = driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')
signup_mobile_number_or_email = driver.find_element(By.CSS_SELECTOR, '#ap_email')
signup_password = driver.find_element(By.CSS_SELECTOR, '#ap_password')
signup_reenter_password = driver.find_element(By.CSS_SELECTOR, '#ap_password_check')
signup_continue = driver.find_element(By.CSS_SELECTOR, '#continue')
amazon_sign_in = driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis')
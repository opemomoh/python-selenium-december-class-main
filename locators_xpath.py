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

amazon_logo = driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
email_field = driver.find_element(By.ID, 'ap_email')
continue_button = driver.find_element(By.ID, "continue")
conditions_of_use_link = driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")
privacy_notice_link = driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")
need_help_link = driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
forgot_your_password_link = driver.find_element(By.ID, "auth-fpp-link-bottom")
other_issues_with_signin_link = driver.find_element(By.ID, "ap-other-signin-issues-link")
create_your_amazon_account_button = driver.find_element(By.ID, "createAccountSubmit")
amazon_orders_returns = driver.find_element(By.ID, "nav-cart")
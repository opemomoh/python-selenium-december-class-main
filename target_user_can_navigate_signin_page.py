from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

#click on signin page
target_homepage_signin_button = driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
target_homepage_signin_button.click()

sleep(2)
#click signin from side navigation
target_nav_signin_button = driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
target_nav_signin_button.click()

sleep(2)

#verify signin page opened
sign_in_verification = driver.find_element(By.ID, "login").text
assert 'Sign in' in sign_in_verification
if "Sign in" in sign_in_verification:
       print("test passed")
else:print("test failed")
sleep(2)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# NOTE: Make sure you have the Chrome webdriver in /usr/local/bin
# or replace this with your own webdriver
browser = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
browser.get("https://twitter.com/")
print("Navigated to Twitter...")

signup = browser.find_element_by_class_name("js-signup")
print("Found signup link:")
print("\tText: " + signup.text)
loc = signup.location
print("\tLocation: " + str(loc['x']) + ", " + str(loc['y']))

print("Clicking signup link...")
signup.click()

# Wait to continue until page load
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "signup")))

print("Navigated to signup page")

print("Filling out mock user information...")

name_input = browser.find_element_by_id('full-name')
name_input.send_keys('John Botsman')

email_input = browser.find_element_by_id('email')
email_input.send_keys('botsman@sky.net')

pwd_input = browser.find_element_by_id('password')
pwd_input.send_keys('swordfish')
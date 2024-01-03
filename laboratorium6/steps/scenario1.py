from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from time import sleep

driver = None


@given('I open the website "{url}" on specific "{browser}"')
def open_website(context, url, browser):
    print(browser)
    global driver
    options = ChromeOptions() if 'chrome' in browser.lower() else FirefoxOptions()
    context.driver = webdriver.Chrome(options=options) if 'chrome' in browser.lower() else webdriver.Firefox(options=options)
    context.driver.get(url)


@when('I click on the login button')
def click_login_button(context):
    context.driver.find_element(By.ID, 'nav-login').click()


@when('I enter "{username}" and "{password}"')
def enter_credentials(context, username, password):
    context.driver.find_element(By.ID, 'email').send_keys(username)
    context.driver.find_element(By.ID, 'password').send_keys(password)


@when('I click the login button')
def click_login(context):
    context.driver.find_element(By.CLASS_NAME, 'btn-primary').click()
    sleep(2)


@then('I should see an error message "{expected_error}"')
def verify_error_message(context, expected_error):
    error_popup = context.driver.find_element(By.CLASS_NAME, 'ui-pnotify-title')
    actual_error = error_popup.text
    assert expected_error in actual_error, f"Expected: '{expected_error}'. Got: '{actual_error}.'"
    context.driver.quit()

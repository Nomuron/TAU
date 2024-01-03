from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)


@given('I open the website "{url}" using "{browser}" browser')
def open_website(context, url, browser):
    options = ChromeOptions() if 'Chrome' in browser else FirefoxOptions()
    context.driver = webdriver.Chrome(options=options) if 'Chrome' in browser else webdriver.Firefox(options=options)
    context.driver.get(url)


@when('I log in with username "{username}" and password "{password}"')
def login(context, username, password):
    context.driver.find_element(By.ID, 'user-name').send_keys(username)
    context.driver.find_element(By.ID, 'password').send_keys(password)
    context.driver.find_element(By.ID, 'login-button').click()


@when('I add items to the cart')
def add_items_to_cart(context):
    items_add_buttons_list = [
        'add-to-cart-sauce-labs-backpack', 'add-to-cart-sauce-labs-bike-light',
        'add-to-cart-sauce-labs-bolt-t-shirt', 'add-to-cart-sauce-labs-fleece-jacket',
        'add-to-cart-sauce-labs-onesie'
    ]

    for item_button in items_add_buttons_list:
        context.driver.find_element(By.ID, item_button).click()


@then('I should see the correct number of items in the cart')
def verify_cart_items(context):
    cart_badge_number = int(context.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text)

    if cart_badge_number == 5:
        logger.info('Cart badge is showing the correct number of items')
    else:
        logger.info('Cart badge is showing an incorrect number of items')

    context.driver.quit()

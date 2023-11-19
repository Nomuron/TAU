import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chop
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as ffop

logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)

logger.info('Start of the test scenario')

DRIVER_NAMES = ['Chrome', 'Firefox']
for driver_name in DRIVER_NAMES:
    if 'Chro' in driver_name:
        logger.info(f'Starting test with {driver_name} browser')
        chrome_options = chop()
        driver = webdriver.Chrome(options=chrome_options)
    else:
        logger.info(f'Starting test with {driver_name} browser')
        firefox_options = ffop()
        driver = webdriver.Firefox(options=firefox_options)

    driver.get('https://www.saucedemo.com/')
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.ID, 'login-button').click()

    items_add_buttons_list = ['add-to-cart-sauce-labs-backpack', 'add-to-cart-sauce-labs-bike-light',
                              'add-to-cart-sauce-labs-bolt-t-shirt', 'add-to-cart-sauce-labs-fleece-jacket',
                              'add-to-cart-sauce-labs-onesie']

    for item_button in items_add_buttons_list:
        driver.find_element(By.ID, item_button).click()

    cart_badge_number = int(driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text)

    if len(items_add_buttons_list) == cart_badge_number:
        logger.info('Cart badge is showing same number as amount of added items')
    else:
        logger.info('Cart badge is showing incorrect number of items.')

    logger.info('End of the test scenarion for browser')
    driver.close()

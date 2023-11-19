import logging
from time import sleep

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

    driver.get('http://www.scrapethissite.com/')
    login_subpage_button = driver.find_element(By.ID, 'nav-login')
    login_subpage_button.click()

    login_input = driver.find_element(By.ID, 'email')
    login_input.send_keys('example@onet.pl')

    password_input = driver.find_element(By.ID, 'password')
    password_input.send_keys('example')

    login_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
    login_button.click()

    sleep(2)

    error_popup = driver.find_element(By.CLASS_NAME, 'ui-pnotify-title')
    logger.info('Site testing stopped at logging page with an error:')
    logger.warning(error_popup.text)

    logger.info(f'End of the test scenario for {driver_name} browser')
    driver.close()

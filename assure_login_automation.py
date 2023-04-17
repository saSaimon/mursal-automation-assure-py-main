import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import datetime
import os

json_keys = json.loads(open(os.path.join('tests', 'CONSTANTS.json')).read())
config = json.loads(open(os.path.join('tests', 'config.json'), 'r').read())
json_keys = json.loads(open('CONSTANTS.json', 'r').read())
test_list = json.loads(open('cases/login_cases.json', 'r').read())
config = json.loads(open('config.json', 'r').read())

driver_path = config['driver_path']
base_url = config['base_url']


def init_driver(driver_path):
    '''Initialize Webdriver and returns the driver object'''
    from selenium.webdriver.chrome.service import Service
    from selenium import webdriver

    service = Service(driver_path)
    # options = webdriver.Edge()
    driver = webdriver.Chrome(service=service)
    return driver

# def init_driver(driver_path):
#     '''Initialize Webdriver and returns the driver object'''
#     from selenium.webdriver.chrome.service import Service
#     from selenium import webdriver
#     from webdriver_manager.chrome import ChromeDriverManager

#     options = webdriver.ChromeOptions() 
#     options.add_argument("--no-sandbox");
#     options.add_argument("--disable-dev-shm-usage");

#     options.add_argument('--headless')
#     options.add_argument('--disable-gpu')  # Last I checked this was necessary.
#     s=Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=s, options=options)
   
#     return driver


def org_login(
    driver,
    current_case
):
    '''Login to Assure using the given email and password'''
    flag = 'FAILURE'
    test_result  = ''
    print('--------------', current_case, '--------------')
    try:
        description = test_list["LOGIN_CASES"][current_case]["DESCRIPTION"]
        loginemail = test_list["LOGIN_CASES"][current_case]["USERNAME"]
        password = test_list["LOGIN_CASES"][current_case]["PASSWORD"]
        result = test_list["LOGIN_CASES"][current_case]["EXPECTED_RESULT"]

        login_email = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["LOGIN_EMAIL"])
        login_email.clear()
        login_email.send_keys(loginemail)

        login_password = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["LOGIN_PASSWORD"])
        login_password.clear()
        login_password.send_keys(password)

        login_button = driver.find_element(By.TAG_NAME, json_keys["KEYS"]["TAG_NAMES"]["BUTTON"])
        login_button.click()

        time.sleep(8)

        updated_url = driver.current_url
        if (updated_url == json_keys["URLs"]["DEALS_VIEW_URL"]):
            flag = 'SUCCESS'
        else:
            flag = 'FAILURE'

        if(result):
            if (flag == result):
                test_result = description + ', PASSED'
            else:
                test_result = description + ', FAILED'

    except Exception as e:
        print(str(e))

    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ', ' + test_result + '\n'
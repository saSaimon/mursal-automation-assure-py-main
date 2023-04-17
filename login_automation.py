'''
    InstaCate Frontend Automated QA Tests using Selenium
'''
from cgi import test
import datetime
import json
import os
from selenium.webdriver.support import wait
from assure_login_automation import *
from create_vendor_automation import *

# json_keys = json.loads(open(os.path.join('tests', 'CONSTANTS.json')).read())
# config = json.loads(open(os.path.join('tests', 'config.json'), 'r').read())
json_keys = json.loads(open('cases/login_cases.json', 'r').read())
config = json.loads(open('config.json', 'r').read())

try:
    config = json.loads(open(os.path.join('tests', 'config.json'), 'r').read())
    loginemail = config['login']
    password = config['password']
    driver_path = config['driver_path']
    base_url = config['base_url']
except Exception as e:
    print(str(e))

def login_org():
    testCases = []
    # Login to InstaCate
    login_cases_keys = json_keys["LOGIN_CASES"].keys()
    testCases.append(',Login Test Cases, \n')
    for case in login_cases_keys:
        # Initializing and starting the driver
        driver = init_driver(driver_path)
        driver.get(base_url)
        driver.maximize_window()
        login_test = org_login(driver, case) # Initiating the Test Case
        driver.close() # Closing the window for fresh test case everytime

        print(login_test)
        testCases.append(login_test) # Appending the test case to the list
    return testCases

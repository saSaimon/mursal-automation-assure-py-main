'''
    InstaCate Frontend Automated QA Tests using Selenium
'''
from cgi import test
import datetime
import json
import os
from selenium.webdriver.support import wait
from assure_login_automation import *
from org_signup_automation import org_signup

# json_keys = json.loads(open(os.path.join('tests', 'CONSTANTS.json')).read())
# config = json.loads(open(os.path.join('tests', 'config.json'), 'r').read())
json_keys = json.loads(open('cases/signup_cases.json', 'r').read())
config = json.loads(open('config.json', 'r').read())

try:
    config = json.loads(open(os.path.join('config.json'), 'r').read())
    loginemail = config['login']
    password = config['password']
    driver_path = config['driver_path']
    org_signup_url = config['org_signup_url']
except Exception as e:
    print(str(e))

def signup_organizer():
    testCases = []
    # Login to InstaCate
    org_signup_cases_keys = json_keys["SIGNUP_CASES"].keys()
    testCases.append(',Organizer Signup Test Cases, \n')
    for case in org_signup_cases_keys:
        # Initializing and starting the driver
        driver = init_driver(driver_path)
        driver.get(org_signup_url)
        driver.maximize_window()
        org_signup_test = org_signup(driver, case) # Initiating the Test Case
        driver.close() # Closing the window for fresh test case everytime

        print(org_signup_test)
        testCases.append(org_signup_test) # Appending the test case to the list
    return testCases

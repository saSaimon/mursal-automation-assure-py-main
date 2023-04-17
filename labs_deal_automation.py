'''
    InstaCate Frontend Automated QA Tests using Selenium
'''
from cgi import test
import datetime
import json
import os
from selenium.webdriver.support import wait
from assure_login_automation import *
from labs_deal_create_automate import labs_deal_create
from org_signup_automation import org_signup

# json_keys = json.loads(open(os.path.join('tests', 'CONSTANTS.json')).read())
# config = json.loads(open(os.path.join('tests', 'config.json'), 'r').read())
cases = json.loads(open('cases/labs_deal_create_cases.json', 'r').read())
config = json.loads(open('config.json', 'r').read())

try:
    config = json.loads(open(os.path.join('config.json'), 'r').read())
    loginemail = config['login']
    password = config['password']
    driver_path = config['driver_path']
    org_signup_url = config['org_signup_url']
except Exception as e:
    print(str(e))

def labs_deal_creation():
    testCases = []
    # Login to InstaCate
    labs_deal_create_cases_keys = cases["LABS_DEAL_CREATE_CASES"].keys()
    testCases.append(',Oragnizer Labs Deal Create Test Cases, \n')
    for case in labs_deal_create_cases_keys:
        # Initializing and starting the driver
        driver = init_driver(driver_path)
        driver.get(base_url)
        driver.maximize_window()
        org_login(driver, "CASE5")
        labs_deal_create_test = labs_deal_create(driver, case) # Initiating the Test Case
        driver.close() # Closing the window for fresh test case everytime

        print(labs_deal_create_test)
        testCases.append(labs_deal_create_test) # Appending the test case to the list
    return testCases

'''
    InstaCate Frontend Automated QA Tests using Selenium
'''
from cgi import test
import datetime
import json
import os
from selenium.webdriver.support import wait
from assure_login_automation import *
from create_retirement_investor_profile import create_retirement_investor_profiles
from create_trust_investor_profile import create_trust_investor_profiles
from edit_deal import edit_deal

# json_keys = json.loads(open(os.path.join('tests', 'CONSTANTS.json')).read())
# config = json.loads(open(os.path.join('tests', 'config.json'), 'r').read())
cases = json.loads(open('cases/edit_deal.json', 'r').read())
config = json.loads(open('config.json', 'r').read())

try:
    config = json.loads(open(os.path.join('config.json'), 'r').read())

    driver_path = config['driver_path']
    org_signup_url = config['org_signup_url']
except Exception as e:
    print(str(e))

def edit_deal_automation():
    testCases = []
    # Login to InstaCate
    edit_deal_cases_keys = cases["EDIT_DEAL_INVESTOR_SIDE"].keys()
    testCases.append(',Edit Deal Test Cases, \n')
    for case in edit_deal_cases_keys:
        # Initializing and starting the driver
        driver = init_driver(driver_path)
        driver.get(base_url)
        driver.maximize_window()
        org_login(driver, "CASE5")

        edit_deal_test = edit_deal(driver, case) # Initiating the Test Case
        driver.close() # Closing the window for fresh test case everytime

        print(edit_deal_test)
        testCases.append(edit_deal_test) # Appending the test case to the list
    return testCases

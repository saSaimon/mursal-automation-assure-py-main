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
from edit_carry_n_mgmt_fees import edit_carry_n_mgmt_fees
from edit_deal import edit_deal

# json_keys = json.loads(open(os.path.join('tests', 'CONSTANTS.json')).read())
# config = json.loads(open(os.path.join('tests', 'config.json'), 'r').read())
cases = json.loads(open('cases/edit_carry_n_mgmt_fees.json', 'r').read())
config = json.loads(open('config.json', 'r').read())

try:
    config = json.loads(open(os.path.join('config.json'), 'r').read())

    driver_path = config['driver_path']
    org_signup_url = config['org_signup_url']
except Exception as e:
    print(str(e))

def edit_carry_n_mgmt_fees_automation():
    testCases = []
    # Login to InstaCate
    edit_carry_n_mgmt_fees_keys = cases["EDIT_CARRY_N_MGMT_FEES"].keys()
    testCases.append(',Edit Deal Test Cases, \n')
    for case in edit_carry_n_mgmt_fees_keys:
        # Initializing and starting the driver
        driver = init_driver(driver_path)
        driver.get(base_url)
        driver.maximize_window()
        org_login(driver, "CASE5")

        edit_carry_n_mgmt_fees_test = edit_carry_n_mgmt_fees(driver, case) # Initiating the Test Case
        driver.close() # Closing the window for fresh test case everytime

        print(edit_carry_n_mgmt_fees_test)
        testCases.append(edit_carry_n_mgmt_fees_test) # Appending the test case to the list
    return testCases

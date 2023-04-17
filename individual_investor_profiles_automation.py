'''
    InstaCate Frontend Automated QA Tests using Selenium
'''
from cgi import test
import datetime
import json
import os
from selenium.webdriver.support import wait
from assure_login_automation import *
from create_indi_investor_profiles import create_indi_investor_profiles
from invite_investors import invite_investors

# json_keys = json.loads(open(os.path.join('tests', 'CONSTANTS.json')).read())
# config = json.loads(open(os.path.join('tests', 'config.json'), 'r').read())
cases = json.loads(open('cases/create_investor_profiles.json', 'r').read())
config = json.loads(open('config.json', 'r').read())

try:
    config = json.loads(open(os.path.join('config.json'), 'r').read())

    driver_path = config['driver_path']
    org_signup_url = config['org_signup_url']
except Exception as e:
    print(str(e))

def individual_investor_profiles_automation():
    testCases = []
    # Login to InstaCate
    create_individual_investor_profiles_cases_keys = cases["CREATE_INVESTOR_INDIVIDUAL_PROFILES"].keys()
    testCases.append(',Investor Invitation Test Cases, \n')
    for case in create_individual_investor_profiles_cases_keys:
        # Initializing and starting the driver
        driver = init_driver(driver_path)
        driver.get(base_url)
        driver.maximize_window()
        org_login(driver, "INVESTOR_SIGNIN")

        create_investor_profiles_test = create_indi_investor_profiles(driver, case) # Initiating the Test Case
        driver.close() # Closing the window for fresh test case everytime

        print(create_investor_profiles_test)
        testCases.append(create_investor_profiles_test) # Appending the test case to the list
    return testCases

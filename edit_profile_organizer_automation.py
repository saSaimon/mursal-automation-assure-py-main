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
from edit_profile_organizer import edit_profile_orgaziner

# json_keys = json.loads(open(os.path.join('tests', 'CONSTANTS.json')).read())
# config = json.loads(open(os.path.join('tests', 'config.json'), 'r').read())
cases = json.loads(open('cases/edit_profile_organizer.json', 'r').read())
config = json.loads(open('config.json', 'r').read())

try:
    config = json.loads(open(os.path.join('config.json'), 'r').read())

    driver_path = config['driver_path']
    org_signup_url = config['org_signup_url']
except Exception as e:
    print(str(e))

def edit_profile_organizer_automation():
    testCases = []
    # Login to InstaCate
    edit_org_profile_keys = cases["EDIT_PROFILE_ORGANIZER"].keys()
    testCases.append(',Edit Profile - Organizer Test Cases, \n')
    for case in edit_org_profile_keys:
        # Initializing and starting the driver
        driver = init_driver(driver_path)
        driver.get(base_url)
        driver.maximize_window()
        org_login(driver, "CASE5")

        edit_org_profile_test = edit_profile_orgaziner(driver, case) # Initiating the Test Case
        driver.close() # Closing the window for fresh test case everytime

        print(edit_org_profile_test)
        testCases.append(edit_org_profile_test) # Appending the test case to the list
    return testCases

'''
    Assure Frontend Automated QA Tests using Selenium
'''
from cgi import test
import datetime
import json
import os
from selenium.webdriver.support import wait
from assure_login_automation import *
from edit_carry_n_mgmt_fees_automation import edit_carry_n_mgmt_fees_automation
from edit_deal_automation import edit_deal_automation
from edit_profile_organizer_automation import edit_profile_organizer_automation
from entity_investor_profiles_automation import entity_investor_profiles_automation
from individual_investor_profiles_automation import individual_investor_profiles_automation
from inviting_investors_automation import inviting_investors_automation
from joint_investor_profiles_automation import joint_investor_profiles_automation
from labs_deal_automation import labs_deal_creation
from login_automation import *
from retirement_investor_profile_automation import retirement_investor_profiles_automation
from signup_automation import *
from standard_deal_automation import standard_deal_creation
from trust_investor_profiles_automation import trust_investor_profiles_automation

# json_keys = json.loads(open(os.path.join('tests', 'CONSTANTS.json')).read())
# config = json.loads(open(os.path.join('tests', 'config.json'), 'r').read())
json_keys = json.loads(open('CONSTANTS.json', 'r').read())
config = json.loads(open('config.json', 'r').read())

if __name__ == "__main__":
    testCases_main = []
    driver = init_driver(driver_path)

    # Test Cases Start
    # print('Test Cases -- Organizer Login')
    # testCases_main.append(login_org())

    # print('Test Cases -- Organizer Signup')
    # testCases_main.append(signup_organizer())

    # # Labs Deal Creation
    # print('Test Cases -- Labs Deal Creation')
    # testCases_main.append(labs_deal_creation())

    # # Standard Deal Creation
    # print('Test Cases -- Standard Deal Creation')
    # testCases_main.append(standard_deal_creation())

    # # Inviting Investors
    # print('Test Cases -- Inviting Investors')
    # testCases_main.append(inviting_investors_automation())

    # # Inviting Investors
    # print('Test Cases -- Creating Individual Investor Profiles')
    # testCases_main.append(individual_investor_profiles_automation())

    # print('Test Cases -- Creating Entity Investor Profiles')
    # testCases_main.append(entity_investor_profiles_automation())

    # print('Test Cases -- Creating Trust Investor Profiles')
    # testCases_main.append(trust_investor_profiles_automation())

    # # InComplete
    # print('Test Cases -- Creating Joint Investor Profiles')
    # testCases_main.append(joint_investor_profiles_automation())

    # print('Test Cases -- Creating Retirement Investor Profiles')
    # testCases_main.append(retirement_investor_profiles_automation())

    # # Incomplete
    # print('Test Cases -- Editing a Deal')
    # testCases_main.append(edit_deal_automation())

    # Incomplete
    print('Test Cases -- Editing carry and management fee')
    testCases_main.append(edit_carry_n_mgmt_fees_automation())

    # # Incomplete
    # print('Test Cases -- Editing profiles on organizer side')
    # testCases_main.append(edit_profile_organizer_automation())

    # print('Test Cases -- Editing profiles on investor side')
    # testCases_main.append(edit_profile_investor_automation())

    # print('Test Cases -- Regenerate deal docs')
    # testCases_main.append(regen_deal_docs_automation())

    # print('Test Cases -- Upload documents to investor')
    # testCases_main.append(upload_docs_investor_auomation())

    # print('Test Cases -- Add side letter to investor')
    # testCases_main.append(add_side_letter_investor_automation())

    driver.quit() #Quiting the driver

    # Writing the test cases to a file
    save_file_name = "report" + config['outputFileType']

    # file_name = os.path.join(config['outputFolder'], save_file_name)
    file_name = os.path.join(save_file_name)

    if os.path.exists(file_name):
        file = open(file_name, "r+")
        file.truncate(0)
    else:
        file = open(file_name, "w")
    
    print('Writing the test cases to a file')
    for each in testCases_main:
        for case in each:
            file.write(case)

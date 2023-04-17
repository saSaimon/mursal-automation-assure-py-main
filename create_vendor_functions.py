'''
    Assure Frontend Automated QA Tests using Selenium
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
json_keys = json.loads(open('CONSTANTS.json', 'r').read())
config = json.loads(open('config.json', 'r').read())

try:
    config = json.loads(open(os.path.join('tests', 'config.json'), 'r').read())
    loginemail = config['login']
    password = config['password']
    driver_path = config['driver_path']
    base_url = config['base_url']
except Exception as e:
    print(str(e))

def create_vendor():
    testCases = []
    # Creating Vendor Test Cases
    create_vedor_keys = json_keys["CREATE_VENDORS_CASES"].keys()
    testCases.append(', Create Vendor Cases, \n')
    for case in create_vedor_keys:

        driver = init_driver(driver_path)
        driver.get(base_url)
        driver.maximize_window()

        # Declaring variables for Login
        admin_login(driver, 'CASE7')
        time.sleep(5) # Waiting for the page to load

        output = []
        output.append(create_vendor_values(driver=driver,current_case=case))

        try:
            for case_out in output:
                for result in case_out:
                    testCases.append(result + '\n') # Appending the test case to the list
                # testCases.append('\n')
        except Exception as e:
            testCases.append(','+str(e)+',\n')

        driver.close() # Closing the window for fresh test case everytime
        time.sleep(2)
    return testCases

def create_vendor_status():
    testCases = []
    #Test Cases to check the different status of the vendors during creation
    create_vedor_keys_status = json_keys["CREATE_VENDORS_CASES_STATUS"].keys()
    testCases.append(', Create Vendor Cases with Status, \n')
    for case in create_vedor_keys_status:
        # Initializing and starting the driver
        driver = init_driver(driver_path)
        driver.get(base_url)
        driver.maximize_window()

        #Login
        admin_login(driver, 'CASE7')
        time.sleep(4) # Waiting for the page to load

        # Declaring variables for Create Vendor
        output = []
        output.append(check_enabled_disabled(driver=driver,current_case=case))

        try:
            for result in output:
                for case_out in result:
                    testCases.append(case_out + '\n') # Appending the test case to the list
                # testCases.append('\n')
        except Exception as e:
            testCases.append(','+str(e)+',\n')

        driver.close() # Closing the window for fresh test case everytime
        time.sleep(2)
    return testCases

def create_vendor_validations():
    testCases = []
    #  Test Cases to check the different Validations of the vendors during creation
    testCases.append(', Create Vendor Cases with Field Validations, \n')
    create_vedor_keys_validations = json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"].keys()
    for case in create_vedor_keys_validations:
        # Initializing and starting the driver
        driver = init_driver(driver_path)
        driver.get(base_url)
        driver.maximize_window()

        #Login
        admin_login(driver, 'CASE7')
        time.sleep(5) # Waiting for the page to load

        # Declaring variables for Create Vendor
        output = []
        output.append(create_vendor_validation_check(driver=driver, current_case=case))

        try:
            for each in output:
                for case_out in each:
                    testCases.append(case_out) # Appending the test case to the list
                testCases.append('\n')
        except Exception as e:
            testCases.append(','+str(e)+',\n')

        driver.close() # Closing the window for fresh test case everytime
        time.sleep(2)
    return testCases

def create_vendor_cancel_button_func():
    testCases = []
    #  Test Cases to check the different Validations of the vendors during creation
    testCases.append(', Check Cancel Button, \n')
    create_vedor_keys_cancel = json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"].keys()
    for case in create_vedor_keys_cancel:
        # Initializing and starting the driver
        driver = init_driver(driver_path)
        driver.get(base_url)
        driver.maximize_window()

        #Login
        admin_login(driver, 'CASE7')
        time.sleep(5) # Waiting for the page to load

        # Declaring variables for Create Vendor
        output = []
        output.append(create_vendor_cancel_button(driver=driver, current_case=case))

        try:
            for each in output:
                for case_out in each:
                    testCases.append(case_out) # Appending the test case to the list
                testCases.append('\n')
        except Exception as e:
            testCases.append(','+str(e)+',\n')

        driver.close() # Closing the window for fresh test case everytime
        time.sleep(2)
    return testCases

def create_vendor_all_empty():
    testCases = []
    #  Test Cases to check the Reaction of page components on empty fields
    testCases.append(', Check All Empty Fields, \n')
    create_vedor_keys_cancel = json_keys["CREATE_VENDOR_EMPTY_FIELDS"].keys()
    for case in create_vedor_keys_cancel:
        # Initializing and starting the driver
        driver = init_driver(driver_path)
        driver.get(base_url)
        driver.maximize_window()

        #Login
        admin_login(driver, 'CASE7')
        time.sleep(5) # Waiting for the page to load

        # Declaring variables for Create Vendor
        output = []
        output.append(create_vendor_all_empty_fields(driver=driver, current_case=case))

        try:
            for each in output:
                for case_out in each:
                    testCases.append(case_out) # Appending the test case to the list
                testCases.append('\n')
        except Exception as e:
            testCases.append(','+str(e)+',\n')

        driver.close() # Closing the window for fresh test case everytime
        time.sleep(2)
    return testCases

def create_vendor_confirm_cancel():
    testCases = []
    #  Test Cases to check the confirmation modal on cancel click
    testCases.append(', Confirmation on Cancel Click, \n')
    create_vedor_keys_cancel = json_keys["CREATE_VENDOR_CANCEL_CONFIRMATION"].keys()
    for case in create_vedor_keys_cancel:
        # Initializing and starting the driver
        driver = init_driver(driver_path)
        driver.get(base_url)
        driver.maximize_window()

        #Login
        admin_login(driver, 'CASE7')
        time.sleep(5) # Waiting for the page to load

        # Declaring variables for Create Vendor
        output = []
        output.append(confirm_cancel_modal(driver=driver, current_case=case))

        try:
            for each in output:
                for case_out in each:
                    testCases.append(case_out) # Appending the test case to the list
                testCases.append('\n')
        except Exception as e:
            testCases.append(','+str(e)+',\n')

        driver.close() # Closing the window for fresh test case everytime
        time.sleep(2)
    return testCases

def create_vendor_success():
    testCases = []
    #  Test Cases to confirm the success modal on vendor creation
    testCases.append(', Successful Vendor Creation, \n')
    create_vedor_keys_cancel = json_keys["CREATE_VENDOR_SUCCESSFUL_VENDOR_CREATION"].keys()
    for case in create_vedor_keys_cancel:
        # Initializing and starting the driver
        driver = init_driver(driver_path)
        driver.get(base_url)
        driver.maximize_window()

        #Login
        admin_login(driver, 'CASE7')
        time.sleep(5) # Waiting for the page to load

        # Declaring variables for Create Vendor
        output = []
        output.append(success_vendor_creation(driver=driver, current_case=case))

        try:
            for each in output:
                for case_out in each:
                    testCases.append(case_out) # Appending the test case to the list
                testCases.append('\n')
        except Exception as e:
            testCases.append(','+str(e)+',\n')

        driver.close() # Closing the window for fresh test case everytime
        time.sleep(2)
    return testCases
import time
import datetime
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import os

# json_keys = json.loads(open(os.path.join('tests', 'CONSTANTS.json')).read())
# config = json.loads(open(os.path.join('tests', 'config.json'), 'r').read())
json_keys = json.loads(open('CONSTANTS.json', 'r').read())
config = json.loads(open('config.json', 'r').read())

def checkValue(field, value):
    if str(field.get_attribute('value')) == str(value):
        return 'PASSED'
    else:
        return 'FAILED'

def checkSelectValue(field, value):
    if str(field.text) == str(value):
        return 'PASSED'
    else:
        return 'FAILED'

# Function to return current date and time stamp
def getDateTime():
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    
def create_vendor_values(
    current_case='',
    driver='',
):
    '''Login to InstaCate using the given email and password'''

    description = json_keys["CREATE_VENDORS_CASES"][current_case]["DESCRIPTION"] # Description of the test case
    name = json_keys["CREATE_VENDORS_CASES"][current_case]["NAME"] # Name of the vendor
    unique_number = datetime.datetime.now().strftime("%Y%m%d%H%M%S") # Unique number for the vendor
    # Conditional initializing on Organization Number
    if json_keys["CREATE_VENDORS_CASES"][current_case]["ORGNo"] != "":
        org_number = json_keys["CREATE_VENDORS_CASES"][current_case]["ORGNo"]
    else:
        org_number = unique_number
    city = json_keys["CREATE_VENDORS_CASES"][current_case]["CITY"] # City of the vendor
    address = json_keys["CREATE_VENDORS_CASES"][current_case]["ADDRESS"] # Address of the vendor
    address_area = json_keys["CREATE_VENDORS_CASES"][current_case]["AREA"] # Address of the vendor
    postal_code = json_keys["CREATE_VENDORS_CASES"][current_case]["POSTAL_CODE"] # Postal Code of the vendor
    contact_person = json_keys["CREATE_VENDORS_CASES"][current_case]["CONTACTPERSON"] # Contact Person of the vendor
    # Conditional initializing on Contact Email Address
    if json_keys["CREATE_VENDORS_CASES"][current_case]["EMAILADDRESS"] != "":
        contact_email = json_keys["CREATE_VENDORS_CASES"][current_case]["EMAILADDRESS"]
    else:
        contact_email = unique_number + '@mailinator.com'
    contact_phone = json_keys["CREATE_VENDORS_CASES"][current_case]["CONTACT_NUMBER"] # Contact Number of the vendor
    password = json_keys["CREATE_VENDORS_CASES"][current_case]["PASSWORD"] # Password of the vendor
    confirm_password = json_keys["CREATE_VENDORS_CASES"][current_case]["PASSWORD2"] # Confirm Password of the vendor
    result = json_keys["CREATE_VENDORS_CASES"][current_case]["EXPECTED_RESULT"] # Expected Result of the test case

        
    try:
        test_result  = ''
        individual_result = []
        driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["SIDEBAR_VENDORS"]).click()
        driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["CREATE_VENDORS_BUTTON"]).click()

        input_name = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_NAME"])
        input_name.clear()
        input_name.send_keys(name)

        input_org_number = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_ORGNUMBER"])
        input_org_number.clear()
        input_org_number.send_keys(org_number)
        
        input_city = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CITY_VENDOR"])
        try:
            input_city.clear()
            input_city.send_keys(city)
        except Exception as e:
            pass

        input_address = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_ADDRESS"])
        input_address.clear()
        input_address.send_keys(address)

        input_postalcode = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_POSTAL_CODE"])
        input_postalcode.clear()
        input_postalcode.send_keys(postal_code)
        
        # Selecting the Address Area
        # Opening the Adress Area Dropdown
        dropdown_trigger = driver.find_element(By.CLASS_NAME, 'css-8mmkcg')
        dropdown_trigger.click()
        time.sleep(5)
        
        for i in range(0,100):
            current_option = driver.find_element(By.XPATH, '//*[@id="react-select-2-option-{}"]'.format(i))
            if current_option.text == address_area:
                current_option.click()
                break

        input_contatperson = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CONTACTPERSON"])
        input_contatperson.clear()
        input_contatperson.send_keys(contact_person)

        input_email = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_EMAILADDRESS"])
        input_email.clear()
        input_email.send_keys(contact_email)

        input_contactnumber = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CONTACTNUMBER"])
        input_contactnumber.clear()
        input_contactnumber.send_keys(contact_phone)

        input_password = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_PASS"])
        input_password.clear()
        input_password.send_keys(password)

        input_confirm_password = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_PASS2"])
        input_confirm_password.clear()
        input_confirm_password.send_keys(confirm_password)
        
        individual_result.append(getDateTime() + ', Input Name Working as Expected' + ', ' + checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_NAME"]), name))
        individual_result.append(getDateTime() + ', Input Org Number Working as Expected' + ', ' + checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_ORGNUMBER"]), org_number))
        individual_result.append(getDateTime() + ', Input City Working as Expected' + ', ' + checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CITY_VENDOR"]), city))
        individual_result.append(getDateTime() + ', Input Address Working as Expected' + ', ' + checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_ADDRESS"]), address))
        individual_result.append(getDateTime() + ', Input Postal Code Working as Expected' + ', ' + checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_POSTAL_CODE"]), postal_code))
        try:
            individual_result.append(getDateTime() + ', Input City Area is Working as Expected' + ', ' + checkSelectValue(driver.find_element(By.CLASS_NAME, json_keys["KEYS"]["CLASS_NAMES"]["SELECT_TEXT"]), address_area))
        except Exception as e:
            pass
        individual_result.append(getDateTime() + ', Input Contact Person Working as Expected' + ', ' + checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CONTACTPERSON"]), contact_person))
        individual_result.append(getDateTime() + ', Input Email Working as Expected' + ', ' + checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_EMAILADDRESS"]), contact_email))
        individual_result.append(getDateTime() + ', Input Contact Number Working as Expected' + ', ' + checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CONTACTNUMBER"]), contact_phone))
        individual_result.append(getDateTime() + ', Input Password Working as Expected' + ', ' + checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_PASS"]), password))
        individual_result.append(getDateTime() + ', Input Confirm Password Working as Expected' + ', ' + checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_PASS2"]), confirm_password))
        
        input_submit = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_SUBMIT"])
        input_submit.click()

        time.sleep(5)

        modal_heading = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]').text
        if modal_heading == 'DONE!':
            flag = 'SUCCESS'
        else:
            flag = 'FAILURE'

        if flag == result:
            test_result = description + ', PASSED'
        else:
            test_result = description + ', FAILED - ' + modal_heading

        final_result = []
        final_result.append(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ', ' + test_result)
        try:
            for result in individual_result:
                final_result.append(result)
        except Exception as e:
            print(str(e))

        return final_result
    except Exception as e:
        print(str(e))

def check_enabled_disabled(
    current_case='',
    driver='',
):
    '''Login to InstaCate using the given email and password'''

    description = json_keys["CREATE_VENDORS_CASES_STATUS"][current_case]["DESCRIPTION"] # Description of the test case
    name = json_keys["CREATE_VENDORS_CASES_STATUS"][current_case]["NAME"] # Name of the vendor
    unique_number = datetime.datetime.now().strftime("%Y%m%d%H%M%S") # Unique number for the vendor
    # Conditional initializing on Organization Number
    if json_keys["CREATE_VENDORS_CASES_STATUS"][current_case]["ORGNo"] != "":
        org_number = json_keys["CREATE_VENDORS_CASES_STATUS"][current_case]["ORGNo"]
    else:
        org_number = unique_number
    city = json_keys["CREATE_VENDORS_CASES_STATUS"][current_case]["CITY"] # City of the vendor
    address = json_keys["CREATE_VENDORS_CASES_STATUS"][current_case]["ADDRESS"] # Address of the vendor
    address_area = json_keys["CREATE_VENDORS_CASES_STATUS"][current_case]["AREA"] # Address of the vendor
    postal_code = json_keys["CREATE_VENDORS_CASES_STATUS"][current_case]["POSTAL_CODE"] # Postal Code of the vendor
    contact_person = json_keys["CREATE_VENDORS_CASES_STATUS"][current_case]["CONTACTPERSON"] # Contact Person of the vendor
    # Conditional initializing on Contact Email Address
    if json_keys["CREATE_VENDORS_CASES_STATUS"][current_case]["EMAILADDRESS"] != "":
        contact_email = json_keys["CREATE_VENDORS_CASES_STATUS"][current_case]["EMAILADDRESS"]
    else:
        contact_email = unique_number + '@mailinator.com'
    status = json_keys["CREATE_VENDORS_CASES_STATUS"][current_case]["STATUS"] # Status of the vendor
    contact_phone = json_keys["CREATE_VENDORS_CASES_STATUS"][current_case]["CONTACT_NUMBER"] # Contact Number of the vendor
    password = json_keys["CREATE_VENDORS_CASES_STATUS"][current_case]["PASSWORD"] # Password of the vendor
    confirm_password = json_keys["CREATE_VENDORS_CASES_STATUS"][current_case]["PASSWORD2"] # Confirm Password of the vendor
    result = json_keys["CREATE_VENDORS_CASES_STATUS"][current_case]["EXPECTED_RESULT"] # Expected Result of the test case

    try:
        test_result  = ''
        individual_result = []
        driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["SIDEBAR_VENDORS"]).click()
        driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["CREATE_VENDORS_BUTTON"]).click()

        input_name = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_NAME"])
        input_name.clear()
        input_name.send_keys(name)

        input_org_number = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_ORGNUMBER"])
        input_org_number.clear()
        input_org_number.send_keys(org_number)
        
        input_city = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CITY_VENDOR"])
        try:
            input_city.clear()
            input_city.send_keys(city)
        except Exception as e:
            pass

        input_address = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_ADDRESS"])
        input_address.clear()
        input_address.send_keys(address)

        input_postalcode = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_POSTAL_CODE"])
        input_postalcode.clear()
        input_postalcode.send_keys(postal_code)
        
        # Selecting the Address Area
        # Opening the Adress Area Dropdown
        dropdown_trigger = driver.find_element(By.CLASS_NAME, 'css-8mmkcg')
        dropdown_trigger.click()
        time.sleep(2)
        
        for i in range(0,100):
            current_option = driver.find_element(By.XPATH, '//*[@id="react-select-2-option-{}"]'.format(i))
            if current_option.text == address_area:
                current_option.click()
                break

        input_contatperson = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CONTACTPERSON"])
        input_contatperson.clear()
        input_contatperson.send_keys(contact_person)

        input_email = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_EMAILADDRESS"])
        input_email.clear()
        input_email.send_keys(contact_email)

        input_status = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_STATUS"])
        input_status.click()
        time.sleep(1)
        if(status == 'Enabled'):
            driver.find_element(By.ID, 'status_enabled').click()
        elif (status == 'Disabled'):
            driver.find_element(By.ID, 'status_disabled').click()
        time.sleep(1)

        input_contactnumber = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CONTACTNUMBER"])
        input_contactnumber.clear()
        input_contactnumber.send_keys(contact_phone)

        input_password = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_PASS"])
        input_password.clear()
        input_password.send_keys(password)

        input_confirm_password = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_PASS2"])
        input_confirm_password.clear()
        input_confirm_password.send_keys(confirm_password)

        individual_result.append(getDateTime() + ', Input Status Working as Expected' + ', ' + checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_STATUS"]), status.lower()))   
        input_submit = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_SUBMIT"])
        input_submit.click()

        time.sleep(5)
        
        modal_heading = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]').text
        if modal_heading == 'DONE!':
            flag = 'SUCCESS'
        else:
            flag = 'FAILURE'

        if flag == result:
            test_result = description + ', PASSED'
        else:
            test_result = description + ', FAILED - ' + modal_heading

        final_result = []
        final_result.append(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ', ' + test_result)
        for result in individual_result:
            final_result.append(result)

        return final_result
    except Exception as e:
        print(str(e))

def create_vendor_validation_check(
    current_case='',
    driver='',
):
    '''Login to InstaCate using the given email and password'''
    description = json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["DESCRIPTION"] # Description of the test case
    name = json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["NAME"] # Name of the vendor
    unique_number = datetime.datetime.now().strftime("%Y%m%d%H%M%S") # Unique number for the vendor
    # Conditional initializing on Organization Number
    if json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["ORGNo"] == "None":
        org_number = ""
    elif json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["ORGNo"] == "":
        org_number = unique_number
    else:
        org_number = json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["ORGNo"]
    city = json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["CITY"] # City of the vendor
    address = json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["ADDRESS"] # Address of the vendor
    address_area = json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["AREA"] # Address of the vendor
    postal_code = json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["POSTAL_CODE"] # Postal Code of the vendor
    contact_person = json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["CONTACTPERSON"] # Contact Person of the vendor
    # Conditional initializing on Contact Email Address
    if json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["EMAILADDRESS"] == "None":
        contact_email = ""
    elif json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["EMAILADDRESS"] == "":
        contact_email = unique_number + '@mailinator.com'
    else:
        contact_email = json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["EMAILADDRESS"]
    contact_phone = json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["CONTACT_NUMBER"] # Contact Number of the vendor
    password = json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["PASSWORD"] # Password of the vendor
    confirm_password = json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["PASSWORD2"] # Confirm Password of the vendor
    result = json_keys["CREATE_VENDORS_CASES_CHECK_VALIDATIONS"][current_case]["EXPECTED_RESULT"] # Expected Result of the test case

    try:
        empty_item = ''
        error_message = ''
        if name == '':
            empty_item = json_keys["KEYS"]["IDs"]["INPUT_NAME"]
        if org_number == '':
            empty_item = json_keys["KEYS"]["IDs"]["INPUT_ORGNUMBER"]
        if city == '':
            empty_item = json_keys["KEYS"]["IDs"]["INPUT_CITY_VENDOR"]
        if address == '':
            empty_item = json_keys["KEYS"]["IDs"]["INPUT_ADDRESS"]
        if postal_code == '':
            empty_item = json_keys["KEYS"]["IDs"]["INPUT_POSTAL_CODE"]
        if contact_person == '':
            empty_item = json_keys["KEYS"]["IDs"]["INPUT_CONTACTPERSON"]
        if contact_email == '':
            empty_item = json_keys["KEYS"]["IDs"]["INPUT_EMAILADDRESS"]
        if contact_phone == '':
            empty_item = json_keys["KEYS"]["IDs"]["INPUT_CONTACTNUMBER"]
        if password == '':
            empty_item = json_keys["KEYS"]["IDs"]["INPUT_PASS"]
        if confirm_password == '':
            empty_item = json_keys["KEYS"]["IDs"]["INPUT_PASS2"]

        test_result  = ''
        city_name_not_editable = False
        individual_result = []
        driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["SIDEBAR_VENDORS"]).click()
        driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["CREATE_VENDORS_BUTTON"]).click()

        input_name = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_NAME"])
        input_name.clear()
        input_name.send_keys(name)

        input_org_number = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_ORGNUMBER"])
        input_org_number.clear()
        input_org_number.send_keys(org_number)
        
        input_city = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CITY_VENDOR"])
        try:
            input_city.clear()
            input_city.send_keys(city)
        except Exception as e:
            city_name_not_editable = True

        input_address = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_ADDRESS"])
        input_address.clear()
        input_address.send_keys(address)

        input_postalcode = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_POSTAL_CODE"])
        input_postalcode.clear()
        input_postalcode.send_keys(postal_code)
        
        # Selecting the Address Area
        # Opening the Adress Area Dropdown
        if(address_area != ''):
            dropdown_trigger = driver.find_element(By.CLASS_NAME, 'css-8mmkcg')
            dropdown_trigger.click()
            time.sleep(3)
        
            for i in range(0,100):
                current_option = driver.find_element(By.XPATH, '//*[@id="react-select-2-option-{}"]'.format(i))
                if current_option.text == address_area:
                    current_option.click()
                    break

        input_contatperson = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CONTACTPERSON"])
        input_contatperson.clear()
        input_contatperson.send_keys(contact_person)

        input_email = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_EMAILADDRESS"])
        input_email.clear()
        input_email.send_keys(contact_email)

        input_contactnumber = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CONTACTNUMBER"])
        input_contactnumber.clear()
        input_contactnumber.send_keys(contact_phone)

        input_password = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_PASS"])
        input_password.clear()
        input_password.send_keys(password)

        input_confirm_password = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_PASS2"])
        input_confirm_password.clear()
        input_confirm_password.send_keys(confirm_password)

        input_submit = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_SUBMIT"])
        input_submit.click()

        if empty_item != '':
            try:
                error_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, empty_item))).get_attribute("validationMessage")
            except Exception as e:
                error_message = ''
        elif(address_area == ''):
            try:
                address_area_empty = driver.find_element(By.ID, 'swal2-html-container')
                time.sleep(3)
                error_message = address_area_empty.text
            except Exception as e:
                error_message = ''
        elif(empty_item == '' and password != '' and confirm_password != '' and password != confirm_password):
            time.sleep(3)
            try:
                error_message = driver.find_element(By.CLASS_NAME, 'error-message').text
            except Exception as e:
                error_message = ''
        elif(empty_item == '' and password != '' and confirm_password != '' and password == confirm_password and len(password) < 6 and len(confirm_password) <6):
            try:
                passwordLessThan6 = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'swal2-html-container'))).text
                if(passwordLessThan6 == "Password should be at least 6 characters (auth/weak-password)."):
                    error_message = passwordLessThan6
                else:
                    error_message = ''
            except Exception as e:
                error_message = ''
        elif(org_number != '' and org_number != "None"):
            try:
                error_message_org = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, 'error-message'))).text
                if(error_message_org == "Organization number already exists."):
                    error_message = error_message_org
                else:
                    error_message = ''
            except Exception as e:
                error_message = ''

        if error_message == '':
            flag = 'PASSED'
        else:
            flag = 'FAILED'

        if flag == result:
            test_result = description + ', PASSED'
        else:
            test_result = description + ', FAILED'

        final_result = []
        final_result.append(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ', ' + test_result)
        try:
            for result in individual_result:
                final_result.append(result)
        except Exception as e:
            print(str(e))

        print(final_result)
        return final_result
    except Exception as e:
        print(str(e))

def create_vendor_cancel_button(
    current_case='',
    driver='',
):
    '''Login to InstaCate using the given email and password'''
    description = json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["DESCRIPTION"] # Description of the test case
    name = json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["NAME"] # Name of the vendor
    unique_number = datetime.datetime.now().strftime("%Y%m%d%H%M%S") # Unique number for the vendor
    # Conditional initializing on Organization Number
    if json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["ORGNo"] == "None":
        org_number = ""
    elif json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["ORGNo"] == "":
        org_number = unique_number
    else:
        org_number = json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["ORGNo"]
    city = json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["CITY"] # City of the vendor
    address = json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["ADDRESS"] # Address of the vendor
    address_area = json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["AREA"] # Address of the vendor
    postal_code = json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["POSTAL_CODE"] # Postal Code of the vendor
    contact_person = json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["CONTACTPERSON"] # Contact Person of the vendor
    # Conditional initializing on Contact Email Address
    if json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["EMAILADDRESS"] == "None":
        contact_email = ""
    elif json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["EMAILADDRESS"] == "":
        contact_email = unique_number + '@mailinator.com'
    else:
        contact_email = json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["EMAILADDRESS"]
    contact_phone = json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["CONTACT_NUMBER"] # Contact Number of the vendor
    password = json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["PASSWORD"] # Password of the vendor
    confirm_password = json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["PASSWORD2"] # Confirm Password of the vendor
    result = json_keys["CREATE_VENDORS_CASES_CANCEL_BUTTON"][current_case]["EXPECTED_RESULT"] # Expected Result of the test case

    try:
        empty_item = ''
        error_message = ''

        test_result  = ''
        city_name_not_editable = False
        individual_result = []
        driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["SIDEBAR_VENDORS"]).click()
        driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["CREATE_VENDORS_BUTTON"]).click()

        cancel_button = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["CREATE_VENDORS_BUTTON"])
        cancel_button.click()

        time.sleep(3)

        create_button = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["CREATE_VENDORS_BUTTON"])
        if(create_button.text == "Create Vendor"):
            flag = 'SUCCESS'
        else:
            flag = 'FAILED'

        if flag == result:
            test_result = description + ', PASSED'
        else:
            test_result = description + ', FAILED'

        final_result = []
        final_result.append(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ', ' + test_result)
        try:
            for result in individual_result:
                final_result.append(result)
        except Exception as e:
            print(str(e))

        print(final_result)
        return final_result
    except Exception as e:
        print(str(e))

def create_vendor_all_empty_fields(
    current_case='',
    driver='',
):
    '''Login to InstaCate using the given email and password'''
    description = json_keys["CREATE_VENDOR_EMPTY_FIELDS"][current_case]["DESCRIPTION"] # Description of the test case
    name = json_keys["CREATE_VENDOR_EMPTY_FIELDS"][current_case]["NAME"] # Name of the vendor
    unique_number = datetime.datetime.now().strftime("%Y%m%d%H%M%S") # Unique number for the vendor
    # Conditional initializing on Organization Number
    if json_keys["CREATE_VENDOR_EMPTY_FIELDS"][current_case]["ORGNo"] != "":
        org_number = json_keys["CREATE_VENDOR_EMPTY_FIELDS"][current_case]["ORGNo"]
    else:
        org_number = unique_number
    city = json_keys["CREATE_VENDOR_EMPTY_FIELDS"][current_case]["CITY"] # City of the vendor
    address = json_keys["CREATE_VENDOR_EMPTY_FIELDS"][current_case]["ADDRESS"] # Address of the vendor
    address_area = json_keys["CREATE_VENDOR_EMPTY_FIELDS"][current_case]["AREA"] # Address of the vendor
    postal_code = json_keys["CREATE_VENDOR_EMPTY_FIELDS"][current_case]["POSTAL_CODE"] # Postal Code of the vendor
    contact_person = json_keys["CREATE_VENDOR_EMPTY_FIELDS"][current_case]["CONTACTPERSON"] # Contact Person of the vendor
    # Conditional initializing on Contact Email Address
    if json_keys["CREATE_VENDOR_EMPTY_FIELDS"][current_case]["EMAILADDRESS"] != "":
        contact_email = json_keys["CREATE_VENDOR_EMPTY_FIELDS"][current_case]["EMAILADDRESS"]
    else:
        contact_email = unique_number + '@mailinator.com'
    contact_phone = json_keys["CREATE_VENDOR_EMPTY_FIELDS"][current_case]["CONTACT_NUMBER"] # Contact Number of the vendor
    password = json_keys["CREATE_VENDOR_EMPTY_FIELDS"][current_case]["PASSWORD"] # Password of the vendor
    confirm_password = json_keys["CREATE_VENDOR_EMPTY_FIELDS"][current_case]["PASSWORD2"] # Confirm Password of the vendor
    result = json_keys["CREATE_VENDOR_EMPTY_FIELDS"][current_case]["EXPECTED_RESULT"] # Expected Result of the test case

    try:
        test_result  = ''
        individual_result = []
        driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["SIDEBAR_VENDORS"]).click()
        driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["CREATE_VENDORS_BUTTON"]).click()

        input_name = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_NAME"])
        input_name.clear()
        input_name.send_keys(name)

        input_org_number = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_ORGNUMBER"])
        input_org_number.clear()
        input_org_number.send_keys(org_number)
        
        input_city = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CITY_VENDOR"])
        try:
            input_city.clear()
            input_city.send_keys(city)
        except Exception as e:
            pass

        input_address = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_ADDRESS"])
        input_address.clear()
        input_address.send_keys(address)

        input_postalcode = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_POSTAL_CODE"])
        input_postalcode.clear()
        input_postalcode.send_keys(postal_code)

        input_contatperson = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CONTACTPERSON"])
        input_contatperson.clear()
        input_contatperson.send_keys(contact_person)

        input_email = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_EMAILADDRESS"])
        input_email.clear()
        input_email.send_keys(contact_email)

        input_contactnumber = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CONTACTNUMBER"])
        input_contactnumber.clear()
        input_contactnumber.send_keys(contact_phone)

        input_password = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_PASS"])
        input_password.clear()
        input_password.send_keys(password)

        input_confirm_password = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_PASS2"])
        input_confirm_password.clear()
        input_confirm_password.send_keys(confirm_password)
        
        fail_flag = False
        if (checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_NAME"]), name) == False):
            fail_flag = True
        elif (checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_ORGNUMBER"]), org_number) == False):
            fail_flag = True
        elif (checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CITY_VENDOR"]), city) == False):
            fail_flag = True
        elif (checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_ADDRESS"]), address) == False):
            fail_flag = True
        elif (checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_POSTAL_CODE"]), postal_code) == False):
            fail_flag = True
        elif (checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CONTACTPERSON"]), contact_person) == False):
            fail_flag = True
        elif (checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_EMAILADDRESS"]), contact_email) == False):
            fail_flag = True
        elif (checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CONTACTNUMBER"]), contact_phone) == False):
            fail_flag = True
        elif (checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_PASS"]), password) == False):
            fail_flag = True
        elif (checkValue(driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_PASS2"]), confirm_password) == False):
            fail_flag = True

        if (fail_flag == True):
            flag = 'SUCCESS'
        else:
            flag = 'FAILED'
        
        input_submit = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_SUBMIT"])
        input_submit.click()

        time.sleep(5)

        if flag == result:
            test_result = description + ', PASSED'
        else:
            test_result = description + ', FAILED'

        final_result = []
        final_result.append(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ', ' + test_result)
        try:
            for result in individual_result:
                final_result.append(result)
        except Exception as e:
            print(str(e))

        return final_result
    except Exception as e:
        print(str(e))

def success_vendor_creation(
    current_case='',
    driver='',
):
    '''Login to InstaCate using the given email and password'''

    description = json_keys["CREATE_VENDOR_SUCCESSFUL_VENDOR_CREATION"][current_case]["DESCRIPTION"] # Description of the test case
    name = json_keys["CREATE_VENDOR_SUCCESSFUL_VENDOR_CREATION"][current_case]["NAME"] # Name of the vendor
    unique_number = datetime.datetime.now().strftime("%Y%m%d%H%M%S") # Unique number for the vendor
    # Conditional initializing on Organization Number
    if json_keys["CREATE_VENDOR_SUCCESSFUL_VENDOR_CREATION"][current_case]["ORGNo"] != "":
        org_number = json_keys["CREATE_VENDOR_SUCCESSFUL_VENDOR_CREATION"][current_case]["ORGNo"]
    else:
        org_number = unique_number
    city = json_keys["CREATE_VENDOR_SUCCESSFUL_VENDOR_CREATION"][current_case]["CITY"] # City of the vendor
    address = json_keys["CREATE_VENDOR_SUCCESSFUL_VENDOR_CREATION"][current_case]["ADDRESS"] # Address of the vendor
    address_area = json_keys["CREATE_VENDOR_SUCCESSFUL_VENDOR_CREATION"][current_case]["AREA"] # Address of the vendor
    postal_code = json_keys["CREATE_VENDOR_SUCCESSFUL_VENDOR_CREATION"][current_case]["POSTAL_CODE"] # Postal Code of the vendor
    contact_person = json_keys["CREATE_VENDOR_SUCCESSFUL_VENDOR_CREATION"][current_case]["CONTACTPERSON"] # Contact Person of the vendor
    # Conditional initializing on Contact Email Address
    if json_keys["CREATE_VENDOR_SUCCESSFUL_VENDOR_CREATION"][current_case]["EMAILADDRESS"] != "":
        contact_email = json_keys["CREATE_VENDOR_SUCCESSFUL_VENDOR_CREATION"][current_case]["EMAILADDRESS"]
    else:
        contact_email = unique_number + '@mailinator.com'
    contact_phone = json_keys["CREATE_VENDOR_SUCCESSFUL_VENDOR_CREATION"][current_case]["CONTACT_NUMBER"] # Contact Number of the vendor
    password = json_keys["CREATE_VENDOR_SUCCESSFUL_VENDOR_CREATION"][current_case]["PASSWORD"] # Password of the vendor
    confirm_password = json_keys["CREATE_VENDOR_SUCCESSFUL_VENDOR_CREATION"][current_case]["PASSWORD2"] # Confirm Password of the vendor
    result = json_keys["CREATE_VENDOR_SUCCESSFUL_VENDOR_CREATION"][current_case]["EXPECTED_RESULT"] # Expected Result of the test case

        
    try:
        test_result  = ''
        individual_result = []
        driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["SIDEBAR_VENDORS"]).click()
        driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["CREATE_VENDORS_BUTTON"]).click()

        input_name = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_NAME"])
        input_name.clear()
        input_name.send_keys(name)

        input_org_number = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_ORGNUMBER"])
        input_org_number.clear()
        input_org_number.send_keys(org_number)
        
        input_city = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CITY_VENDOR"])
        try:
            input_city.clear()
            input_city.send_keys(city)
        except Exception as e:
            pass

        input_address = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_ADDRESS"])
        input_address.clear()
        input_address.send_keys(address)

        input_postalcode = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_POSTAL_CODE"])
        input_postalcode.clear()
        input_postalcode.send_keys(postal_code)
        
        # Selecting the Address Area
        # Opening the Adress Area Dropdown
        dropdown_trigger = driver.find_element(By.CLASS_NAME, 'css-8mmkcg')
        dropdown_trigger.click()
        time.sleep(3)
        
        for i in range(0,100):
            current_option = driver.find_element(By.XPATH, '//*[@id="react-select-2-option-{}"]'.format(i))
            if current_option.text == address_area:
                current_option.click()
                break

        input_contatperson = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CONTACTPERSON"])
        input_contatperson.clear()
        input_contatperson.send_keys(contact_person)

        input_email = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_EMAILADDRESS"])
        input_email.clear()
        input_email.send_keys(contact_email)

        input_contactnumber = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CONTACTNUMBER"])
        input_contactnumber.clear()
        input_contactnumber.send_keys(contact_phone)

        input_password = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_PASS"])
        input_password.clear()
        input_password.send_keys(password)

        input_confirm_password = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_PASS2"])
        input_confirm_password.clear()
        input_confirm_password.send_keys(confirm_password)
        
        input_submit = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_SUBMIT"])
        input_submit.click()

        time.sleep(5)

        modal_heading = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]').text
        if modal_heading == 'DONE!':
            flag = 'SUCCESS'
        else:
            flag = 'FAILURE'

        if flag == result:
            test_result = description + ', PASSED'
        else:
            test_result = description + ', FAILED - ' + modal_heading

        final_result = []
        final_result.append(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ', ' + test_result)
        try:
            for result in individual_result:
                final_result.append(result)
        except Exception as e:
            print(str(e))

        return final_result
    except Exception as e:
        print(str(e))

def confirm_cancel_modal(
    current_case='',
    driver='',
):
    '''Login to InstaCate using the given email and password'''

    description = json_keys["CREATE_VENDOR_CANCEL_CONFIRMATION"][current_case]["DESCRIPTION"] # Description of the test case
    name = json_keys["CREATE_VENDOR_CANCEL_CONFIRMATION"][current_case]["NAME"] # Name of the vendor
    unique_number = datetime.datetime.now().strftime("%Y%m%d%H%M%S") # Unique number for the vendor
    # Conditional initializing on Organization Number
    if json_keys["CREATE_VENDOR_CANCEL_CONFIRMATION"][current_case]["ORGNo"] != "":
        org_number = json_keys["CREATE_VENDOR_CANCEL_CONFIRMATION"][current_case]["ORGNo"]
    else:
        org_number = unique_number
    city = json_keys["CREATE_VENDOR_CANCEL_CONFIRMATION"][current_case]["CITY"] # City of the vendor
    address = json_keys["CREATE_VENDOR_CANCEL_CONFIRMATION"][current_case]["ADDRESS"] # Address of the vendor
    address_area = json_keys["CREATE_VENDOR_CANCEL_CONFIRMATION"][current_case]["AREA"] # Address of the vendor
    postal_code = json_keys["CREATE_VENDOR_CANCEL_CONFIRMATION"][current_case]["POSTAL_CODE"] # Postal Code of the vendor
    contact_person = json_keys["CREATE_VENDOR_CANCEL_CONFIRMATION"][current_case]["CONTACTPERSON"] # Contact Person of the vendor
    # Conditional initializing on Contact Email Address
    if json_keys["CREATE_VENDOR_CANCEL_CONFIRMATION"][current_case]["EMAILADDRESS"] != "":
        contact_email = json_keys["CREATE_VENDOR_CANCEL_CONFIRMATION"][current_case]["EMAILADDRESS"]
    else:
        contact_email = unique_number + '@mailinator.com'
    contact_phone = json_keys["CREATE_VENDOR_CANCEL_CONFIRMATION"][current_case]["CONTACT_NUMBER"] # Contact Number of the vendor
    password = json_keys["CREATE_VENDOR_CANCEL_CONFIRMATION"][current_case]["PASSWORD"] # Password of the vendor
    confirm_password = json_keys["CREATE_VENDOR_CANCEL_CONFIRMATION"][current_case]["PASSWORD2"] # Confirm Password of the vendor
    result = json_keys["CREATE_VENDOR_CANCEL_CONFIRMATION"][current_case]["EXPECTED_RESULT"] # Expected Result of the test case

    try:
        test_result  = ''
        individual_result = []
        driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["SIDEBAR_VENDORS"]).click()
        driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["CREATE_VENDORS_BUTTON"]).click()

        input_name = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_NAME"])
        input_name.clear()
        input_name.send_keys(name)

        input_org_number = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_ORGNUMBER"])
        input_org_number.clear()
        input_org_number.send_keys(org_number)
        
        input_city = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CITY_VENDOR"])
        try:
            input_city.clear()
            input_city.send_keys(city)
        except Exception as e:
            pass

        input_address = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_ADDRESS"])
        input_address.clear()
        input_address.send_keys(address)

        input_postalcode = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_POSTAL_CODE"])
        input_postalcode.clear()
        input_postalcode.send_keys(postal_code)
        
        # Selecting the Address Area
        # Opening the Adress Area Dropdown
        dropdown_trigger = driver.find_element(By.CLASS_NAME, 'css-8mmkcg')
        dropdown_trigger.click()
        time.sleep(3)
        
        for i in range(0,100):
            current_option = driver.find_element(By.XPATH, '//*[@id="react-select-2-option-{}"]'.format(i))
            if current_option.text == address_area:
                current_option.click()
                break

        input_contatperson = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CONTACTPERSON"])
        input_contatperson.clear()
        input_contatperson.send_keys(contact_person)

        input_email = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_EMAILADDRESS"])
        input_email.clear()
        input_email.send_keys(contact_email)

        input_contactnumber = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_CONTACTNUMBER"])
        input_contactnumber.clear()
        input_contactnumber.send_keys(contact_phone)

        input_password = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_PASS"])
        input_password.clear()
        input_password.send_keys(password)

        input_confirm_password = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["INPUT_PASS2"])
        input_confirm_password.clear()
        input_confirm_password.send_keys(confirm_password)
        
        input_cancel = driver.find_element(By.ID, json_keys["KEYS"]["IDs"]["CREATE_VENDORS_BUTTON"])
        input_cancel.click()

        time.sleep(3)

        modal_heading = driver.find_element(By.CLASS_NAME, 'swal-text').text

        if modal_heading == 'Are you sure you want to leave this page?':
            flag = 'SUCCESS'
        else:
            flag = 'FAILURE'

        if flag == result:
            test_result = description + ', PASSED'
        else:
            test_result = description + ', FAILED - ' + modal_heading

        final_result = []
        final_result.append(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ', ' + test_result)
        try:
            for result in individual_result:
                final_result.append(result)
        except Exception as e:
            print(str(e))

        return final_result
    except Exception as e:
        print(str(e))

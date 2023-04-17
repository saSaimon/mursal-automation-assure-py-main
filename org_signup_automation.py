import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import datetime
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


# json_keys = json.loads(open(os.path.join('tests', 'CONSTANTS.json')).read())
# config = json.loads(open(os.path.join('tests', 'config.json'), 'r').read())
json_keys = json.loads(open('cases/signup_cases.json', 'r').read())
constants = json.loads(open('CONSTANTS.json', 'r').read())
config = json.loads(open('config.json', 'r').read())

driver_path = config['driver_path']
base_url = config['base_url']

def init_driver(driver_path):
    '''Initialize Webdriver and returns the driver object'''
    from selenium.webdriver.chrome.service import Service
    from selenium import webdriver

    service = Service(driver_path)
    # options = webdriver.Edge()
    driver = webdriver.Edge(service=service)
    return driver

# def init_driver(driver_path):
#     '''Initialize Webdriver and returns the driver object'''
#     from selenium.webdriver.chrome.service import Service
#     from selenium import webdriver
#     from webdriver_manager.chrome import ChromeDriverManager

#     options = webdriver.ChromeOptions() 
#     options.add_argument("--no-sandbox");
#     options.add_argument("--disable-dev-shm-usage");

#     options.add_argument('--headless')
#     options.add_argument('--disable-gpu')  # Last I checked this was necessary.
#     s=Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=s, options=options)
   
#     return driver


def org_signup(
    driver,
    current_case
):
    flag = 'FAILURE'
    test_result  = ''
    unique_number = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    print('--------------', current_case, '--------------')
    try:
        description = json_keys["SIGNUP_CASES"][current_case]["DESCRIPTION"]
        first_name = json_keys["SIGNUP_CASES"][current_case]["FIRST_NAME"]
        last_name = json_keys["SIGNUP_CASES"][current_case]["LAST_NAME"]
        if json_keys["SIGNUP_CASES"][current_case]["EMAIL"] != "":
            email = json_keys["SIGNUP_CASES"][current_case]["EMAIL"]
        else:
            email = unique_number
        phone = json_keys["SIGNUP_CASES"][current_case]["PHONE"]
        country = json_keys["SIGNUP_CASES"][current_case]["COUNTRY"]
        state = json_keys["SIGNUP_CASES"][current_case]["STATE"]
        postal_code = json_keys["SIGNUP_CASES"][current_case]["POSTAL_CODE"]
        date_of_birth = json_keys["SIGNUP_CASES"][current_case]["DATE_OF_BIRTH"]
        password = json_keys["SIGNUP_CASES"][current_case]["PASSWORD"]
        result = json_keys["SIGNUP_CASES"][current_case]["EXPECTED_RESULT"]

        signup_first_name = driver.find_element(By.ID, constants["KEYS"]["IDs"]["SIGNUP_FIRSTNAME"])
        signup_first_name.clear()
        signup_first_name.send_keys(first_name)

        signup_last_name = driver.find_element(By.ID, constants["KEYS"]["IDs"]["SIGNUP_LASTNAME"])
        signup_last_name.clear()
        signup_last_name.send_keys(last_name)

        signup_email = driver.find_element(By.ID, constants["KEYS"]["IDs"]["SIGNUP_EMAIL"])
        signup_email.clear()
        signup_email.send_keys("{email}@mailinator.com".format(email=email))

        signup_phone = driver.find_element(By.ID, constants["KEYS"]["IDs"]["SIGNUP_PHONE"])
        signup_phone.clear()
        signup_phone.send_keys(phone)

        signup_country = driver.find_element(By.ID, constants["KEYS"]["IDs"]["SIGNUP_COUNTRY"])
        signup_country.send_keys(Keys.CONTROL + "a")
        signup_country.send_keys(Keys.DELETE)
        signup_country.send_keys(country)
        signup_country.send_keys(Keys.ENTER)

        signup_state = driver.find_element(By.ID, constants["KEYS"]["IDs"]["SIGNUP_STATE"])
        signup_state.send_keys(Keys.CONTROL + "a")
        signup_state.send_keys(Keys.DELETE)
        signup_state.send_keys(state)
        signup_state.send_keys(Keys.ENTER)

        signup_postal_code = driver.find_element(By.ID, constants["KEYS"]["IDs"]["SIGNUP_POSTAL_CODE"])
        signup_postal_code.clear()
        signup_postal_code.send_keys(postal_code)

        signup_date_of_birth = driver.find_element(By.ID, constants["KEYS"]["IDs"]["SIGNUP_DOB"])
        signup_date_of_birth.clear()
        signup_date_of_birth.send_keys(date_of_birth)

        signup_password = driver.find_element(By.ID, constants["KEYS"]["IDs"]["SIGNUP_PASSWORD"])
        signup_password.clear()
        signup_password.send_keys(password)

        login_button = driver.find_element(By.ID, constants["KEYS"]["IDs"]["SIGNUP_SUBMIT_BUTTON"])
        login_button.click()

        # Wait until URL Changes
        print('----------------', {constants["URLs"]["TERMS_AND_CONDITIONS"]})
        WebDriverWait(driver, 10).until(EC.url_changes(base_url))
        # Wait until the Page loads
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, constants["KEYS"]["IDs"]["AGREE_TERMS_BUTTON"])))
        print('-------------------------')

        agree_tems_button = driver.find_element(By.ID, constants["KEYS"]["IDs"]["AGREE_TERMS_BUTTON"])
        agree_tems_button.click()

        updated_url = driver.current_url
        if (updated_url == constants["URLs"]["NEW_ACCOUNT_CREATED"]):
            flag = 'SUCCESS'
        else:
            flag = 'FAILURE'

        if(result):
            if (flag == result):
                test_result = description + ', PASSED'
            else:
                test_result = description + ', FAILED'


    except Exception as e:
        print(str(e))

    
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ', ' + test_result + '\n'
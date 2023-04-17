from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import datetime
import json


import os

# reports creation
if os.path.exists("tests/report.txt"):
    f = open("tests/report.txt", "r+")
    f.truncate(0)
else:
    f = open("tests/report.txt", "w")

options = webdriver.ChromeOptions() 
options.add_argument("--no-sandbox");
options.add_argument("--disable-dev-shm-usage");

options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, options=options )


json_keys = json.loads(open('tests/CONSTANTS.json').read())
login_cases_keys = json_keys["LOGIN_CASES"].keys()
vendor_create_keys = json_keys["CREATE_VENDORS_CASES"].keys()

driver.maximize_window()
driver.get(json_keys["URL_ADMIN_LOGIN"])

# Test cases for Login
login_email = driver.find_element(
    By.ID, json_keys["KEYS"]["IDs"]["LOGIN_EMAIL"])
login_password = driver.find_element(
    By.ID, json_keys["KEYS"]["IDs"]["LOGIN_PASSWORD"])
login_button = driver.find_element(
    By.TAG_NAME, json_keys["KEYS"]["TAG_NAMES"]["BUTTON"])


def appendValue(field, value):

    field.clear()
    field.send_keys(value)


for case in login_cases_keys:
    try:
        appendValue(login_email, json_keys["LOGIN_CASES"][case]["USERNAME"])
        appendValue(login_password,
                    json_keys["LOGIN_CASES"][case]["PASSWORD"])
        login_button.click()
        time.sleep(5)
        actual_result = ''
        if driver.current_url == "https://instacate-development-en-472ed.web.app/admin/orders":
            actual_result = 'SUCCESS'
        else:
            actual_result = 'FAILURE'

        if(actual_result == json_keys["LOGIN_CASES"][case]["EXPECTED_RESULT"]):
            print(
                f"{datetime.datetime.now()} - {json_keys['LOGIN_CASES'][case]['DESCRIPTION']} - PASSED")
            f.write(f"{datetime.datetime.now()} - {json_keys['LOGIN_CASES'][case]['DESCRIPTION']} - PASSED \n")
        else:
            print(
                f"{datetime.datetime.now()} - {json_keys['LOGIN_CASES'][case]['DESCRIPTION']} - FAILED")
            f.write(f"{datetime.datetime.now()} - {json_keys['LOGIN_CASES'][case]['DESCRIPTION']} - FAILED \n")
    except:
        print(
            f"{datetime.datetime.now()} - {json_keys['LOGIN_CASES'][case]['DESCRIPTION']} - FAILED")
        f.write(f"{datetime.datetime.now()} - {json_keys['LOGIN_CASES'][case]['DESCRIPTION']} - FAILED \n")

# f.write("END OF TEST")
driver.close()
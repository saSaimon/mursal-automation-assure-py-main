from gettext import find
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
json_keys = json.loads(open('cases/edit_carry_n_mgmt_fees.json', 'r').read())
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


def edit_carry_n_mgmt_fees(
    driver,
    current_case
):
    flag = 'FAILURE'
    test_result  = ''
    unique_number = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    # print('--------------', current_case, '--------------')
    try:

        print("EDIT DEAL WORKING")

        deal_container = driver.find_elements(By.ID, "investment-detail_container")
        # Click on first element of deal_container
        deal_container[0].click()

        time.sleep(5)

        all_h6 = driver.find_elements(By.TAG_NAME, "h6")
        for h6 in all_h6:
            if h6.text == "Carry":
                h6.click()
                break
        # Press Down Key
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

        time.sleep(2)

        # Click on Edit Deal
        edit_deal_button = driver.find_element(By.ID, "carry-edit")
        edit_deal_button.click()

        time.sleep(2)

        # Click on Carry N Management Fees
        carry_input = driver.find_element(By.NAME, "flat")
        # Press Back Space 3 times
        carry_input.send_keys(Keys.BACK_SPACE)
        carry_input.send_keys(Keys.BACK_SPACE)
        carry_input.send_keys(Keys.BACK_SPACE)
        # Enter new value
        carry_input.send_keys(5)

        all_span = driver.find_elements(By.TAG_NAME, "span")
        for span in all_span:
            if span.text == "Save and close":
                span.click()
                break

        time.sleep(2)

        # Edit Management Fees
        # Page Up
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)

        time.sleep(2)

        all_h6 = driver.find_elements(By.TAG_NAME, "h6")
        for h6 in all_h6:
            if h6.text == "Management fees":
                h6.click()
                break
        
        # Press Down Key
        driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)
        driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)

        time.sleep(2)

        all_buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in all_buttons:
            if button.text == "Edit Deal":
                button.click()
                break

        print('--------')

        percent_input = driver.find_element(By.NAME, "percent")
        # Press Back Space 3 times
        percent_input.send_keys(Keys.BACK_SPACE)
        percent_input.send_keys(Keys.BACK_SPACE)
        percent_input.send_keys(Keys.BACK_SPACE)
        # Enter new value
        percent_input.send_keys(7)

        all_spans = driver.find_elements(By.TAG_NAME, "span")
        for span in all_spans:
            if span.text == "Save and close":
                span.click()
                break
        
        description = json_keys['EDIT_CARRY_N_MGMT_FEES'][current_case]['DESRIPTION']
        result = json_keys["EDIT_CARRY_N_MGMT_FEES"][current_case]["EXPECTED_RESULT"]

        if (flag == result):
            test_result = description + ', PASSED'
        else:
            test_result = description + ', FAILED'


    except Exception as e:
        print(str(e))
        return json_keys['EDIT_CARRY_N_MGMT_FEES'][current_case]['DESRIPTION'] + ', FAILED'

    
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ', ' + test_result + '\n'
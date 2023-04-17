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
json_keys = json.loads(open('cases/invite_investors.json', 'r').read())
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


def invite_investors(
    driver,
    current_case
):
    flag = 'FAILURE'
    test_result  = ''
    unique_number = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    # print('--------------', current_case, '--------------')
    try:

        deal_container = driver.find_elements(By.ID, "investment-detail_container")
        # Click on first element of deal_container
        deal_container[0].click()

        time.sleep(5)

        spans = driver.find_elements(By.TAG_NAME, "span")
        for span in spans:
            if span.text == 'Invite':
                span.click()
                break
        
        h4s = driver.find_elements(By.TAG_NAME, "h4")
        for h4 in h4s:
            if h4.text == 'Invite investors to this deal':
                h4.click()
                break

        input_email = driver.find_element(By.TAG_NAME, "input")
        input_email.send_keys("mursalfurqan@gmail.com")

        send_invite_btn = driver.find_element(By.ID, "ar-btn-send-invite")
        send_invite_btn.click()

        time.sleep(10)

        all_Ps = driver.find_elements(By.TAG_NAME, "p")
        for p in all_Ps:
            if p.text == 'Done. View deal in dashboard':
                p.click()
                test_result = 'PASS'
                flag = 'SUCCESS'
                break

        description = json_keys['INVITE_INVESTORS'][current_case]['DESRIPTION']
        result = json_keys["INVITE_INVESTORS"][current_case]["EXPECTED_RESULT"]

        if (flag == result):
            test_result = description + ', PASSED'
        else:
            test_result = description + ', FAILED'


    except Exception as e:
        print(str(e))

    
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ', ' + test_result + '\n'
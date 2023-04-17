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
json_keys = json.loads(open('cases/edit_profile_organizer.json', 'r').read())
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


def edit_profile_orgaziner(
    driver,
    current_case
):
    flag = 'FAILURE'
    test_result  = ''
    unique_number = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    # print('--------------', current_case, '--------------')
    try:

        print("EDIT DEAL WORKING")

        all_Ps = driver.find_element(By.ID, 'basic-button')
        all_Ps.click()
        # for ps in all_Ps:
        #     print('---------', ps.text)
        #     if ps.text == 'Settings':
        #         ps.click()
        #         break

        all_li = driver.find_elements(By.TAG_NAME, 'li')
        for li in all_li:
            if li.text == 'Profiles':
                li.click()
                break

        # all_h5s = driver.find_elements(By.TAG_NAME, 'h5')
        # for h5 in all_h5s:
        #     if h5.text == 'Profiles':
        #         h5.click()
        #         break

        time.sleep(200)

        # # description = json_keys['INVITE_INVESTORS'][current_case]['DESRIPTION']
        # # result = json_keys["INVITE_INVESTORS"][current_case]["EXPECTED_RESULT"]

        # # if (flag == result):
        # #     test_result = description + ', PASSED'
        # # else:
        # #     test_result = description + ', FAILED'


    except Exception as e:
        print(str(e))

    
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ', ' + test_result + '\n'
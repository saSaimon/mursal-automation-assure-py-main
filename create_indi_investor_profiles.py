from gettext import find
import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import datetime
import os
from selenium.webdriver.support import wait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


# json_keys = json.loads(open(os.path.join('tests', 'CONSTANTS.json')).read())
# config = json.loads(open(os.path.join('tests', 'config.json'), 'r').read())
json_keys = json.loads(open('cases/create_investor_profiles.json', 'r').read())
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


def create_indi_investor_profiles(
    driver,
    current_case
):
    flag = 'FAILURE'
    test_result  = ''
    unique_number = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    # print('--------------', current_case, '--------------')
    try:
        time.sleep(10)
        deal_container = driver.find_elements(By.ID, "investment-detail_container")
        # Click on first element of deal_container        
        deal_container[0].click()

        # wait untill the element is visible
        time.sleep(10)

        invest_now_btn = driver.find_element(By.ID, "invest-now")
        invest_now_btn.click()

        create_new_profile = driver.find_element(By.ID, "investor-create-new-profile")
        create_new_profile.click()

        time.sleep(5)

        input_first_name = driver.find_element(By.NAME, "name")
        if input_first_name.text == '':
            input_first_name.send_keys(json_keys['CREATE_INVESTOR_INDIVIDUAL_PROFILES'][current_case]['FIRST_NAME'])

        input_last_name = driver.find_element(By.NAME, "lastName")
        if input_last_name.text == '':
            input_last_name.send_keys(json_keys['CREATE_INVESTOR_INDIVIDUAL_PROFILES'][current_case]['LAST_NAME'])

        # input_email = driver.find_element(By.NAME, "email")
        # if input_email.text == '':
        #     input_email.send_keys(json_keys['CREATE_INVESTOR_INDIVIDUAL_PROFILES'][current_case]['EMAIL'])

        input_address1 = driver.find_element(By.NAME, "address1")
        if input_address1.text == '':
            input_address1.send_keys(json_keys['CREATE_INVESTOR_INDIVIDUAL_PROFILES'][current_case]['ADDRESS1'])

        input_address2 = driver.find_element(By.NAME, "address2")
        if input_address2.text == '':
            input_address2.send_keys(json_keys['CREATE_INVESTOR_INDIVIDUAL_PROFILES'][current_case]['ADDRESS2'])
        
        input_city = driver.find_element(By.NAME, "city")
        if input_city.text == '':
            input_city.send_keys(json_keys['CREATE_INVESTOR_INDIVIDUAL_PROFILES'][current_case]['CITY'])

        signup_state = driver.find_element(By.NAME, "state")
        signup_state.send_keys(Keys.CONTROL + "a")
        signup_state.send_keys(Keys.DELETE)
        signup_state.send_keys("Alabama")
        signup_state.send_keys(Keys.ENTER)
        # signup_state.send_keys(Keys.TAB)

        input_postalCode = driver.find_element(By.NAME, "postalCode")
        if input_postalCode.text == '':
            input_postalCode.send_keys(json_keys['CREATE_INVESTOR_INDIVIDUAL_PROFILES'][current_case]['POSTAL_CODE'])
        
        input_date_of_birth = driver.find_element(By.NAME, "dateOfBirth")
        if input_date_of_birth.text == '':
            input_date_of_birth.send_keys(json_keys['CREATE_INVESTOR_INDIVIDUAL_PROFILES'][current_case]['DATE_OF_BIRTH'])

        radio_button_US_Citizen = driver.find_elements(By.NAME, "usCItizen")
        for radio in radio_button_US_Citizen:
            if radio.get_attribute('value') == 'yes':
                radio.click()
        
        input_ssn = driver.find_element(By.NAME, "ssnNumber")
        if input_ssn.text == '':
            input_ssn.send_keys(json_keys['CREATE_INVESTOR_INDIVIDUAL_PROFILES'][current_case]['SSN'])

        submit_btn = driver.find_element(By.ID, "submit--individual-profile")
        submit_btn.click()

        time.sleep(5)

        all_h5s = driver.find_elements(By.TAG_NAME, "h5")
        for h5 in all_h5s:
            if h5.text == 'Investor Accreditation':
                h5.click()
                break

        # Scroll Down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        first_select_checkbox = driver.find_element(By.ID, "check-box-1")
        first_select_checkbox.click()

        for h5 in all_h5s:  
            if h5.text == 'Qualified Purchaser':
                h5.click()
                break
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        second_select_checkbox = driver.find_element(By.ID, "check-box-5")
        second_select_checkbox.click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        third_select_checkbox = driver.find_element(By.ID, "check-box-14")
        third_select_checkbox.click()

        all_spans = driver.find_elements(By.TAG_NAME, "span")
        for span in all_spans:
            if span.text == 'Create profile':
                span.click()
                break

        time.sleep(200)
        
        # h4s = driver.find_elements(By.TAG_NAME, "h4")
        # for h4 in h4s:
        #     if h4.text == 'Invite investors to this deal':
        #         h4.click()
        #         break

        # input_email = driver.find_element(By.TAG_NAME, "input")
        # input_email.send_keys("mursalfurqan@gmail.com")

        # send_invite_btn = driver.find_element(By.ID, "ar-btn-send-invite")
        # send_invite_btn.click()

        # time.sleep(5)
        # all_Ps = driver.find_elements(By.TAG_NAME, "p")
        # for p in all_Ps:
        #     if p.text == 'Done. View deal in dashboard':
        #         p.click()
        #         test_result = 'PASS'
        #         flag = 'SUCCESS'
        #         break

        # description = json_keys['INVITE_INVESTORS'][current_case]['DESRIPTION']
        # result = json_keys["INVITE_INVESTORS"][current_case]["EXPECTED_RESULT"]

        # if (flag == result):
        #     test_result = description + ', PASSED'
        # else:
        #     test_result = description + ', FAILED'


    except Exception as e:
        print(str(e))

    
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ', ' + test_result + '\n'
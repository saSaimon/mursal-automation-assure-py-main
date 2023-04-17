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
json_keys = json.loads(open('cases/labs_deal_create_cases.json', 'r').read())
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


def labs_deal_create(
    driver,
    current_case
):
    flag = 'FAILURE'
    test_result  = ''
    unique_number = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    # print('--------------', current_case, '--------------')
    print('WORKING DAMN Hawtly')
    try:

        description = json_keys['LABS_DEAL_CREATE_CASES'][current_case]['DESCRIPTION']

        new_deal_button = constants["KEYS"]["IDs"]["NEW_DEAL_BUTTON"]
        new_deal_button = driver.find_element_by_id(new_deal_button)
        new_deal_button.click()

        # Wait until the visibilty
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, constants["KEYS"]["IDs"]["DEAL_PROFILE_DROPDOWN"])))
        deal_profile_dropdown = driver.find_element(By.ID, constants["KEYS"]["IDs"]["DEAL_PROFILE_DROPDOWN"])
        deal_profile_dropdown.click()

        # Selecting the Deal Profile
        deal_profile_dropdown_options = constants["KEYS"]["TAG_NAMES"]["LIST_ITEM"]
        deal_profile_dropdown_options = driver.find_elements(By.TAG_NAME, deal_profile_dropdown_options)
        for each_option in deal_profile_dropdown_options:
            if each_option.text == "TestOrgFn - INDIVIDUAL":
                each_option.click()
                break
        
        time.sleep(2)

        close_deal_renewal_notice = driver.find_elements(By.TAG_NAME, "p")
        for each_p in close_deal_renewal_notice:
            if each_p.text == "Close":
                each_p.click()
                break
        
        # Scroll Down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Press Page Down Key
        # driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)

        select_labs_deal = driver.find_element(By.ID, constants["KEYS"]["IDs"]["SELECT_LABS_DEAL"])
        select_labs_deal.click()

        enter_deal_details = driver.find_element(By.ID, constants["KEYS"]["IDs"]["ENTER_DEAL_DETAILS"])
        enter_deal_details.click()

        deal_name = json_keys["LABS_DEAL_CREATE_CASES"][current_case]["DEAL_NAME"]
        inputs = driver.find_elements(By.TAG_NAME, "input")
        for each_input in inputs:
            # Print Placeholders
            if each_input.get_attribute("placeholder") == "Enter your deal name here":
                each_input.send_keys(deal_name, unique_number)
                break
        
        editable_divs = driver.find_elements(By.TAG_NAME, "div")
        for each_div in editable_divs:
            if each_div.get_attribute("contenteditable") == "true":
                each_div.send_keys("Testing Description on ", unique_number)
                break
        
        # Scroll Down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        for each_input in inputs:
            # Print Placeholders
            if each_input.get_attribute("placeholder") == "$500,000":
                each_input.send_keys("5000000")
                break

        min_investment = driver.find_element(By.NAME, "minInvestmentAmount")
        min_investment.send_keys("5000")

        org_carry_percent = driver.find_element(By.NAME, "organizerCarryPercentage")
        org_carry_percent.send_keys("10")

        estimatedCloseDate = driver.find_element(By.NAME, "estimatedCloseDate")
        estimatedCloseDate.send_keys("01012024")

        gen_doc_btn = driver.find_element(By.ID, "ar-btn-generate-doc")
        gen_doc_btn.click()
        time.sleep(10)
        # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "swal-button swal-button--confirm")))

        swal_ok_btn = driver.find_element(By.CLASS_NAME, "swal-button--confirm")
        swal_ok_btn.click()

        time.sleep(15)

        check_id = driver.find_element(By.ID, "ar-check-reveiew-acceptance")
        check_id.click()

        # scroll down
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        approve_cont_btn = driver.find_element(By.ID, "ar-btn-approve-continue")
        approve_cont_btn.click()

        time.sleep(2)

        h5s = driver.find_elements(By.TAG_NAME, "h5")
        for each_h5 in h5s:
            if each_h5.text == "Skip this step.":
                each_h5.click()
                break

        test_result = description, ', PASSED'
        return test_result

    except Exception as e:
        print(str(e))

    
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ', ' + test_result + '\n'
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
json_keys = json.loads(open('cases/create_trust_investor_profile.json', 'r').read())
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


def create_joint_investor_profiles(
    driver,
    current_case
):
    flag = 'FAILURE'
    test_result  = ''
    unique_number = datetime.datetime.now().strftime("%Y %m %d %H %M %S")
    # print('--------------', current_case, '--------------')
    try:
        description = 'Create Joint Investor Profile'

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

        allh6s =driver.find_elements(By.TAG_NAME, "h6")
        for h6 in allh6s:
            if h6.text == 'Joint':
                h6.click()
                break

        display_name = driver.find_element(By.NAME, "displayName")
        display_name.send_keys('Testing Joint Investor Profile on ' + unique_number)

        joint_name = driver.find_element(By.NAME, "name")
        joint_name.send_keys('Joint Acc Name ' + unique_number)

        first_name = driver.find_element(By.NAME, "firstName")
        if first_name.text == '':
            first_name.send_keys("Testing First Name")

        last_name = driver.find_element(By.NAME, "lastName")
        if last_name.text == '':
            last_name.send_keys("Testing Last Name")
            last_name.send_keys(Keys.TAB)

        title_name = driver.find_element(By.NAME, "title")
        if title_name.text == '':
            title_name.send_keys("Mr.")

        dob_name = driver.find_element(By.NAME, "dateOfBirth")
        if dob_name.text == '':
            dob_name.send_keys("01011990")
            dob_name.send_keys(Keys.PAGE_DOWN)

        address1_input = driver.find_element(By.NAME, "address1")
        address1_input.send_keys('Test Address 1')
        address1_input.send_keys(Keys.TAB)

        city_input = driver.find_element(By.NAME, "city")
        city_input.send_keys('Test City')

        signup_state = driver.find_element(By.NAME, "state")
        signup_state.send_keys(Keys.CONTROL + "a")
        signup_state.send_keys(Keys.DELETE)
        signup_state.send_keys("Alabama")
        signup_state.send_keys(Keys.ENTER)
        # signup_state.send_keys(Keys.TAB)

        input_postalCode = driver.find_element(By.NAME, "postalCode")
        if input_postalCode.text == '':
            input_postalCode.send_keys('12345')
            input_postalCode.send_keys(Keys.PAGE_DOWN)

        signatory_US_citizen = driver.find_elements(By.TAG_NAME, "h6")
        for i in signatory_US_citizen:
            if i.text == 'Yes':
                i.click()  
                break

        input_ssn = driver.find_element(By.NAME, "ssnNumber")
        if input_ssn.text == '':
            input_ssn.send_keys('123456789')

        signitory_req = driver.find_element(By.ID, "add--joint--signatory")
        signitory_req.click()

        time.sleep(5)
        print('-----------------------------------------------------')

        # first_name_signitory = driver.find_elements(By.TAG_NAME, "input")
        # for i in first_name_signitory:
        #     # if i's placeholder is First Name
        #     if i.get_attribute('placeholder') == 'First Name':
        #         i.send_keys("Testing First Name")

        # Focus on Element
        # driver.switch_to.active_element.send_keys(Keys.TAB)

        
        print('==============')
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.ID, "add-sig-fn")))

        demo = driver.find_element(By.ID, 'add-sig-fn')
        print('==============')
        demo.send_keys('HELLO')
        # demo.click()
        time.sleep(200)
        signitory_first_name = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div/form/div[1]/div[1]/div[1]/input")
        if signitory_first_name.text == '':
            signitory_first_name.send_keys("Testing First Name")

        time.sleep(200)

        signitory_last_name = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div/form/div[1]/div[2]/div/input")
        if signitory_last_name.text == '':
            signitory_last_name.send_keys("Testing Last Name")

        signitory_email_name = driver.find_element(By.XPATH, "/html/body/div[7]/div[3]/div/div[2]/div/form/div[2]/div/input")
        if signitory_email_name.text == '':
            signitory_email_name.send_keys("assure_joint_test@mailinator.com")

        all_spans = driver.find_elements(By.TAG_NAME, "span")
        for span in all_spans:
            print(span.text)
            # if span.text == 'Save':
            #     span.click()
            #     break
        time.sleep(2)
        print('----------------------')
        input_ssn.send_keys(Keys.PAGE_DOWN)

        all_spans_submit = driver.find_elements(By.TAG_NAME, "span")
        for span in all_spans_submit:
            if span.text == 'Next: Joint accreditation':
                span.click()
                break

        time.sleep(5)

        all_h5s = driver.find_elements(By.TAG_NAME, "h5")
        for h5 in all_h5s:
            if h5.text == 'Joint Accreditation':
                h5.click()
                break

        # Scroll Down
        first_select_checkbox = driver.find_element(By.ID, "check-box-1")
        first_select_checkbox.click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        for h5 in all_h5s:  
            if h5.text == 'Qualified Purchaser':
                h5.click()
                break

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        third_select_checkbox = driver.find_element(By.ID, "check-box-14")
        third_select_checkbox.click()

        buttons = driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            if button.text == 'Create profile':
                button.click()
                break

        test_result = description + ", PASSED"

    except Exception as e:
        print(str(e))
    
    return datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ', ' + test_result + '\n'
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


def edit_deal(
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

        # Press Down Key
        driver.find_element_by_tag_name('body').send_keys(Keys.DOWN)

        time.sleep(2)

        edit_detail_btn = driver.find_elements(By.TAG_NAME, 'button')

        # Select on button, whose Title attribute is Edit Deal
        for btn in edit_detail_btn:
            if btn.get_attribute('title') == 'Edit Deal':
                btn.click()
                break
        # Change focus to upper moddal
        # driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)

        print('-------------------------')

        all_inputs = driver.find_elements(By.TAG_NAME, 'input')
        for input in all_inputs:
            if input.get_attribute('value') == '$5,000,000':
                input.send_keys(11111111111111111111111)
                break

        # Find element with name = targetRaiseAmount and send_keys = 100
        # driver.find_element_by_name('targetRaiseAmount').send_keys('100')

        # all_inputs = driver.find_elements(By.TAG_NAME, 'input')
        # for input in all_inputs:
        #     if input.get_attribute('name') == 'targetRaiseAmount':
        #         input.send_keys('5555555555555')
        #         break
        # time.sleep(2)
        # target_amount = driver.find_element(By.NAME, 'targetRaiseAmount')
        # target_amount.clear()
        # target_amount.send_keys(30000000)
        driver.wait = WebDriverWait(driver, 10)
        target_amount = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'targetRaiseAmount')))
        target_amount.clear()
        target_amount.send_keys(30000000)

        min_investment = driver.find_element(By.FULL_XPATH, '/html/body/div[6]/div[3]/div/form/div[2]/div[4]/div[1]/div/input')
        min_investment.clear()
        min_investment.send_keys(3000000)

        estimate_closing_date = driver.find_element(By.NAME, 'estimatedCloseDate')
        estimate_closing_date.clear()
        estimate_closing_date.send_keys('01012025')

        all_spans = driver.find_elements(By.TAG_NAME, 'span')
        for span in all_spans:
            if span.text == 'Save and close':
                span.click()
                break

        time.sleep(5)

        # time.sleep(5)

        # spans = driver.find_elements(By.TAG_NAME, "span")
        # for span in spans:
        #     if span.text == 'Invite':
        #         span.click()
        #         break
        
        # h4s = driver.find_elements(By.TAG_NAME, "h4")
        # for h4 in h4s:
        #     if h4.text == 'Invite investors to this deal':
        #         h4.click()
        #         break

        # input_email = driver.find_element(By.TAG_NAME, "input")
        # input_email.send_keys("mursalfurqan@gmail.com")

        # send_invite_btn = driver.find_element(By.ID, "ar-btn-send-invite")
        # send_invite_btn.click()

        # time.sleep(10)

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
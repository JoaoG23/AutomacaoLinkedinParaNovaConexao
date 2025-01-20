
import os
from time import sleep
import traceback

from dotenv import load_dotenv

from httpcore import TimeoutException
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.common.exceptions import InvalidSelectorException

from connect_people.do_login.do_login import do_login
from connect_people.search_people_and_connect.search_people_and_connect import search_people_and_connect
from utils.logging.log_manager.log_manager import write_to_log
# from utils.wait_for_element_load.wait_for_element_load import wait_for_element_load

options = webdriver.ChromeOptions()
service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

load_dotenv()

    
if __name__ == '__main__':
    try:
        driver.maximize_window()
        
        user_login = {
            'email': os.getenv("USER_LINKEDIN"),
            'password': os.getenv("PASSWORD_LINKEDIN")
        }
        do_login(driver, user_login)
        search_data_people = {
            'description': os.getenv("DESCRIPTION"),
            'location': os.getenv("LOCATION")
        }
        sleep(12)
        
        search_people_and_connect(driver, search_data_people)
   
    except WebDriverException as e:
        write_to_log(f"WebDriverException: {traceback.format_exc()}", type='error')
    except NoSuchElementException as e:
        write_to_log(f"NoSuchElementException: {traceback.format_exc()}", type='error')
    except InvalidSelectorException as e:
        write_to_log(f"InvalidSelectorException: {traceback.format_exc()}", type='error')
    except TimeoutException as e:
        write_to_log(f"TimeoutException: {traceback.format_exc()}", type='error')
    except Exception as e:
        write_to_log(f"Exception: {traceback.format_exc()}", type='error')
    finally:
        print("Encerrando automação")
        driver.quit()   
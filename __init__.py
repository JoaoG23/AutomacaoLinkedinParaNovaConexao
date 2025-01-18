
import os
from time import sleep
import traceback

from dotenv import load_dotenv

from httpcore import TimeoutException
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSelectorException

from connect_people.do_login.do_login import do_login
from connect_people.encode_message_for_url.encode_message_for_url import encode_message_for_url
from connect_people.search_people.search_people import search_people
from utils.logging.log_manager.log_manager import write_to_log
from utils.wait_for_element_load.wait_for_element_load import wait_for_element_load
# from utils.move_to_file.move_to_file import move_to_file



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
        # wait_for_element_load()
        search_data_people = {
            'description': os.getenv("DESCRIPTION"),
            'location': os.getenv("LOCATION")
        }
        sleep(7)
        
        # description_encoded = encode_message_for_url(description_people)
            
        # driver.get(f'https://www.linkedin.com/search/results/people/?keywords=TECH&location=Sao%20Paulo')

        search_people(driver, search_data_people)
   
        
        # path_file_imports = os.path.join(os.getcwd(), 'import', 'jobs.csv')
        # path_file_export = os.path.join(os.getcwd(),'exported', 'datetime_now' +'.csv')
        
        # move_to_file(path_file_imports, path_file_export)
    except WebDriverException as e:
        write_to_log(f"WebDriverException: {traceback.format_exc()}", type='error')
    except InvalidSelectorException as e:
        write_to_log(f"InvalidSelectorException: {traceback.format_exc()}", type='error')
    except TimeoutException as e:
        write_to_log(f"TimeoutException: {traceback.format_exc()}", type='error')
    except Exception as e:
        write_to_log(f"Exception: {traceback.format_exc()}", type='error')
    finally:
        print("Encerrando automação")
        driver.quit()   
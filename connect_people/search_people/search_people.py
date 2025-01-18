from time import sleep
from connect_people.encode_message_for_url.encode_message_for_url import encode_message_for_url
from utils.wait_for_element_load.wait_for_element_load import wait_for_element_load
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_total_pages_of_search(driver):
    pages_box = driver.find_elements(By.CLASS_NAME, 'artdeco-pagination__pages--number')
    print(pages_box)
    # pages = pages_box.find_elements(By.TAG_NAME, "li") 
    # for page in pages:
    #     print(page.text)
    
def connect_people_to_page(driver):
    connect_recruiter_buttons = driver.find_elements(By.XPATH,"//*[text()='Conectar']")
    sleep(2)
    
    for connect_button in connect_recruiter_buttons:
        connect_button.click()
        sleep(3)
        no_send_note_button = driver.find_element(By.XPATH, "//*[text()='Enviar sem nota']")
        no_send_note_button.click()
        sleep(3)

def search_people(driver, information_people):
    
    sleep(7)
    wait_for_element_load(driver.find_elements(By.XPATH, '//*[@id="global-nav"]'), 'search results')   
     
    description_people = information_people['description']
    
    description_encoded = encode_message_for_url(description_people)
    sleep(1)
    
    
    
    driver.get(f'https://www.linkedin.com/search/results/people/?keywords={description_encoded}')
    sleep(12)
    get_total_pages_of_search(driver)
    # connect_recruiter_buttons = driver.find_elements(By.XPATH,"//*[text()='Conectar']")
    # sleep(2)
    
    # for connect_button in connect_recruiter_buttons:
    #     connect_button.click()
    #     sleep(3)
    #     no_send_note_button = driver.find_element(By.XPATH, "//*[text()='Enviar sem nota']")
    #     no_send_note_button.click()
    #     sleep(3)
    # while len(driver.find_elements(By.XPATH, '//*[@id="lightbox-cover"]')) < 1:
    #     sleep(2)
    # print("Login efetuado com sucesso.")
    # sleep(2)
    
    # user_input = driver.find_element(By.XPATH, '//*[@id="username"]')
    # sleep(1)
    # user_input.send_keys(email)
    # sleep(1)
    # password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    # sleep(1)
    # password_input.send_keys(password)
    # sleep(1)
    # login_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
    # sleep(1)
    # login_button.click()
    
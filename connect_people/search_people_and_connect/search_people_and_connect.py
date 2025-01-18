import os
from time import sleep
from connect_people.encode_message_for_url.encode_message_for_url import encode_message_for_url
from selenium.webdriver.common.by import By

from utils.logging.log_manager.log_manager import write_to_log

def connect_people_of_page(driver):
    connect_people_buttons = driver.find_elements(By.XPATH,"//*[text()='Conectar']")
    sleep(2)
    
    for connect_button in connect_people_buttons:
        connect_button.click()
        sleep(3)
        no_send_note_button = driver.find_element(By.XPATH, "//*[text()='Enviar sem nota']")
        no_send_note_button.click()
        sleep(3)
    return len(connect_people_buttons)

def search_people_and_connect(driver, information_people):
    
    description_people = information_people['description']
    
    description_encoded = encode_message_for_url(description_people)
    sleep(5)
    driver.get(f'https://www.linkedin.com/search/results/people/?keywords={description_encoded}')
    sleep(8)
    
    limit_connects = os.getenv("LIMIT_CONNECTIONS")
    quantity_people_connects = 0
    
    while quantity_people_connects < int(limit_connects):
        sleep(2)
        quantity_people_connects += connect_people_of_page(driver)
        sleep(2)
        next_page_button = driver.find_element(By.XPATH, '//*[@aria-label="Avançar"]')
        next_page_button.click()
        sleep(2)
    mgs = f"Total de conexões realizadas: {quantity_people_connects}"
    
    write_to_log(mgs, type='info')
    print(mgs)
    
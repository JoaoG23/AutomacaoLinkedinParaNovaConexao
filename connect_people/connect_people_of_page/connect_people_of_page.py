from time import sleep
from selenium.webdriver.common.by import By

from connect_people.verify_connection_required_email.verify_connection_required_email import verify_connection_required_email


def connect_people_of_page(driver):
    connect_people_buttons = driver.find_elements(By.XPATH,"//*[text()='Conectar']")
    sleep(2)
    
    for connect_button in connect_people_buttons:
        connect_button.click()
        sleep(2)
        verify_connection_required_email(driver)
    return len(connect_people_buttons)
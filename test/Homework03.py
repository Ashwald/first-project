import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def click_to_name_input():
    input_thing = driver.find_element(By.ID, "create-form:name-input")
    input_thing.click()


def type_to_name_input(name):
    input_thing = driver.find_element(By.ID, "create-form:name-input")
    input_thing.send_keys(name)


def click_to_header():
    cim = driver.find_element(By.XPATH, "//h1")
    cim.click()


def wait_for_error_message(msg):
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.CLASS_NAME, "invalid-feedback"), msg)
    )


def wait_for_monogram(expected_monogram):
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "create-form:monogram-text"), expected_monogram)
        # expected_conditions.element_to_be_clickable(By.ID, "create-form:monogram-text")
    )
    monogram = driver.find_element(By.ID, "create-form:monogram-text").text
    return monogram


def click_create_button():
    create_button = driver.find_element(By.ID, "create-form:save-button")
    create_button.click()


def type_card_number(card_start):
    expected_conditions.element_to_be_clickable((By.ID, "create-form:card-number-input"))
    card_code = card_start + str(time.time())
    # card_code = str(random.random() * 999)
    print(card_code)
    # card_code = "129"
    card_input_element = driver.find_element(By.ID, "create-form:card-number-input")
    card_input_element.click()
    card_input_element.send_keys(card_code)


def delete_by_name(name):
    name_xpath = "//tr[td[text()='name']]/*[last()]"
    delete_button = driver.find_element(By.XPATH, )

def find_id_by_name(name):



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome()
# driver.get("http://www.learnwebservices.com/empapp/create-employee.xhtml")
driver.get("http://www.learnwebservices.com/empapp/")

#click_to_name_input()

#click_to_header()

#wait_for_error_message("Name can not be empty!")

type_to_name_input("Joe James")
click_create_button()
type_card_number()
click_create_button()

# print(wait_for_monogram("JJ"))

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://www.yellowpages.com.au/search/listings?clue=Air+conditioning&locationClue=SA"
driver = None

def init(page_number):
    global url 
    global driver
    url = url + "&pageNumber=" + str(page_number)
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def find_box(driver):
    time.sleep(3)
    hidden_box = driver.find_elements(By.CLASS_NAME, "bXFSCz")
    return hidden_box

def get_name_element(number):
    global driver
    name_element = driver.find_elements(By.CLASS_NAME, "MuiTypography-displayBlock")[number]
    return name_element.text

def get_phone_element(number):
    global driver
    phone_element = driver.find_elements(By.CLASS_NAME, "fXPEMO")[number]
    return phone_element.text

def get_address_element(number):
    global driver
    address_element = driver.find_elements(By.CLASS_NAME, "MuiTypography-colorTextSecondary")[number+1]
    name, suburb, state = address_element.text.split(",")
    return (suburb + state).lstrip()

def get_state_name(number):
    global driver
    state = get_address_element(number).split(" ")[-2]
    return state


find_box(init(21))[0].click()
print(get_name_element(1))
print(get_phone_element(1))
print(get_address_element(1))
print(get_state_name(1))

# for i in find_box(init(21)):
#     print(i.text)
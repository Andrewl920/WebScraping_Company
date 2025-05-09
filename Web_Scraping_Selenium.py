from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

driver = None

def init(page_number):
    global driver
    url = "https://www.yellowpages.com.au/search/listings?clue=Electrican&locationClue=ACT"

    if page_number == 1:
        url = url
    else: 
        url = url + "&pageNumber=" + str(page_number)

    driver = webdriver.Chrome()
    driver.get(url)

    return driver

def find_large_container(number):
    global driver
    large_container = driver.find_elements(By.CLASS_NAME, "iOfhmk")[number]
    return large_container

def find_hidden_box():
    global driver
    time.sleep(3)
    hidden_box = driver.find_elements(By.CLASS_NAME, "bXFSCz")
    return hidden_box
    
def find_box():
    global driver
    time.sleep(3)
    # hidden_box = driver.find_elements(By.CLASS_NAME, "bXFSCz")
    box = driver.find_elements(By.CLASS_NAME, "enijwQ")
    
    return box

def find_hidden(container):
    global driver
    try:
        hidden_element = container.find_elements(By.CLASS_NAME, "bXFSCz")
        if hidden_element:
            return True
    except: 
        return False

def find_total_box():
    global driver
    list_box = find_box()
    return len(list_box)

def get_name_element(number):
    global driver
    name_element = driver.find_elements(By.CLASS_NAME, "MuiTypography-displayBlock")[number]
    return name_element.text

def get_phone_element(number):
    global driver
    time.sleep(3)
    container_element = driver.find_elements(By.CLASS_NAME, "enijwQ")[number]

    #seach the larger container
    try:
        phone_element = container_element.find_elements(By.CLASS_NAME, "ButtonPhone")[0].get_attribute("href")
        phone_element = phone_element.split(":")[1]
    except IndexError as e:
        phone_element = None

    return phone_element

def get_website_element(number):
    global driver
    time.sleep(3)
    #find the larger container
    container_element = driver.find_elements(By.CLASS_NAME, "enijwQ")[number]

    #search for the website button
    try:
        website_element = container_element.find_elements(By.CLASS_NAME, "ButtonWebsite")[0].get_attribute("href")
        return website_element
    except IndexError as e:
        website_element = None
        return website_element
    
def get_address_element(number):
    global driver
    address_element = driver.find_elements(By.CLASS_NAME, "MuiTypography-colorTextSecondary")[number]
    name, suburb, state = address_element.text.split(",")
    return (suburb + state).lstrip()

def get_state_name(number):
    global driver
    state = get_address_element(number).split(" ")[-2]
    return state

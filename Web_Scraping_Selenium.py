from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service

class WebScraping:
    def __init__(self, page_number = 1):
        self.driver = None
        self.service = Service(r"C:\Users\Administrator\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        self.driver = webdriver.Chrome()
        self.url = "https://www.yellowpages.com.au/search/listings?clue=Electrican&locationClue=TAS"

        if page_number == 1:
            self.url = self.url
        else: 
            self.url = self.url + "&pageNumber=" + str(page_number)

        self.driver.get(self.url)

    def find_large_container(self, number):
        large_container = self.driver.find_elements(By.CLASS_NAME, "iOfhmk")[number]
        return large_container

    def find_hidden_box(self):
        time.sleep(3)
        hidden_box = self.driver.find_elements(By.CLASS_NAME, "bXFSCz")
        return hidden_box
        
    def find_box(self):
        time.sleep(3)
        # hidden_box = driver.find_elements(By.CLASS_NAME, "bXFSCz")
        box = self.driver.find_elements(By.CLASS_NAME, "enijwQ")
        
        return box

    def find_hidden(self,  container):
        try:
            hidden_element = container.find_elements(By.CLASS_NAME, "bXFSCz")
            if hidden_element:
                return True
        except: 
            return False

    def find_total_box(self):
        list_box = self.find_box()
        return len(list_box)

    def get_name_element(self, number):
        name_element = self.driver.find_elements(By.CLASS_NAME, "MuiTypography-displayBlock")[number]
        return name_element.text

    def get_phone_element(self, number):
        time.sleep(3)
        container_element = self.driver.find_elements(By.CLASS_NAME, "enijwQ")[number]

        #seach the larger container
        try:
            phone_element = container_element.find_elements(By.CLASS_NAME, "ButtonPhone")[0].get_attribute("href")
            phone_element = phone_element.split(":")[1]
        except IndexError as e:
            phone_element = None

        return phone_element

    def get_website_element(self, number):
        time.sleep(3)
        #find the larger container
        container_element = self.driver.find_elements(By.CLASS_NAME, "enijwQ")[number]

        #search for the website button
        try:
            website_element = container_element.find_elements(By.CLASS_NAME, "ButtonWebsite")[0].get_attribute("href")
            return website_element
        except IndexError as e:
            website_element = None
            return website_element
        
    def get_address_element(self, number):
        address_element = self.driver.find_elements(By.CLASS_NAME, "MuiTypography-colorTextSecondary")[number]
        name, suburb, state = address_element.text.split(",")
        return (suburb + state).lstrip()

    def get_state_name(self, number):
        state = self.get_address_element(number).split(" ")[-2]
        return state

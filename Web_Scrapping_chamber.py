from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
# import undetected_chromedriver as uc

class WebScraping_chamber:
    def __init__(self):
        self.options = uc.ChromeOptions()
        self.options.headless = False
        self.driver = uc.Chrome(options=self.options)
        self.url = "https://australia.chamberofcommerce.com/search?what=Air+Conditioning&where=Rockhampton"
        self.driver.execute_cdp_cmd("Network.setBlockedURLs", {"urls": ["*doubleclick.net*", "*ads.google.com*"]})
        self.driver.get(self.url)

    def find_type_input(self, business_type):
        self.driver.implicitly_wait(5)
        type_input = self.driver.find_element(By.ID, "search3")
        type_input.clear()
        text_to_type = business_type
        for char in text_to_type:
            type_input.send_keys(char)
            time.sleep(0.2)
        

    def find_location_input(self, location):
        self.driver.implicitly_wait(5)
        type_input = self.driver.find_element(By.ID, "citystate3")
        type_input.clear()
        text_to_type = location
        for char in text_to_type:
            type_input.send_keys(char)
            time.sleep(0.2) 

        type_input.send_keys(Keys.RETURN)
        time.sleep(5) 

    def find_business_card(self):
        time.sleep(10) 
        self.driver.implicitly_wait(5)
        business_card = self.driver.find_elements(By.CLASS_NAME, "FeaturedPlacePreview")
        return business_card
    
    def get_company_name(self):
        company_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        return company_name.text

    def get_address(self):
        city = self.driver.find_element(By.XPATH, '//span[@selector-type="City"]')
        state = self.driver.find_element(By.XPATH, '//span[@selector-type="State"]')
        post_code = self.driver.find_element(By.XPATH, '//span[@selector-type="Zip"]')
        return city, state, post_code
    def get_phone_number(self):
        phone_number = self.driver.find_element(By.XPATH, '//a[@selector-type="Phone"]')
        return phone_number.text
    
    def get_website(self):
        container = self.driver.find_elements(By.CLASS_NAME, "card-body")[3]
        sentense = container.find_elements(By.CLASS_NAME, "text-dark")[5].text
        seperate_text = sentense.split(": ")
        website = seperate_text[1]
        return website
    
    def click_next_page(self):
        next_page_button = self.driver.find_elements(By.CLASS_NAME, "page-link")[-1]
        return next_page_button
    
    


if __name__ == "__main__":
    web_scraping_chamber = WebScraping_chamber()
    web_scraping_chamber.find_type_input("Air Conditioning")
    web_scraping_chamber.find_location_input("Brisbane")
    # print(web_scraping_chamber.find_business_card())
    time.sleep(15)
    web_scraping_chamber.click_next_page().click()
    time.sleep(5)

    while True:
        try:
            wait = WebDriverWait(web_scraping_chamber, 5)
            next_page_button = wait.until(EC.element_to_be_clickable(web_scraping_chamber.click_next_page()))
            next_page_button.click()
            time.sleep(5)
        except: 
            print("It is the end of the page")
    
        
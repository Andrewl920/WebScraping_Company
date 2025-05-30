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
        self.url = "https://australia.chamberofcommerce.com/search?what=Electrician&where=Sydney"
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

    def safe_click(self, element):
        try:
            # Scroll element into view
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            time.sleep(2)  # Wait for scroll to complete
            
            # Try regular click first
            try:
                element.click()
                return True
            except:
                # If regular click fails, use JavaScript click
                self.driver.execute_script("arguments[0].click();", element)
                return True
        except Exception as e:
            print(f"Error clicking element: {str(e)}")
            return False

    def find_business_card(self):
        time.sleep(10) 
        self.driver.implicitly_wait(5)
        business_cards = self.driver.find_elements(By.CLASS_NAME, "FeaturedPlacePreview")
        
        # Filter out any non-clickable cards
        clickable_cards = []
        for card in business_cards:
            try:
                if card.is_displayed() and card.is_enabled():
                    clickable_cards.append(card)
            except:
                continue
                
        return clickable_cards
    
    def get_company_name(self):
        company_name = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        return company_name.text

    def get_address(self):
        city = self.driver.find_element(By.XPATH, '//span[@selector-type="City"]').text
        state = self.driver.find_element(By.XPATH, '//span[@selector-type="State"]').text
        post_code = self.driver.find_element(By.XPATH, '//span[@selector-type="Zip"]').text
        return city, state, post_code
    
    def get_phone_number(self):
        try: 
            phone_number = self.driver.find_element(By.XPATH, '//a[@selector-type="Phone"]')
            return phone_number.text
        except:
            return None
    
    def get_website(self):
        try: 
            container = self.driver.find_elements(By.CLASS_NAME, "card-body")[3]
            sentense = container.find_elements(By.CLASS_NAME, "text-dark")[5].text
            seperate_text = sentense.split(": ")
            website = seperate_text[1]

            if website.startswith("http"):
                return website
            else:
                return None
            
        except:
            return None
    
    def click_next_page(self):
        next_page_button = self.driver.find_elements(By.CLASS_NAME, "page-link")[-1]
        return next_page_button
    
    def check_last_page(self):
        container = self.driver.find_element(By.CLASS_NAME, "pagination")
        try:
            last_page_button = container.find_element(By.XPATH, '//span[@class="next page-link"]')
            
            if last_page_button is not None:
                return False
            
            return True
        except:
            return True
    
    


if __name__ == "__main__":
    web_scraping_chamber = WebScraping_chamber()

    time.sleep(10)
    while True:
        next_button = web_scraping_chamber.check_last_page()
        if next_button is False:
            print("this is the end of the search")
            break
        else:
            print("there is another page")
            web_scraping_chamber.click_next_page().click()

        time.sleep(10)

    
        
import Web_Scrapping_chamber as Webscraping
from Excel import Excel
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

major_city = ["Sydney", "Newcastle", "Wollongong", "Melbourne", "Geelong", "Ballarat", "Bendigo", "Brisbane", "Gold Coast", "Sunshine Coast", "Townsville", "Cairns", "Toowoomba", "Mackay", "Rockhampton", "Perth", "Bunbury", "Geraldton", "Adelaide", "Mount Gambier", "Hobart", "Launceston", "Devonport", "Burnie", "Canberra", "Darwin", "Alice Springs"]
search_type = ["Air Conditioning", "Electrican"]

if __name__ == "__main__":
    
    for city in major_city:
        for type in search_type:
            company_info = []
            company_list = {}

            scraping = Webscraping.WebScraping_chamber()
            scraping.find_type_input(type)
            scraping.find_location_input(city)
            total_business_card = scraping.find_business_card()
            print(len(total_business_card))

            for card in range(len(total_business_card)):
                scraping.driver.switch_to.window(scraping.driver.window_handles[0])
                total_business_card = scraping.find_business_card()
                total_business_card[card].click()

                time.sleep(10)
                scraping.driver.switch_to.window(scraping.driver.window_handles[-1])
                name = scraping.get_company_name()
                # time.sleep(1000)
                address = scraping.get_address()
                phone_number = scraping.get_phone_number()
                website = scraping.get_website()

                print(name, address, phone_number, website)
                scraping.driver.switch_to.window(scraping.driver.window_handles[-1])
                scraping.driver.close()
            
            scraping.click_next_page().click()
            time.sleep(5)




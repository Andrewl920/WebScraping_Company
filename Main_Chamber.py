import Web_Scrapping_chamber as Webscraping
import Excel as excel
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

major_city = ["Sydney", "Newcastle", "Wollongong", "Melbourne", "Geelong", "Ballarat", "Bendigo", "Brisbane", "Gold Coast", "Sunshine Coast", "Townsville", "Cairns", "Toowoomba", "Mackay", "Rockhampton", "Perth", "Bunbury", "Geraldton", "Adelaide", "Mount Gambier", "Hobart", "Launceston", "Devonport", "Burnie", "Canberra", "Darwin", "Alice Springs"]
search_type = ["Air Conditioning", "Electrican"]

if __name__ == "__main__":
    
    for city in major_city:
        Company_list = []

        for type in search_type:
            scraping = Webscraping.WebScraping_chamber()
            scraping.find_type_input(type)
            scraping.find_location_input(city)
            total_business_card = scraping.find_business_card()
            print(len(total_business_card))

            for card in range(len(total_business_card)):
                Company_info = {}
                scraping.driver.switch_to.window(scraping.driver.window_handles[0])
                total_business_card = scraping.find_business_card()
                total_business_card[card].click()

                time.sleep(10)
                scraping.driver.switch_to.window(scraping.driver.window_handles[-1])
                name = scraping.get_company_name()
                # time.sleep(1000)
                city, state, post_code = scraping.get_address()
                state = state
                address = city + " " + state + " " + post_code
                phone_number = scraping.get_phone_number()
                website = scraping.get_website()

                print(name, address, phone_number, website)
                Company_info["Name"] = name
                Company_info["Phone"] = phone_number
                Company_info["Address"] = address
                Company_info["Website"] = website
                Company_list.append(Company_info)

                scraping.driver.switch_to.window(scraping.driver.window_handles[-1])
                scraping.driver.close()
            
            # Company_info = {}
            # Company_info["Name"] = "name"
            # Company_info["Phone"] = "phone_number"
            # Company_info["Address"] = "address"
            # Company_info["Website"] = "website"
            # Company_list.append(Company_info)
            # state = "QLD"
            
            #put the company info in the excel
            for each_company in Company_list:
                excel = excel.Excel()
                last_row = excel.find_last_row(state)

                if excel.check_duplicate(state, each_company) == True:
                    continue
                else:
                    excel.fill_in_value(state, last_row, each_company)

            print("Just finsihed the web scraping of this page")

            try:
                wait = WebDriverWait(scraping.driver, 5)
                next_page_button = wait.until(EC.element_to_be_clickable(scraping.click_next_page()))
                next_page_button.click()
                time.sleep(5)
            except:
                continue
                





import Web_Scrapping_chamber as Webscraping
import Excel as excel
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

major_city = ["Sydney", "Newcastle", "Wollongong", "Melbourne", "Geelong", "Ballarat", "Bendigo", "Brisbane", "Gold Coast", "Sunshine Coast", "Townsville", "Cairns", "Toowoomba", "Mackay", "Rockhampton", "Perth", "Bunbury", "Geraldton", "Adelaide", "Mount Gambier", "Hobart", "Launceston", "Devonport", "Burnie", "Canberra", "Darwin", "Alice Springs"]
search_type = ["Air Conditioning", "Electrician"]

if __name__ == "__main__":
    
    for city in major_city:
        Company_list = []

        for type in search_type:
            if type == "Air Conditioning":
                continue
            page = 1
            scraping = Webscraping.WebScraping_chamber()
            scraping.find_type_input(type)
            scraping.find_location_input(city)

            while True:
                total_business_card = scraping.find_business_card()
                for card in range(len(total_business_card)):
                    Company_info = {}
                    time.sleep(5)
                    scraping.driver.switch_to.window(scraping.driver.window_handles[0])
                    
                    try:
                        # Use the safe click method
                        if not scraping.safe_click(total_business_card[card]):
                            print(f"Could not click card {card}, skipping...")
                            continue
                            
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
                    except Exception as e:
                        print(f"Error processing card {card}: {str(e)}")
                        continue

                excel_handler = excel.Excel()
                #put the company info in the excel
                for each_company in Company_list:
                    try:
                        last_row = excel_handler.find_last_row(state)

                        if excel_handler.check_duplicate(state, each_company) == True:
                            continue
                        else:
                            excel_handler.fill_in_value(state, last_row, each_company)
                            print(f"Saved company {each_company['Name']} to {state} sheet")
                    except Exception as e:
                        print(f"Error saving to Excel: {str(e)}")
                        continue

                print("Just finished the web scraping of this page")
                
                scraping.driver.switch_to.window(scraping.driver.window_handles[0])
                next_button = scraping.check_last_page()
                if next_button is False:
                    print("this is the end of the search")
                    break
                else:
                    wait = WebDriverWait(scraping.driver, 5)
                    next_page_button = wait.until(EC.element_to_be_clickable(scraping.click_next_page()))
                    next_page_button.click()
                    print("there is another page")
                    time.sleep(5)

                
                print(page)
                page += 1
                





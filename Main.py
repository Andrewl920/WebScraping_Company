import requests
from bs4 import BeautifulSoup
import Web_Scraping as Ws
import Excel as excel


def main():
    page_number = 1
    url = "https://www.yellowpages.com.au/search/listings?clue=Air+conditioning&locationClue=SA"

    while True:
        Company_list = []
        
        Ws.open_new_page(page_number)
        #get the total number of boxes
        boxes_number = Ws.total_box_number()
        if boxes_number == 0:
            break
            return "This is the end of the search result"
                
        else:
                    print(boxes_number)
                    for company in range(boxes_number):
                            Company_info = {}
                            if company == 0 or company == 36 or company == 37:
                                continue
                            else:
                                try:
                                    name = Ws.get_name_element(company)
                                    # print(name)
                                    phone = Ws.get_phone_element(company)
                                    website = Ws.get_website_element(company)
                                    address = Ws.get_address(company)
                                    Company_info["Name"] = name
                                    Company_info["Phone"] = phone
                                    Company_info["Address"] = address
                                    Company_info["Website"] = website

                                    Company_list.append(Company_info)
                                except:
                                     url = url + "&pageNumber=" + str(page_number)

        # print(Company_list)
                
        
            # fill in the excel sheet
        for each_company in Company_list:
                
                state_name = excel.state_name(each_company)
                # print(state_name)
                last_row = excel.find_last_row(state_name)

                #check duplicate
                if excel.check_duplicate(state_name, each_company) == True:
                    continue
                else:
                    excel.fill_in_value(state_name, last_row, each_company)
        print("Just finsihed the web scraping of page" + str(page_number))
        page_number += 1
        
        

if __name__ == "__main__":
    main()
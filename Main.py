import requests
from bs4 import BeautifulSoup
import Web_Scraping as Ws
import Excel as excel

def main():
    Company_list = []
    page_number = 1
    Ws.open_new_page(page_number)
    #get the total number of boxes
    boxes_number = Ws.total_box_number()
    if boxes_number == 0:
        return "This is the end of the search result"
    else:
            for company in range(2):
                    Company_info = {}
                    if company == 0:
                        continue

                    else:

                        name = Ws.get_name_element(company)
                        phone = Ws.get_phone_element(company)
                        website = Ws.get_website_element(company)
                        address = Ws.get_address(company)
                        Company_info["Name"] = name
                        Company_info["Phone"] = phone
                        Company_info["Address"] = address
                        Company_info["Website"] = website

                        Company_list.append(Company_info)
        
    # page_number += 1
    # fill in the excel sheet
    for each_company in Company_list:
         
        state_name = excel.state_name(each_company)
        # print(state_name)
        last_row = excel.find_last_row(state_name)

        #check duplicate
        # print(excel.check_duplicate(state_name, each_company))
        if excel.check_duplicate(state_name, each_company) == True:
             continue
        else:
             excel.fill_in_value(state_name, last_row, each_company)


    # print(Company_list)

if __name__ == "__main__":
    main()
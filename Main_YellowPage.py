import requests
import Excel as excel
import Web_Scraping_Selenium as Ws_Selenium


if __name__ == "__main__":
    page_number = 1

    while True:
        Company_list = []
        
        # Ws.open_new_page(page_number)
        Ws_Selenium = Ws_Selenium.WebScraping(page_number)
        #get the total number of boxes
        total_box_number = Ws_Selenium.find_total_box()
        hidden_box_number = 0
        # boxes_number = Ws.total_box_number()
        if total_box_number == 0:
            break
                
        else:
            for company in range(total_box_number):
                    Company_info = {}

                    if company == 0 or company == 36:
                        continue
                    elif Ws_Selenium.find_hidden(Ws_Selenium.find_large_container(company)):
                        print(company, hidden_box_number)
                        Ws_Selenium.find_hidden_box()[hidden_box_number].click()
                        name = Ws_Selenium.get_name_element(company)
                        phone = Ws_Selenium.get_phone_element(company)
                        website = Ws_Selenium.get_website_element(company)
                        address = Ws_Selenium.get_address_element(company)
                        hidden_box_number += 1
                    else:
                        name = Ws_Selenium.get_name_element(company)
                        phone = Ws_Selenium.get_phone_element(company)
                        website = Ws_Selenium.get_website_element(company)
                        address = Ws_Selenium.get_address_element(company)

                    Company_info["Name"] = name
                    Company_info["Phone"] = phone
                    Company_info["Address"] = address
                    Company_info["Website"] = website
                    Company_list.append(Company_info)


            # try:
            #     for company in range(2):
            #         Company_info = {}
            #         if company == 0 or company == 36 or company == 37:
            #             continue
            #         else:                    
            #             name = Ws.get_name_element(company)
            #             # print(name)
            #             phone = Ws.get_phone_element(company)
            #             website = Ws.get_website_element(company)
            #             print(website)
            #             address = Ws.get_address(company)

            #             Company_info["Name"] = name
            #             Company_info["Phone"] = phone
            #             Company_info["Address"] = address
            #             Company_info["Website"] = website
            #             Company_list.append(Company_info)
                                                                   
            # except:
            #     Ws_Selenium.init(page_number)
            #     hidden_box_number = Ws_Selenium.find_total_box()
            #     for company in range(hidden_box_number):
            #         Ws_Selenium.find_box()[company].click()
            #         name = Ws_Selenium.get_name_element(company)
            #         phone = Ws_Selenium.get_phone_element(company)
            #         website = Ws_Selenium.get_website_element(company)
            #         address = Ws_Selenium.get_address_element(company)

                                
            #     Company_info["Name"] = name
            #     Company_info["Phone"] = phone
            #     Company_info["Address"] = address
            #     Company_info["Website"] = website
            #     Company_list.append(Company_info)
                
        
            # fill in the excel sheet
        for each_company in Company_list:
                # Ws_Selenium.find_box()[company].click()
                excel = excel.Excel()
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
        
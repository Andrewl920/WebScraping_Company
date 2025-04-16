import requests
from bs4 import BeautifulSoup
import Web_Scraping as Ws
import Excel as excel

def main():
    page_number, boxes_number = Ws.total_page_number()

    for company in range(boxes_number):
        if company == 0:
            continue

        else:
            Company_info = {}
            name = Ws.get_name_element(company)
            phone = Ws.get_phone_element(company)
            website = Ws.get_website_element(company)
            address = Ws.get_address
            Ws.add_company_list(name, phone, website, address)
            print(Ws.Company_list)


if __name__ == "__main__":
    main ()
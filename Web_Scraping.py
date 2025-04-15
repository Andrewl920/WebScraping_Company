from selenium import webdriver
from bs4 import BeautifulSoup

Company_list = []
Company_info = {}

driver = webdriver.Chrome()
driver.get("https://www.yellowpages.com.au/search/listings?clue=air+conditioning&locationClue=All+States")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

numbers = len(soup.find_all("h3"))

for company in range(numbers):
    Company_info = {}

    name_element = soup.find_all("h3")[company]
    phone_element = soup.find_all("a", "MuiButtonBase-root MuiButton-root MuiButton-text ButtonPhone wobble-call MuiButton-textSecondary MuiButton-fullWidth")[company]
    address_element = soup.find_all("p", "MuiTypography-root")[company]
    website_element = soup.find_all("a", "MuiButtonBase-root MuiButton-root MuiButton-text ButtonWebsite jss366 MuiButton-textPrimary MuiButton-fullWidth")[company]

    Company_info["name"] = name_element.get_text(strip=True)
    Company_info["phone"] = phone_element.get_text(strip=True)
    Company_info["address"] = address_element.get_text(strip=True)
    Company_info["website"] = website_element["href"]
    Company_list.append(Company_info)



for i in Company_list:
    print(i)




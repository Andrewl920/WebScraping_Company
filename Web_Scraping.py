from selenium import webdriver
from bs4 import BeautifulSoup

Company_list = []
Company_info = {}

driver = webdriver.Chrome()
driver.get("https://www.yellowpages.com.au/search/listings?clue=air+conditioning&locationClue=All+States")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

numbers = len(soup.find_all("h3")) - 1

for company in range(numbers):
    Company_info = {}

    name_element = soup.find_all("h3")[company]
    phone_element = soup.find_all("a", "MuiButtonBase-root MuiButton-root MuiButton-text ButtonPhone wobble-call MuiButton-textSecondary MuiButton-fullWidth")[company]
    address_element = soup.find_all("p", "MuiTypography-root")[company]
    website_element = soup.find_all("a", "MuiButtonBase-root MuiButton-root MuiButton-text ButtonWebsite jss366 MuiButton-textPrimary MuiButton-fullWidth")[company]

    # get the address
    box_element = list(soup.find_all("div", "Box__Div-sc-dws99b-0 iOfhmk MuiPaper-root MuiCard-root PaidListing MuiPaper-elevation1 MuiPaper-rounded"))[company]
    seperate_element = box_element.get_text(strip=True).split(",")
    first = seperate_element[1].lstrip()
    second = seperate_element[2].split("(")[0].split()[0] # get the state name
    # check if the post code in other location
    if any(char.isdigit() for char in seperate_element[2]):
        second_half = seperate_element[2].split("(")[0].split()[1][:4]
    else:
        second_half = seperate_element[3].split("(")[1].split()[1][:4]


    # get the post code
    address = first + " " + second + " " + second_half

    Company_info["name"] = name_element.get_text(strip=True)
    Company_info["phone"] = phone_element.get_text(strip=True)
    Company_info["address"] = address
    Company_info["website"] = website_element["href"]
    Company_list.append(Company_info)

    


for i in Company_list:
    print(i)




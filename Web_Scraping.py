from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

Company_list = []
Company_info = {}

# chromedriver_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
service = Service(r"C:\Users\stars\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = service, options = options)
driver.get("https://www.yellowpages.com.au/search/listings?clue=air+conditioning&locationClue=All+States")

soup = BeautifulSoup(driver.page_source, 'html.parser')

numbers = len(soup.find_all("h3"))

for company in range(numbers):
    if company == 0:
        continue

    else:

        Company_info = {}

        name_element = soup.find_all("h3")[company]
        phone_element = soup.find_all("a", "MuiButtonBase-root MuiButton-root MuiButton-text ButtonPhone wobble-call MuiButton-textSecondary MuiButton-fullWidth")[company]
        website_element = soup.find_all("a", "MuiButtonBase-root MuiButton-root MuiButton-text ButtonWebsite jss366 MuiButton-textPrimary MuiButton-fullWidth")[company]

        # get the address
        box_element = list(soup.find_all("div", "Box__Div-sc-dws99b-0 bKFqNV"))[company+4]

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

        Company_info["Name"] = name_element.get_text(strip=True)
        Company_info["Phone"] = phone_element.get_text(strip=True)
        Company_info["Address"] = address
        Company_info["Website"] = website_element["href"]
        Company_list.append(Company_info)

# get the total page number
def total_page_number():
    element = driver.find_element(By.XPATH, "//p[contains(text(),'Showing results')]")
    total_page_number = element.text.split(" ")[4]
    return total_page_number



for i in Company_list:
    print(i)




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

Company_list = []
Company_info = {}

global driver
global soup

#create a new page
def open_new_page(page_number=1):
    global driver
    global soup

    url = "https://www.yellowpages.com.au/search/listings?clue=Electrican&locationClue=NSW"

    service = Service(r"C:\Users\Administrator\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    options = Options()
    # options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service = service, options = options)
    

    if page_number == 1:
        driver.get(url)
    else:
        new_url = url + "&pageNumber=" + str(page_number)
        driver.get(new_url)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

# get the total boxes number --> should be used before web scraping
def total_box_number():
    #get the total boxes number
    boxes_number = len(soup.find_all("h3"))
    return boxes_number

def get_name_element(number):
    name_element = soup.find_all("h3")[number]
    name = name_element.get_text(strip=True)
    return name

def get_phone_element(number):
    #check if the company have phone number
    # print(number)
    details = soup.find_all("div", "Box__Div-sc-dws99b-0 enijwQ MuiCardContent-root")[number]
    phone_box = details.find_all("a", "MuiButtonBase-root MuiButton-root MuiButton-text ButtonPhone wobble-call MuiButton-textSecondary MuiButton-fullWidth")
    if phone_box == []:
        phone_element = None
    else:
        phone_element = details.find_all("a", class_="MuiButtonBase-root MuiButton-root MuiButton-text ButtonPhone wobble-call MuiButton-textSecondary MuiButton-fullWidth")[0].get_text(strip=True)
            
    return phone_element


def get_website_element(number):
    #check if the company have website
    details = soup.find_all("div", "Box__Div-sc-dws99b-0 enijwQ MuiCardContent-root")[number]
    website_box = details.find_all("a", "MuiButtonBase-root MuiButton-root MuiButton-text ButtonWebsite jss366 MuiButton-textPrimary MuiButton-fullWidth")
    if website_box == []:
        website_element = None
    else:
        website_element = details.find_all("a", class_="MuiButtonBase-root MuiButton-root MuiButton-text ButtonWebsite jss366 MuiButton-textPrimary MuiButton-fullWidth")[0]["href"]
    
    return website_element
    

def get_address(number):
    box_element = list(soup.find_all("div", "Box__Div-sc-dws99b-0 bKFqNV"))[number+4]

    seperate_element = box_element.get_text(strip=True).split(",")
    first = seperate_element[1].lstrip()
    second = seperate_element[2].split("(")[0].split()[0] # get the state name
    # check if the post code in other location
    if any(char.isdigit() for char in seperate_element[2]):
        second_half = seperate_element[2].split("(")[0].split()[1][:4]
    else:
        second_half = seperate_element[3].split("(")[1].split()[1][:4]
    
    address = first + " " + second + " " + second_half
    return address








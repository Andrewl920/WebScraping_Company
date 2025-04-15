from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.yellowpages.com.au/search/listings?clue=air+conditioning&locationClue=All+States")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#get the name of the company
for title in soup.find_all("h3"):
    print(title.get_text(strip=True))

#get the number of the compnay
for numbers in soup.find_all("a", "MuiButtonBase-root MuiButton-root MuiButton-text ButtonPhone wobble-call MuiButton-textSecondary MuiButton-fullWidth"):
    print(numbers.get_text(strip= True))

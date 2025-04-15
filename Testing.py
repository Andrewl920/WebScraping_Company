from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://www.yellowpages.com.au/search/listings?clue=air+conditioning&locationClue=All+States")
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

for title in soup.find_all("h3"):
    print(title.get_text(strip=True))

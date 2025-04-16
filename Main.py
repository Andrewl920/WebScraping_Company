import requests
from bs4 import BeautifulSoup
import Web_Scraping as Ws
import Excel as excel

url = "https://www.starsparky.com.au/"
req = requests.session().get(url)
soup = BeautifulSoup(req.text, features="html.parser")
result = soup

print(result)
import requests
from bs4 import BeautifulSoup

url = "https://www.starsparky.com.au/"
req = requests.session().get(url)
soup = BeautifulSoup(req.text, features="html.parser")
result = soup

print(result)
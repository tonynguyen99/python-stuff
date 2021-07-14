import requests
from bs4 import BeautifulSoup

base_url = 'https://www.coles.com.au/catalogues-and-specials/view-all#view=list&saleId=40032&areaName=c-vic-met'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

r = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky')
soup = BeautifulSoup(r.content, 'lxml')

productList = soup.find_all('li', attrs={'class':'product-grid__item'})

print(productList)
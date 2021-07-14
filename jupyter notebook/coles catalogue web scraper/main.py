import requests
from bs4 import BeautifulSoup

base_url = 'https://salefinder.com.au/coles-catalogue/coles-catalogue-vic-metro/40032/list?qs=1,,0,0,0'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

r = requests.get(base_url)
soup = BeautifulSoup(r.content, 'lxml')

product_links = []

for a in soup.find_all('a', {'class': 'item-name'}):
    # print(a['href'])
    product_links.append(base_url + '/' + a['href'])

print(product_links)

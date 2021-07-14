import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://salefinder.com.au/coles-catalogue/coles-catalogue-vic-metro'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

product_links = []

# 

testlink = 'https://salefinder.com.au/40032/food-and-beverage/groceries/biscuits-and-snacks/carmans-nut-bars-160g175g/400321001/'


# # # # # # # # # 
# # Final Code # #
# # # # # # # # # 

# for x in range(1, 10):
#     r = requests.get(f'https://salefinder.com.au/coles-catalogue/coles-catalogue-vic-metro/40032/list?qs={x},,0,0,0')
#     soup = BeautifulSoup(r.content, 'lxml')

#     for a in soup.find_all('a', {'class': 'item-name'}):
#         # print(a['href'])
#         product_links.append(base_url + '/' + a['href'])

# product_list = []

# for link in product_links:
#     r = requests.get(link, headers = headers)
#     soup = BeautifulSoup(r.content, 'lxml')

#     product_name = soup.find('h1').text.strip()
#     product_price = soup.find('span', {'class': 'price'}).text.strip()
#     product_discount = soup.find('div', {'class': 'price-options'}).text.strip()

#     product = {
#         'product name': product_name,
#         'product price': product_price,
#         'product discount': product_discount
#     }

#     product_list.append(product)

# df = pd.DataFrame(product_list)
# print(df.head(15))





# # # # # # # # # 
# # Test Code # #
# # # # # # # # # 
r = requests.get(testlink, headers = headers)
soup = BeautifulSoup(r.content, 'lxml')

product_name = soup.find('h1').text.strip()
product_price = soup.find('span', {'class': 'price'}).text.strip()
product_discount = soup.find('div', {'class': 'price-options'}).text.strip()

product = {
    'product name': product_name,
    'product price': product_price,
    'product discount': product_discount
}

print(product)
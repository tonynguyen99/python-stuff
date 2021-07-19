import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

base_url = 'https://salefinder.com.au/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}

# testlink = 'https://salefinder.com.au/40032/food-and-beverage/groceries/biscuits-and-snacks/carmans-nut-bars-160g175g/400321001/'
# # # # # # # # # 
# # Test Code # #
# # # # # # # # # 
# r = requests.get(testlink, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# product_name = soup.find('h1').text.strip()
# product_price = soup.find('span', {'class': 'price'}).text.strip()
# product_discount = soup.find('div', {'class': 'price-options'}).text.strip()

# product = {
#     'product name': product_name,
#     'product price': product_price,
#     'product discount': product_discount
# }

# print(product)

# # # # # # # # # 
# # Final Code # #
# # # # # # # # # 
product_links = []
product_list = []

#n = number of pages in catalogue (inclusive)
def generate_product_links(catalogue_number, n):
    for x in range(1, n):
        r = requests.get(f'https://salefinder.com.au/coles-catalogue/coles-catalogue-vic-metro/{catalogue_number}/list?qs={x},,0,0,0')
        soup = BeautifulSoup(r.content, 'lxml')

        for a in soup.find_all('a', {'class': 'item-name'}):
            product_links.append(base_url + a['href'])
    return product_links

#Empty list for products to be appended
def get_product_details(product_links):
    for link in product_links:
        r = requests.get(link, headers=headers)
        soup = BeautifulSoup(r.content, 'lxml')

        product_name = soup.find('h1').text.strip()
        product_price = soup.find('span', {'class': 'price'}).text.strip()
        product_discount = soup.find('div', {'class': 'price-options'}).text.strip()

        product = {
            'product_name': product_name,
            'product_price': product_price,
            'product_discount': product_discount
        }

        product_list.append(product)
    return product_list

def convert_product_list_to_csv(product_list):
    keys = product_list[0].keys()
    with open('./python-stuff/coles catalogue web scraper/products.csv', 'w', newline='')  as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(product_list)

def get_valid_dates(catalogue_number):
    r = requests.get(f'https://salefinder.com.au/coles-catalogue/coles-catalogue-vic-metro/{catalogue_number}/list?qs=1,,0,0,0')
    soup = BeautifulSoup(r.content, 'lxml')

    valid_dates = soup.find('span', {'class': 'sale-dates'}).text
    return valid_dates



if __name__ == '__main__':
    generate_product_links('40141', 10)
    get_product_details(product_links)
    convert_product_list_to_csv(product_list)
    print(get_valid_dates('40141'))
import random
import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

page = 1

file = open('amazon_products.csv', 'w', newline='', encoding='utf-8')
f_obj = csv.writer(file)
f_obj.writerow(['Title', 'Price', 'Rating'])

while page <= 5:
    url = 'https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A172456&page=' + str(page)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    products = soup.find_all('div', {'data-component-type': 's-search-result'})

    for product in products:
        title = product.find('span', {'class': 'a-size-medium'}).text.strip()
        price = product.find('span', {'class': 'a-offscreen'}).text.strip()
        rating = product.find('span', {'class': 'a-icon-alt'}).text.strip()

        f_obj.writerow([title, price, rating])

    page += 1
    delay = random.randint(15, 20)
    sleep(delay)

file.close()
print("Data saved to amazon_products.csv")













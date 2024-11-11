from bs4 import BeautifulSoup
import requests

response = requests.get("https://books.toscrape.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("article", {"class": "product_pod"})

    # Проходим по всем книгам и выводим их цены
    for book in soup_list:
        price = book.find("p", {"class": "price_color"})
        print(price.text)


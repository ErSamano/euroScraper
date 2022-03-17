from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import date


def get_data(product_type, product_url):
    response = requests.get(product_url).content
    soup = BeautifulSoup(response, 'html.parser')

    products_type = []
    products_name = []
    products_link = []
    products_price = []
    products_old_price = []
    products_date = []

    # Get the product name and the link
    for contentProduct in soup.findAll(attrs={'class': 'product name product-item-name'}):
        products_name.append(contentProduct.find('a').text)
        products_type.append(product_type)
        products_date.append(date.today())
        for links in contentProduct.find_all('a'):
            products_link.append(links.get('href'))

    # Get the products price
    for contentPrice in soup.findAll(attrs={'class': 'price-box price-final_price'}):

        if contentPrice.find(class_='old-price'):
            products_old_price.append(contentPrice.find(class_='old-price').text)
            products_price.append(contentPrice.find(class_='special-price').text)

        else:
            products_old_price.append("SIN OFERTA")
            products_price.append(contentPrice.find(class_='price').text)

    products_table = pd.DataFrame({'Tipo': products_type, 'Nombre': products_name, 'Link': products_link,
                                   'Oferta/Prec_Original': products_old_price, 'Precio': products_price,
                                   'Fecha': products_date})

    return products_table
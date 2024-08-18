from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import date

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def get_data(product_type, product_url):
    '''
            When the content page is dynamic, we need to anable a way to load
            the hiden html site content. In order to achieve that we are going
            to use Selenium Lib
            to load dynamic elements.
    '''

    # s = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=s)
    driver = webdriver.Firefox()  # Use Firefox, Chrome, etc. depending on your preference
    driver.set_window_size(2304, 1440)
    driver.get(product_url)

    # Setting up a waiting time before scroll down
    SCROLL_PAUSE_TIME = 6.0  # Increase the pause time if necessary
    EXTRA_WAIT_TIME = 5.0  # Additional waiting time after scrolling

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page using WebDriverWait
        WebDriverWait(driver, SCROLL_PAUSE_TIME).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))

        # Additional wait
        time.sleep(EXTRA_WAIT_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")

        # Break the loop when either new_height == last_height (page end) or the specific HTML block is found
        if new_height == last_height:
            break
        last_height = new_height

    response = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()

    ## start the scraper

    soup = BeautifulSoup(response, 'html.parser')

    products_type = []
    products_name = []
    products_link = []
    products_price = []
    products_old_price = []
    products_date = []

    # Target the specific div by its class
    target_div = soup.find('div', class_='products wrapper grid products-grid')

    # If the div is found, proceed with the parsing
    if target_div:

        # Get the product name and the link
        for contentProduct in target_div.findAll(attrs={'class': 'product name product-item-name'}):
            products_name.append(contentProduct.find('a').text)
            products_type.append(product_type)
            products_date.append(date.today())
            for links in contentProduct.find_all('a'):
                products_link.append(links.get('href'))

        # Get the products price
        for contentPrice in target_div.findAll(attrs={'class': 'price-box price-final_price'}):

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

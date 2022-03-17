from get_european_soup import get_data

products = {
    'Tequila': 'https://www.laeuropea.com.mx/licores-y-destilados/tequilas.html?product_list_limit=144',
    'Ron': 'https://www.laeuropea.com.mx/licores-y-destilados/ron.html?product_list_limit=144',
    'Whisky': 'https://www.laeuropea.com.mx/licores-y-destilados/whisky.html?product_list_limit=144',
    'Vodka': 'https://www.laeuropea.com.mx/licores-y-destilados/vodka.html?product_list_limit=144',
    'Ginebra': 'https://www.laeuropea.com.mx/licores-y-destilados/ginebra.html?product_list_limit=144',
    'Mezcal': 'https://www.laeuropea.com.mx/licores-y-destilados/mezcales.html?product_list_limit=144',
    'Cremas/Licores': 'https://www.laeuropea.com.mx/licores-y-destilados/cremas-y-licores.html?product_list_limit=144',
    'Cognag': 'https://www.laeuropea.com.mx/licores-y-destilados/cognac.html?product_list_limit=144',
    'Brandy': 'https://www.laeuropea.com.mx/licores-y-destilados/brandy.html?product_list_limit=144',
    'Sake': 'https://www.laeuropea.com.mx/licores-y-destilados/sake.html?product_list_limit=144',
    'Otro': 'https://www.laeuropea.com.mx/licores-y-destilados/otros.html?product_list_limit=144',
    'Vinos': 'https://www.laeuropea.com.mx/vinos/tipos/todos.html?product_list_limit=144',
    'Vinos': 'https://www.laeuropea.com.mx/vinos/tipos/todos.html?p=2&product_list_limit=144',
    'Vinos': 'https://www.laeuropea.com.mx/vinos/tipos/todos.html?p=3&product_list_limit=144',
    'Vinos': 'https://www.laeuropea.com.mx/vinos/tipos/todos.html?p=4&product_list_limit=144'
}

count = 0
for type, url in products.items():
    if count == 0:
        get_data(type, url).to_csv('europea_precios.csv', index=False)
    else:
        get_data(type, url).to_csv('europea_precios.csv', mode='a', index=False, header=False)
    count += 1
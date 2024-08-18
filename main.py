from get_european_soup import get_data

products = {
    'Vinos': 'https://www.laeuropea.com.mx/vinos/tipos/todos.html',
    'Tequila':'https://www.laeuropea.com.mx/licores-y-destilados/tequilas.html',
    'Ron': 'https://www.laeuropea.com.mx/licores-y-destilados/ron.html',
    'Whisky': 'https://www.laeuropea.com.mx/licores-y-destilados/whisky.html',
    'Vodka': 'https://www.laeuropea.com.mx/licores-y-destilados/vodka.html',
    'Ginebra': 'https://www.laeuropea.com.mx/licores-y-destilados/ginebra.html',
    'Mezcal': 'https://www.laeuropea.com.mx/licores-y-destilados/mezcales.html',
    'Cremas/Licores': 'https://www.laeuropea.com.mx/licores-y-destilados/cremas-y-licores.html',
    'Cognag': 'https://www.laeuropea.com.mx/licores-y-destilados/cognac.html',
    'Brandy': 'https://www.laeuropea.com.mx/licores-y-destilados/brandy.html',
    'Sake': 'https://www.laeuropea.com.mx/licores-y-destilados/sake.html',
    'Otro': 'https://www.laeuropea.com.mx/licores-y-destilados/otros.html',
}

count = 0
for ptype, url in products.items():
    if count == 0:
        get_data(ptype, url).to_csv('europea_precios.csv', index=False)
    else:
        get_data(ptype, url).to_csv('europea_precios.csv', mode='a', index=False, header=False)
    count += 1
import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print('Status del sitio',r.status_code)
    print(r.text)
    print('tipo', type(r.text))
    # Como tiene tipo string lo transformamos con request a diccionario
    categories = r.json()
    for category in categories:
        print(category['name'])
    print('tipo nuevo', type(categories))

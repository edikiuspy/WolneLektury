import requests

def get_books():
    url = "http://wolnelektury.pl/api/books/"
    response = requests.get(url)

    return response.json()
print(get_books())
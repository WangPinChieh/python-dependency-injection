from requests import get
from abstractService import IApiFetcher

class ApiFetcher(IApiFetcher):
    def print(self):
        x = get('https://w3schools.com/python/demopage.htm')
        print(x.text)


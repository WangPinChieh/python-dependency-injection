from requests import get
from abstractService import IApiFetcher

class ApiFetcher(IApiFetcher):
    def print(self):
        x = get('https://www.google.com')
        print(x.text)

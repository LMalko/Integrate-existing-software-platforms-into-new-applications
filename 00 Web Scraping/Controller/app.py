import requests
from bs4 import BeautifulSoup
import csv

def start_app():
    response = requests.get("https://www.imdb.com/name/nm0000142/")
    print(response)

if __name__ == "__main__":
    pass

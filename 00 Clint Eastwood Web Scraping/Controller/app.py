import requests
from bs4 import BeautifulSoup
import csv

def check_response():
    response = requests.get ( "https://www.imdb.com/name/nm0000142/" )
    return response

def start_app():
    response = check_response()

    print(response.text)



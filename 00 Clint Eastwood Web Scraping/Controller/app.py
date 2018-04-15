import requests
from bs4 import BeautifulSoup
import csv

def check_url_response():
    response = requests.get ( "https://www.imdb.com/name/nm0000142/" )
    return response

def get_films(soup):
    return soup.findAll('div', id=lambda x: x and x.startswith('actor-'))

def start_app():
    response = check_url_response()
    soup = BeautifulSoup(response.text, "html.parser")
    films = get_films(soup)
    for film in films:
            print(film.find("a").get_text())




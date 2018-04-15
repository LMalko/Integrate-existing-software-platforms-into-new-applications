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
        title = film.find("a").text
        character = film.find("b").next_sibling.next_sibling.next_sibling
        release_form = film.find( "b" ).next_sibling
        release_year = film.find("span").text





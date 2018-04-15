import requests
from bs4 import BeautifulSoup
import csv

def check_url_response():
    response = requests.get ( "https://www.imdb.com/name/nm0000142/" )
    return response

def get_movies(soup):
    return soup.findAll('div', id=lambda x: x and x.startswith('actor-'))

def set_movies_attributes(movies):
    for movie in movies:
        title = movie.find("a").text
        character = movie.find("b").next_sibling.next_sibling.next_sibling.split("\n")[1]
        release_form = movie.find( "b" ).next_sibling

        if release_form == "\n":
            release_form = "Movie"
        else:
            release_form = release_form.split("\n")[1]

        release_year = movie.find("span").text.split("\n")[1]
        print(f"{title}***{character}***{release_form}***{release_year}")


def start_app():
    response = check_url_response()
    soup = BeautifulSoup(response.text, "html.parser")
    movies = get_movies(soup)
    set_movies_attributes(movies)





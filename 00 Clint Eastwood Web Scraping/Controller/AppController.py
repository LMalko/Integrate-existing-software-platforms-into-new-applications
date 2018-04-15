import requests
from bs4 import BeautifulSoup
from Model.Movie import *
from csv import writer

class AppController:

    movie_collection = []

    def __init__(self, link):
        response = self.check_url_response(link)
        soup = BeautifulSoup(response.text, "html.parser")
        self.set_movies_collection(soup)


    def set_movies_collection(self, soup):
        movies = self.get_movies(soup)
        for movie in movies:
            temp_movie = self.set_movie_object(movie)
            self.movie_collection.append(temp_movie)

    @staticmethod
    def check_url_response(link):
        response = requests.get(link)
        return response

    @staticmethod
    def get_movies(soup):
        return soup.findAll('div', id=lambda x: x and x.startswith('actor-'))

    @staticmethod
    def set_movie_object(movie):
        title = movie.find("a").text
        character = movie.find("b").next_sibling.next_sibling.next_sibling.split("\n")[1]
        category = movie.find( "b" ).next_sibling

        if category == "\n":
            category = "Movie"
        else:
            category = category.split("(")[1].split(")")[0]

        release_year = movie.find("span").text.split("\n")[1]
        return Movie(title, character, category, release_year)


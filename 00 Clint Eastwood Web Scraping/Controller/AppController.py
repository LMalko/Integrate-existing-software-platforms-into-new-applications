import requests
from bs4 import BeautifulSoup
from Model.Movie import *
from csv import writer

class AppController:

    movie_collection = []

    def __init__(self, link):
        self.response = self.set_url_response(link)
        self.soup = BeautifulSoup(self.response.text, "html.parser")


    @staticmethod
    def set_url_response(link):
        response = requests.get(link)
        return response

    def get_response(self):
        return self.response

    def run_app(self):
        self._set_movies_collection(self.soup)
        self.actors_name = self._set_actors_name(self.soup)
        self._write_collection_to_csv_file(self.movie_collection)

    def _set_movies_collection(self, soup):
        movies = self._get_movies(soup)
        for movie in movies:
            temp_movie = self._set_movie_object(movie)
            self.movie_collection.append(temp_movie)

    @staticmethod
    def _get_movies(soup):
        return soup.findAll('div', id=lambda x: x and x.startswith('actor-'))

    def _write_collection_to_csv_file(self, collection):
        with open(f"{self.get_actors_name()} Movies.csv", "w", encoding="utf-8", newline='') as file:
            csv_writer = writer(file)
            csv_writer.writerow(["Title", "Character", "Year", "Category"])
            for item in collection:
                csv_writer.writerow([item.title, item.character_played, item.release_year, item.category])

    @staticmethod
    def _set_movie_object(movie):
        title = movie.find("a").text
        try:
            character = movie.find("b").next_sibling.next_sibling.next_sibling.split("\n")[1]
        except AttributeError:
            character = "Unspecified"
        category = movie.find( "b" ).next_sibling

        if category == "\n":
            category = "Movie"
        else:
            category = category.split("(")[1].split(")")[0]

        release_year = movie.find("span").text.split("\n")[1]
        return Movie(title, character, category, release_year)

    def _set_actors_name(self, soup):
        self.actors_name = soup.findAll("span", "itemprop")
        return self.actors_name[0].text

    def get_actors_name(self):
        return self.actors_name

    def get_movies_collection(self):
        return self.movie_collection


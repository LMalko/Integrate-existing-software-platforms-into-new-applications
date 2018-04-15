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

        self.actors_name = self._set_actors_name(soup)

        self.write_collection_to_csv_file(self.movie_collection)

    @staticmethod
    def check_url_response(link):
        response = requests.get(link)
        return response

    def set_movies_collection(self, soup):
        movies = self.get_movies(soup)
        for movie in movies:
            temp_movie = self.set_movie_object(movie)
            self.movie_collection.append(temp_movie)

    @staticmethod
    def get_movies(soup):
        return soup.findAll('div', id=lambda x: x and x.startswith('actor-'))

    def write_collection_to_csv_file(self, collection):
        with open(f"{self.get_actors_name()} Movies.csv", "w", encoding="utf-8", newline='') as file:
            csv_writer = writer(file)
            csv_writer.writerow(["Title", "Character", "Year", "Category"])
            for item in collection:
                csv_writer.writerow([item.title, item.character_played, item.release_year, item.category])

    @staticmethod
    def set_movie_object(movie):
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
        self.actors_name = soup.findAll("span", itemprop="name")
        return self.actors_name[0].text

    def get_actors_name(self):
        return self.actors_name


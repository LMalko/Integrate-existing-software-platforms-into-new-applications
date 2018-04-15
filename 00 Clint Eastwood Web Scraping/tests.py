import unittest
from Controller.AppController import AppController
from Model.Movie import Movie

class AppControllerTests(unittest.TestCase):

    app_controller = AppController ( "http://www.imdb.com/name/nm0000142/" )

    def test_response(self):
        self.assertEqual(str(self.app_controller.response), "<Response [200]>")

    def test_movie_collection(self):
        self.assertTrue(all(isinstance(item, Movie) for item in self.app_controller.get_movies_collection()))
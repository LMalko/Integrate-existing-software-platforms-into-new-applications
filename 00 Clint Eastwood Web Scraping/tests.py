import unittest
from Controller.AppController import AppController
from Model.Movie import Movie

class AppControllerTests(unittest.TestCase):

    def test_response(self):
        app_controller = AppController ( "http://www.imdb.com/name/nm0000142/" )
        self.assertEqual(str(app_controller.get_response()), "<Response [200]>")

    def test_movie_collection(self):
        app_controller = AppController("http://www.imdb.com/name/nm0000143/")
        self.assertTrue(all(isinstance(item, Movie) for item in app_controller.get_movies_collection()))


if __name__ == '__main__':
    unittest.main()
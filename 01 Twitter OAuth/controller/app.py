import sys
sys.path.append("..")
from model.database import Database
from model.flask_operator import *


class App:

    def __init__(self):
        self.request_token = None

    def initialize_database(self, **kwargs):
        Database().initialize(**kwargs)


    def start_app(self):

        initiate_flask_operator()

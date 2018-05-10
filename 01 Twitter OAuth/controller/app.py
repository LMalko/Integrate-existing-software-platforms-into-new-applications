import sys
sys.path.append("..")
from view.view import View
from controller.login import Login
import urllib.parse as urlparse


class App:

    view = View()


    def start_app(self):
        login = Login()
        if login.get_response_status() != 200:
            self.view.display_message("An error occured")
        request_token = \
            dict(urlparse.parse_qsl(login.get_content().decode("utf-8")))
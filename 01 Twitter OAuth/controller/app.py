import sys
sys.path.append("..")
from view.view import View
from controller.login import Login
import urllib.parse as urlparse
from enums.constants import Constants

class App:

    view = View()


    def start_app(self):
        login = Login()
        if login.get_response_status() != 200:
            self.view.display_message("An error occured")
        request_token = dict(urlparse.parse_qsl(
            login.get_content().decode("utf-8")))

        self.view.display_message("\nGo to the following site: \n")
        self.view.display_message(
            f"{Constants.AUTHORIZATION_URL.value}?oauth_token={request_token['oauth_token']}")

        authentication_verifier = self.view.get_user_input("What is the PIN?")
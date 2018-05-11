import sys
sys.path.append("..")
from view.view import View
from controller.login import Login
import urllib.parse as urlparse
from enums.constants import Constants
import oauth2

class App:

    view = View()
    login = Login()


    def start_app(self):

        request_token = self.get_request_token()
        client = self.get_client(request_token)
        access_token = self.get_access_token(client)


    def get_request_token(self):
        if self.login.get_response_status() != 200:
            self.view.display_message("An error occured")
        request_token = dict(urlparse.parse_qsl(
            self.login.get_content().decode("utf-8")))

        return request_token


    def get_client(self, request_token):

        self.view.display_message("\nGo to the following site: \n")
        self.view.display_message(
            f"{Constants.AUTHORIZATION_URL.value}?oauth_token={request_token['oauth_token']}")

        authorization_verifier = self.view.get_user_input("What is the PIN? --> ")

        token = oauth2.Token(request_token['oauth_token'],
                             request_token['oauth_token_secret'])

        token.set_verifier(authorization_verifier)

        client = oauth2.Client(self.login.get_consumer(), token)

        return client

    def get_access_token(self, client):

        request, content = client.request(Constants.ACCESS_TOKEN_URL.value, "POST")
        access_token = dict(urlparse.parse_qsl(content.decode("utf-8")))

        return access_token


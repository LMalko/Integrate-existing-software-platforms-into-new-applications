import sys
import json
sys.path.append("..")
from view.view import View
from controller.login import Login
from enums.constants import Constants
from model.user import User
from model.database import Database


class App:

    view = View()
    login = Login()

    def __init__(self):
        self.user_email = None
        self.consumer = None
        self.user = None

    @staticmethod
    def initialize_database(**kwargs):
        Database().initialize(**kwargs)


    def start_app(self):

        self.user = self.get_user()

        if self.user:
            pass
        else:
            access_token = self.get_access_token()

            self.create_user(access_token)

        authorized_client = self.get_authorized_client()

        # Make Twitter API calls.
        response, content = authorized_client.request(
            "https://api.twitter.com/1.1/search/tweets.json?q=barcelona+messi", "GET")

        self.check_response_status(response)

        # Convert bytes to string & display first. Then get string representation.
        tweets = json.loads(content.decode("utf-8"))

        for tweet in tweets["statuses"]:
            try:
                print(tweet["text"])
            except UnicodeEncodeError:
                print(UnicodeEncodeError)

    def get_user(self):

        self.user_email = self.view.get_user_input("What is Your email?")

        user = User.load_from_db_by_email(self.user_email)

        return user

    def create_user(self, access_token):

        self.user = self.create_user(access_token)

        self.user.save_to_db()

    def get_access_token(self):
        self.consumer = self.login.get_consumer()

        client = self.login.get_client(self.consumer)

        response, content = self.login.get_request(client)

        self.check_response_status(response)

        request_token = self.login.get_request_token(content)

        authorization_verifier = self.get_authorization_verifier(request_token)

        client = self.login.get_verified_client(self.consumer, request_token, authorization_verifier)

        access_token = self.login.get_access_token(client)

        return access_token

    def get_authorized_client(self):

        authorized_token = self.login.get_authorized_token(self.user.get_oauth_token,
                                                           self.user.get_oauth_token_secret)

        authorized_client = self.login.get_authorized_client(self.consumer, authorized_token)

        return authorized_client


    def get_authorization_verifier(self, request_token):
        # Ask the user to authorize app and give the pin code.
        self.view.display_message("\nGo to the following site: \n")
        self.view.display_message(
            f"{Constants.AUTHORIZATION_URL.value}?oauth_token={request_token['oauth_token']}")

        authorization_verifier = self.view.get_user_input("What is the PIN? --> ")

        return authorization_verifier

    def check_response_status(self, response):
        if self.login.get_response_status(response) != 200:
            self.view.display_message("An error occured")

    def create_user(self, access_token):
        first_name = self.view.get_user_input("First name --> ")
        last_name = self.view.get_user_input ( "Last name --> " )

        return User(None, first_name, last_name, self.user_email,
                    access_token["oauth_token"], access_token["oauth_token_secret"])




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

    def initialize_database(self, **kwargs):
        Database().initialize(**kwargs)


    def start_app(self):

        authorized_client = self.authorize_client()


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


    def authorize_client(self):
        consumer = self.login.get_consumer()

        client = self.login.get_client(consumer)

        response, content = self.login.get_request(client)

        self.check_response_status(response)

        request_token = self.login.get_request_token(content)

        authorization_verifier = self.get_authorization_verifier(request_token)

        client = self.login.get_verified_client(consumer, request_token, authorization_verifier)

        access_token = self.login.get_access_token(client)

        user_email = self.view.get_user_input("Enter Your email address --> ")

        user = User.load_from_db_by_email(user_email)

        if not user:

            user = self.create_user(access_token)

            user.save_to_db()

        authorized_token = self.login.get_authorized_token(access_token)

        authorized_client = self.login.get_authorized_client(consumer, authorized_token)

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
        email = self.view.get_user_input ( "email --> " )

        return User(None, first_name, last_name, email,
                    access_token["oauth_token"], access_token["oauth_token_secret"])

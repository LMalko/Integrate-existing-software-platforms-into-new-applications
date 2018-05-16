import sys
import json
sys.path.append("..")
from view.view import View
from controller.login import Login
from model.user import User
from model.database import Database
# from model.flask_operator import *


class App:

    view = View()
    login = Login()

    def __init__(self):
        self.request_token = None

    def initialize_database(self, **kwargs):
        Database().initialize(**kwargs)


    def start_app(self):

        authorized_client = self.authorize_client()

        # Make Twitter API calls.
        response, content = authorized_client.request(
            "https://api.twitter.com/1.1/search/tweets.json?q=barcelona+messi", "GET")

        # Convert bytes to string & display first. Then get string representation.
        tweets = json.loads(content.decode("utf-8"))

        self.display_tweets(tweets)


    def authorize_client(self):
        access_token = self.get_access_token()

        user = self.get_user(access_token)

        authorized_token = self.login.get_authorized_token(access_token)

        consumer = self.login.get_consumer()

        authorized_client = self.login.get_authorized_client(consumer, authorized_token)

        return authorized_client

    def get_access_token(self):

        self.request_token = self.login.get_request_token()

        authorization_verifier = self.get_authorization_verifier(self.request_token)

        access_token = self.login.get_access_token(self.request_token, authorization_verifier)

        return access_token

    def get_authorization_verifier(self, request_token):
        # Ask the user to authorize app and give the pin code.
        self.view.display_message("\nGo to the following site: \n")
        self.view.display_message(self.login.get_auth_verifier_url(request_token))

        authorization_verifier = self.view.get_user_input("What is the PIN? --> ")

        return authorization_verifier

    def get_user(self, access_token):

        user_email = self.view.get_user_input("Enter Your email address --> ")
        user = User.load_from_db_by_email(user_email)

        if not user:
            user = self.create_user(user_email, access_token)
            user.save_to_db ()

        return user

    def create_user(self, email, access_token):
        first_name = self.view.get_user_input("First name --> ")
        last_name = self.view.get_user_input ( "Last name --> " )

        return User(None, first_name, last_name, email,
                    access_token["oauth_token"], access_token["oauth_token_secret"])

    @staticmethod
    def display_tweets(tweets):

        count = 1
        for tweet in tweets["statuses"]:
            try:
                print(f"{'{:04d}'.format(count)}. {tweet['text']}")
            except UnicodeEncodeError:
                print(UnicodeEncodeError)
            count += 1

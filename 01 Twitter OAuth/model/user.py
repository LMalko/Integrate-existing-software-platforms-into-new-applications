import sys
sys.path.append("..")
from model.database import *
from controller.login import Login
import oauth2
import json

class User:

    def __init__(self, id, screen_name, oauth_token, oauth_token_secret):
        self.id = id
        self.screen_name = screen_name
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret


    def get_oauth_token(self):
        return self.oauth_token

    def get_oauth_token_secret(self):
        return self.oauth_token_secret

    def get_screen_name(self):
        return self.screen_name

    def __repr__(self):
        return f"User: {self.screen_name}"

    def save_to_db(self):

        with CursorFromConnectionFromPool() as cursor:

                cursor.execute("INSERT INTO users (screen_name, oauth_token, "
                                                            "oauth_token_secret) "
                                 "VALUES (%s, %s, %s);", (self.screen_name,
                                                            self.oauth_token, self.oauth_token_secret))

    @classmethod
    def load_from_db_by_screen_name(cls, screen_name):
        with CursorFromConnectionFromPool() as cursor:

                cursor.execute("SELECT * FROM users WHERE screen_name=%s", (screen_name,))

                user_data = cursor.fetchone()
                if user_data:
                    return cls(id=user_data[0], screen_name=user_data[1],
                               oauth_token=user_data[2], oauth_token_secret=user_data[3])

    def twitter_request(self, uri, verb='GET'):
        authorized_token = oauth2.Token(self.oauth_token, self.oauth_token_secret)
        authorized_client = oauth2.Client(Login.get_consumer(), authorized_token)

        # Make Twitter API calls!
        response, content = authorized_client.request ( uri, verb )
        if response.status != 200:
            print ( "An error occurred when searching!" )

        return json.loads(content.decode('utf-8'))

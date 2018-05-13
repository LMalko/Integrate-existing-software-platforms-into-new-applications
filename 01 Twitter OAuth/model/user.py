import sys
sys.path.append("..")
from model.database import *

class User:

    def __init__(self, id, first_name, last_name, email,
                 oauth_token, oauth_token_secret):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.oauth_token = oauth_token
        self.oauth_token_secret = oauth_token_secret

    def __repr__(self):
        return f"{self.first_name} {self.last_name} has id " \
                                        f"{self.id} & email {self.email}."

    def save_to_db(self):

        with CursorFromConnectionFromPool() as cursor:

                cursor.execute ( "INSERT INTO users (first_name, last_name, "
                                 "email, oauth_token, oauth_token_secret) "
                                 "VALUES (%s, %s, %s, %s, %s);", (self.first_name, self.last_name,
                                                          self.email, self.oauth_token, self.oauth_token_secret))

    @classmethod
    def load_from_db_by_email(cls, email):
        with CursorFromConnectionFromPool() as cursor:

                cursor.execute("SELECT * FROM users WHERE email=%s", (email,))

                user_data = cursor.fetchone()
                return cls(id=user_data[0], first_name=user_data[1],
                           last_name=user_data[2], email=user_data[3])
from enum import Enum

class Constants(Enum):

    # Parts of the account.
    CONSUMER_KEY = "64a5gYM61dBaLE9PQ2BzUe6P6"
    CONSUMER_SECRET = "S5XQMrrPf9icKdumju8DqrigA7fBPpP0sLQZWKKuO6B4qdqjQx"

    # Parts of Twitter API.
    # https://developer.twitter.com/en/docs/basics/authentication/overview/pin-based-oauth

    REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
    ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"
    AUTHORIZATION_URL = "https://api.twitter.com/oauth/authorize"

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title
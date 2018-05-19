import sys
sys.path.append("..")
from enums.constants import Constants
import oauth2
import urllib.parse as urlparse


class Login:

    # Create a consumer, which uses CONSUMER_KEY and
    # CONSUMER_SECRET to identify our app uniquely.
    consumer = oauth2.Consumer(Constants.CONSUMER_KEY.value,
                                        Constants.CONSUMER_SECRET.value)

    @classmethod
    def get_consumer(cls):
        return cls.consumer

    @classmethod
    def get_request_token(cls):
        client = oauth2.Client(cls.consumer)

        response, content = client.request(Constants.REQUEST_TOKEN_URL.value, 'POST')
        if response.status != 200:
            print ( "An error occurred getting the request token from Twitter!" )

        # Get the request token parsing the query string.
        request_token = dict(urlparse.parse_qsl(content.decode( "utf-8")))
        return request_token

    @staticmethod
    def get_auth_verifier_url(request_token):
        return f"{Constants.AUTHORIZATION_URL.value}?oauth_token={request_token['oauth_token']}"

    @classmethod
    def get_access_token(cls, request_token, authorization_verifier):

        token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'] )
        token.set_verifier(authorization_verifier)

        client = oauth2.Client(cls.consumer, token)
        # Ask Twitter for an access token after the request token was verified.
        response, content = client.request(Constants.ACCESS_TOKEN_URL.value, 'POST')
        return dict(urlparse.parse_qsl(content.decode('utf-8')))

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

    # @classmethod
    # def get_consumer(cls):
    #     return cls.consumer

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

    @staticmethod
    def get_authorized_token(access_token):

        # Create an 'authorized_token object and use that to
        # perform Twitter API calls
        # This authorized token will represent the user that authorized the application.
        authorized_token = oauth2.Token(access_token['oauth_token'],
                                        access_token['oauth_token_secret'])
        return authorized_token

    @staticmethod
    def get_authorized_client(consumer, authorized_token):
        authorized_client = oauth2.Client(consumer, authorized_token)
        return authorized_client

import sys
sys.path.append("..")
from enums.constants import Constants
import oauth2
import urllib.parse as urlparse


class Login:

    @staticmethod
    def get_consumer():
        # Create a consumer, which uses CONSUMER_KEY and
        # CONSUMER_SECRET to identify our app uniquely.
        consumer = oauth2.Consumer(Constants.CONSUMER_KEY.value,
                                          Constants.CONSUMER_SECRET.value)
        return consumer

    @staticmethod
    def get_client(consumer):
        client = oauth2.Client(consumer)
        return client

    @staticmethod
    def get_request(client):
        # Use the client to perform a request for the request token.
        return client.request(Constants.REQUEST_TOKEN_URL.value, "POST" )

    @staticmethod
    def get_response_status(response):
        return response.status

    @staticmethod
    def get_request_token(content):
        # Get the request token parsing the query string.
        request_token = dict(urlparse.parse_qsl(content.decode( "utf-8")))
        return request_token

    @staticmethod
    def get_verified_client(consumer, request_token, authorization_verifier):

        # Create a Token object which contains the request token,
        # and the verifier.
        token = oauth2.Token(request_token['oauth_token'],
                             request_token['oauth_token_secret'])

        token.set_verifier(authorization_verifier)

        # Create a client with the consumer (our app) and the newly
        # created (and verified) token.
        client = oauth2.Client(consumer, token)

        return client

    @staticmethod
    def get_access_token(client):

        # Ask Twitter for an access token after the request token was verified.
        response, content = client.request(Constants.ACCESS_TOKEN_URL.value, "POST")
        access_token = dict(urlparse.parse_qsl(content.decode("utf-8")))

        return access_token

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
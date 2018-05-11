import sys
sys.path.append("..")
from enums.constants import Constants
import oauth2


class Login:

    consumer = oauth2.Consumer(Constants.CONSUMER_KEY.value,
                                      Constants.CONSUMER_SECRET.value)
    client = oauth2.Client(consumer)

    def __init__(self):
        self.response, self.content = self.client.request(Constants.REQUEST_TOKEN_URL.value, "POST")

    def get_response_status(self):
        return self.response.status

    def get_content(self):
        return self.content

    def get_consumer(self):
        return self.consumer
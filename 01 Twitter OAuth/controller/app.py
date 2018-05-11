import sys
sys.path.append("..")
from view.view import View
from controller.login import Login
from enums.constants import Constants


class App:

    view = View()
    login = Login()


    def start_app(self):

        authorized_client = self.authorize_client()




    def authorize_client(self):
        consumer = self.login.get_consumer()

        client = self.login.get_client(consumer)

        response, content = self.login.get_request(client)

        if self.login.get_response_status(response) != 200:
            self.view.display_message("An error occured")

        request_token = self.login.get_request_token(content)

        authorization_verifier = self.get_authorization_verifier(request_token)

        client = self.login.get_verified_client(consumer, request_token, authorization_verifier)

        access_token = self.login.get_access_token(client)

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




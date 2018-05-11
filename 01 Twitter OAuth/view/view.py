class View:

    def display_message(self, message):
        print(message)

    def get_user_input(self, message):
        message = '\n' + message
        return input(message)
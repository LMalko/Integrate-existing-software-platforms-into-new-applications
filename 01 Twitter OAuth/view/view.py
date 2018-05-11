class View:

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def get_user_input(message):
        message = '\n' + message
        return input(message)
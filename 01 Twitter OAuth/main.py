from controller.app import App


def main():
    application = App()
    application.initialize_database(minconn=5, maxconn=10,
                                                         database="TwitterOAuth",
                                                         user="postgres",
                                                         password="admin",
                                                         host="localhost",
                                                         port=5433)
    application.start_app()


if __name__ == "__main__":
    main()
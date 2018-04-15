from Controller.AppController import *
from sys import argv


def main():
    try:
        actor_IMBD_home = argv[1].split ( "?" )[0]
    except IndexError:
        actor_IMBD_home = "http://www.imdb.com/name/nm0000142/?ref_=nv_sr_1".split("?")[0]
    app = AppController(actor_IMBD_home)
    print("\nData was successfully saved in .csv file.")


if __name__ == "__main__":
    main()
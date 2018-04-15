from Controller.AppController import *


def main():
    actor_IMBD_home = "http://www.imdb.com/name/nm0000126/?ref_=tt_ov_st_sm".split("?")[0]
    app = AppController(actor_IMBD_home)


if __name__ == "__main__":
    main()
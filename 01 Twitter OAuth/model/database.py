from psycopg2 import pool

class CursorFromConnectionFromPool:

    def __init__(self):
        self.__connection = None
        self.__cursor = None


    def __enter__(self):
        self.__connection = Database.get_connection()
        self.__cursor = self.__connection.cursor()
        return self.__cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        # 3 exception parameters allow us to deal with exceptions if error in sql.
        if exception_value is not None:
            # If error -> rollback
            self__connection.rollback()
        else:
            self.__cursor.close()
            self.__connection.commit()
            # Close connection and return it to the pool.
            Database.return_connection(self.__connection)

class Database:

    __connection_pool = None

    @classmethod
    def initialize(cls, **kwargs):
        cls.__connection_pool = pool.SimpleConnectionPool(**kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        return cls.__connection_pool.putconn(connection)

    @classmethod
    def close_connections(cls):
        cls.__connection_pool.closeall()
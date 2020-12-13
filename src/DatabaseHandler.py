import psycopg2
import logging

class DatabaseHandler:
    default_db_name = "template1"

    def __init__(self):
        self.conn   = None
        self.cursor = None

    def execute(self, query, error_message):
        logger = logging.getLogger('test')
        nr_notices = len(self.conn.notices)
        try:
            self.cursor.execute(query)
        except Exception as exception:
            print(error_message)
            print(exception)
        for notice in self.conn.notices[nr_notices:]:
            print(notice)

    def make_connection(self, name, hostname, username, password):
        self.conn = psycopg2.connect(dbname=name, user=username, password=password, host=hostname)

        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def close_connection(self):
        if self.conn:
            self.conn.cursor().close()
            self.conn.close()

    def load_procedures(self):
        sql_contents = open('sql/create_database.sql', "r").read()
        self.execute(sql_contents, "ERROR LOADING PROCEDURES")

    def create_database(self, name):
        self.load_procedures()
        self.execute("SELECT CreateDB('"+name+"');", "ERROR CREATING DB");
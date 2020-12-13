import psycopg2


class DatabaseHandler:
    default_db_name = "postgres"

    def __init__(self):
        self.conn   = None
        self.cursor = None

    def execute(self, query, error_message):
        try:
            self.cursor.execute(query)
        except:
            print(error_message)

    def make_connection(self, name, hostname, username, password):
        self.conn = psycopg2.connect(dbname=name, user=username, password=password, host=hostname)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def close_connection(self):
        if self.conn:
            self.conn.cursor().close()
            self.conn.close()

    def load_procedures(self):
        sql_contents = open('sql/procedures.sql', "r").read()
        self.execute(sql_contents, "ERROR LOADING PROCEDURES")

    def create_database(self, name):
        self.load_procedures()
        self.execute("call CreateDB("+name+");", "ERROR CREATING DB");
import psycopg2
import logging


class DatabaseHandler:

    default_db_name = "postgres"
    create_db_function_script_path = "sql/create_database.sql"
    functions_and_procedures_script_path = "sql/procedures.sql"

    create_error = -1
    database_created = 0
    database_exists = 1

    def __init__(self):
        self.conn = None
        self.cursor = None
        self.hostname = "127.18.0.3"
        self.username = "postgres"
        self.password = "changeme"
        self.db_name = None

    def execute(self, query, error_message=None):
        nr_notices = len(self.conn.notices)
        try:
            self.cursor.execute(query)
        except Exception as exception:
            if (error_message):
                print(error_message)
            else:
                print("ERROR_MESSAGE_NOT_SPECIFIED")
            print(exception)
            return False
        for notice in self.conn.notices[nr_notices:]:
            print(notice)
        return True

    def make_connection(self, name, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.db_name = name
        self.conn = psycopg2.connect(dbname=name, user=username, password=password, host=hostname)
        self.conn.autocommit = True
        self.cursor = self.conn.cursor()

    def close_connection(self):
        if self.conn:
            self.conn.cursor().close()
            self.conn.close()
        self.conn = None

    def load_procedures(self, script_path):
        sql_contents = open(script_path, "r").read()
        return self.execute(sql_contents, "ERROR LOADING PROCEDURES")

    def switch_db(self, name):
        procedures_loaded = self.load_procedures(self.create_db_function_script_path)
        db_ok = self.execute("SELECT CreateDB('"+name+"');", "ERROR CREATING DB")
        db_exists = "NOTICE:  Database already exists\n" in self.conn.notices
        if procedures_loaded and db_ok:
            self.close_connection()
            self.make_connection(name, self.hostname, self.username, self.password)
            if db_exists:
                print('Database already exists. Skipping sample data creation.')
                return self.database_exists
            else:
                print('DB created. Inserting sample data.')
                procedures_loaded = self.load_procedures(self.functions_and_procedures_script_path)
                if procedures_loaded:
                    self.execute("CALL CreateTables();", "ERROR CREATING TABLE STRUCTURE")
                    self.execute("CALL FillAllTables();", "ERROR FILLING ALL TABLES")
                    return self.database_created
                else:
                    return self.create_error
        else:
            print("ERROR CREATING SAMPLE DATABASE. PROCEDURES:", procedures_loaded, "DB_OK:", db_ok)
            return self.create_error

    @staticmethod
    def parse_data(data):
        data = [item[0] for item in data]
        try:
            parsed_data = []
            for item in data:
                spl = item.split(',')
                spl = [item.replace("'", "") for item in spl]
                spl = [item.replace('"', "") for item in spl]
                spl = [item.replace("(", "") for item in spl]
                spl = [item.replace(")", "") for item in spl]
                parsed_data.append(spl)
            return parsed_data
        except Exception as e:
            print('ex', e)

    def get_table(self, table):
        success = False
        if table.lower() == "doctor":
            success = self.execute("SELECT PrintDoctors();")
        if table.lower() == "patient":
            success = self.execute("SELECT PrintPatients();")
        if table.lower() == "service":
            success = self.execute("SELECT PrintServices();")
        if table.lower() == "logbook":
            success = self.execute("SELECT PrintLogbook();")
        if success:
            data = self.cursor.fetchall()
            if not data:
                return "empty"
            else:
                return self.parse_data(data)
        else:
            return False

    def delete_db(self):
        name = self.db_name
        self.close_connection()
        self.make_connection(DatabaseHandler.default_db_name, self.hostname, self.username, self.password)
        return self.execute("SELECT DeleteDB('" + name + "');", "ERROR CREATING DB")

    def clear_table(self, table):
        return self.execute("SELECT ClearTables('{"+table+"}');")

    def clear_all_tables(self):
        return self.execute("SELECT ClearTables('{Doctor, Service, Logbook, Patient}');")

    def delete_by_phone(self, phone):
        return self.execute("CALL DeletePatientByPhone('"+phone+"');")

    def search_by_phone(self, phone):
        success = self.execute("SELECT SearchPatientByPhone('"+phone+"');")
        if success:
            data = self.cursor.fetchall()
            if not data:
                return "empty"
            else:
                return self.parse_data(data)
        else:
            return False

    def add_appointment(self, client, phone, doctor, service, date):
        return self.execute("CALL insertClients('"+client+"', '"+phone+"', '"+date+"', '"+doctor+"', '"+service+"')")

    def change_appointment_date(self, appointment_id, new_date):
        return self.execute("call ChangeDateOfMeet("+appointment_id+", '"+new_date+"');")

    def delete_apointment(self, appointment_id):
        return self.execute("call delmeetbyid("+appointment_id+");")



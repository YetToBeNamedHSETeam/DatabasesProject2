from PyQt5.QtWidgets import QMainWindow
from ui.MainWindow import Ui_MainWindow
from src.DatabaseHandler import DatabaseHandler as DBHandler
import src.misc as misc


class ProjectApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db_handler = DBHandler()
        self.connect_button.clicked.connect(self.on_connect_pressed)
        self.connection_status_label.show()
        self.connect_button.show()
        self.table_view.hide()
        self.show()

    def on_connect_pressed(self):
        hostname = "127.18.0.3"
        username = "postgres"
        password = "changeme"
        self.db_handler.make_connection(DBHandler.default_db_name, hostname, username, password)
        new_db_name = "plastic_surgery"
        result = self.db_handler.switch_db(new_db_name)
        if result == DBHandler.create_error:
            misc.change_rich_label(rich_text_label=self.connection_status_label,
                                   new_text="Connection failed. Try again.")
        else:
            if result == DBHandler.database_exists:
                misc.change_rich_label(rich_text_label=self.connection_status_label, new_text="DB detected.")
            elif result == DBHandler.database_created:
                misc.change_rich_label(rich_text_label=self.connection_status_label, new_text="DB created.")
            self.connect_button.setText("Continue")
            self.connect_button.clicked.disconnect()
            self.connect_button.clicked.connect(self.on_continue_pressed)

    def on_continue_pressed(self):
        print("Enter")
        self.connection_status_label.hide()
        self.connect_button.hide()
        print(self.db_handler.get_table("doctor"))
        self.table_view.show()

    def closeEvent(self, event):
        self.db_handler.close_connection()
        super().closeEvent(event)

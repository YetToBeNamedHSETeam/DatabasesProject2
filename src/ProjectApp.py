from PyQt5 import QtWidgets
from ui import MainWindow
from src.DatabaseHandler import DatabaseHandler as DBHandler


class ProjectApp(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.on_connect_pressed)

        self.database_handler = DBHandler()
        self.database_handler.make_connection(DBHandler.default_db_name, "127.18.0.3", "postgres", "changeme")
        self.database_handler.load_procedures()
        self.database_handler.create_database("test")

        self.show()

    def on_connect_pressed(self):
        self.label.hide()

    def closeEvent(self, event):
        print("closing")
        if self.database_handler:
            self.database_handler.close_connection()
        super().closeEvent(event)

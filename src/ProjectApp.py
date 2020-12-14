from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from ui.MainWindow import Ui_MainWindow
from src.DatabaseHandler import DatabaseHandler as DBHandler
import src.misc as misc
from src.TableHandler import TableHandler as THandler


class ProjectApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db_handler = DBHandler()
        self.table_handler = THandler(self.table_widget, self.db_handler)
        misc.change_rich_label(rich_text_label=self.connection_status_label,
                               new_text="Disconnected.")
        self.connection_status_label.show()
        self.connect_button.show()
        self.continue_button.hide()
        self.delete_db_button.hide()
        self.setup_connections()
        self.table_handler.hide_table_widget()
        self.show()

    current_table_changed = pyqtSignal(str)

    def setup_connections(self):
        self.connect_button.clicked.connect(self.on_connect_clicked)
        self.continue_button.clicked.connect(self.on_continue_clicked)
        self.delete_db_button.clicked.connect(self.on_delete_db_clicked)
        self.table_handler.widget_hidden.connect(self.on_table_hidden)
        self.table_handler.widget_shown.connect(self.on_table_shown)
        self.select_table_combo_box.currentTextChanged.connect(self.table_handler.on_current_table_changed)
        self.edit_check_box.stateChanged.connect(self.table_handler.on_edit_toggle)

    def on_connect_clicked(self):
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
        self.connect_button.hide()
        self.continue_button.show()
        self.delete_db_button.show()

    def on_continue_clicked(self):
        self.connection_status_label.hide()
        self.continue_button.hide()
        self.delete_db_button.hide()
        self.select_table_combo_box.currentTextChanged.emit(self.select_table_combo_box.currentText())
        self.table_handler.show_table_widget()

    def on_delete_db_clicked(self):
        if self.db_handler.delete_db():
            self.db_handler.close_connection()
            misc.change_rich_label(rich_text_label=self.connection_status_label, new_text="DB deleted. Disconnected.")
            self.continue_button.hide()
            self.delete_db_button.hide()
            self.connect_button.show()
        else:
            misc.change_rich_label(rich_text_label=self.connection_status_label, new_text="DB deletion error. Try again.")

    def closeEvent(self, event):
        self.db_handler.close_connection()
        super().closeEvent(event)

    def on_table_hidden(self):
        self.combo_box_label.hide()
        self.select_table_combo_box.hide()
        self.edit_check_box.hide()

    def on_table_shown(self):
        self.combo_box_label.show()
        self.select_table_combo_box.show()
        self.edit_check_box.show()

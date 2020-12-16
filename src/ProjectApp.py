from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal

from ui.MainWindow import Ui_MainWindow

from src.DatabaseHandler import DatabaseHandler as DBHandler
from src.TableHandler import TableHandler as THandler
from src.SearchDialog import SearchDialog as PhoneSearch
from src.AddAppointmentDialog import AddAppointmentDialog as AddAppointment

import src.misc as misc


class ProjectApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.search_window = PhoneSearch()
        self.appointment_window = AddAppointment()
        self.db_handler = DBHandler()
        self.table_handler = THandler(self.table_widget, self.db_handler)
        misc.change_rich_label(rich_text_label=self.connection_status_label,
                               new_text="Disconnected.")
        self.connection_status_label.show()
        self.connect_button.show()
        self.continue_button.hide()
        self.delete_db_button.hide()
        self.add_appointment_button.hide()
        self.setup_connections()
        self.table_handler.hide_table_widget()
        self.menu_bar.hide()
        self.show()

    current_table_changed = pyqtSignal(str)
    search_by_phone = pyqtSignal(str)
    delete_by_phone = pyqtSignal(str)

    def setup_connections(self):
        self.connect_button.clicked.connect(self.on_connect_clicked)
        self.continue_button.clicked.connect(self.on_continue_clicked)
        self.delete_db_button.clicked.connect(self.on_delete_db_clicked)
        self.action_disconnect_and_delete.triggered.connect(self.on_delete_db_clicked)
        self.action_disconnect.triggered.connect(self.on_disconnect_clicked)
        self.clear_table_button.clicked.connect(self.table_handler.clear_current_table)
        self.action_clear_current_table.triggered.connect(self.table_handler.clear_current_table)
        self.action_clear_all.triggered.connect(self.table_handler.clear_all_tables)
        self.table_handler.widget_visibility_changed.connect(self.on_table_visibility_changed)
        self.select_table_combo_box.currentTextChanged.connect(self.table_handler.on_current_table_changed)
        self.select_table_combo_box.currentTextChanged.connect(self.table_chosen)
        self.action_search_by_phone.triggered.connect(self.search_window.search_dialog)
        self.action_delete_by_phone.triggered.connect(self.search_window.delete_dialog)
        self.search_window.search.connect(self.search_by_phone)
        self.search_window.delete.connect(self.delete_by_phone)
        self.search_by_phone.connect(self.table_handler.search_by_phone)
        self.delete_by_phone.connect(self.table_handler.delete_by_phone)
        self.table_handler.results.connect(self.search_window.results)
        self.table_handler.change_table.connect(self.select_table_combo_box.setCurrentText)
        self.appointment_window.add_appointment.connect(self.table_handler.on_add_appointment)
        self.add_appointment_button.clicked.connect(self.prepare_appointment_dialog)

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
            return
        else:
            if result == DBHandler.database_exists:
                misc.change_rich_label(rich_text_label=self.connection_status_label, new_text="DB detected.")
            elif result == DBHandler.database_created:
                misc.change_rich_label(rich_text_label=self.connection_status_label, new_text="DB created.")
        self.connect_button.hide()
        self.continue_button.show()
        self.delete_db_button.show()
        self.menu_bar.show()
        self.menu_table.setEnabled(False)
        self.menu_phone.setEnabled(False)

    def on_continue_clicked(self):
        self.connection_status_label.hide()
        self.continue_button.hide()
        self.delete_db_button.hide()
        self.select_table_combo_box.currentTextChanged.emit(self.select_table_combo_box.currentText())
        self.table_handler.show_table_widget()
        self.menu_table.setEnabled(True)
        self.menu_phone.setEnabled(True)

    def on_delete_db_clicked(self):
        self.table_handler.hide_table_widget()
        if self.db_handler.delete_db():
            self.db_handler.close_connection()
            misc.change_rich_label(rich_text_label=self.connection_status_label, new_text="DB deleted. Disconnected.")
            self.continue_button.hide()
            self.delete_db_button.hide()
            self.connect_button.show()
            self.connection_status_label.show()
            self.menu_bar.hide()
            self.add_appointment_button.hide()
        else:
            misc.change_rich_label(rich_text_label=self.connection_status_label, new_text="DB deletion error. Try again.")

    def on_disconnect_clicked(self):
        self.table_handler.hide_table_widget()
        self.db_handler.close_connection()
        misc.change_rich_label(rich_text_label=self.connection_status_label, new_text="Disconnected.")
        self.continue_button.hide()
        self.delete_db_button.hide()
        self.connect_button.show()
        self.connection_status_label.show()
        self.menu_bar.hide()
        self.add_appointment_button.hide()

    def closeEvent(self, event):
        self.db_handler.close_connection()
        super().closeEvent(event)

    def on_table_visibility_changed(self, show):
        self.combo_box_label.setVisible(show)
        self.select_table_combo_box.setVisible(show)
        self.clear_table_button.setVisible(show)

    def table_chosen(self):
        if self.select_table_combo_box.currentText() == "Logbook":
            self.add_appointment_button.show()
        else:
            self.add_appointment_button.hide()

    def prepare_appointment_dialog(self):
        doctors = [data[1] for data in self.db_handler.get_table("Doctor")]
        services = [data[1] for data in self.db_handler.get_table("Service")]
        self.appointment_window.update_doctors_and_services(doctors, services)
        self.appointment_window.show()



from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QWidget, QHBoxLayout, QAbstractScrollArea
from PyQt5.QtCore import QObject, pyqtSignal, Qt, QEvent
from src.SetDateDialog import SetDateDialog as EditDateDialog


class TableHandler(QObject):
    widget_visibility_changed = pyqtSignal(bool)
    results = pyqtSignal(bool)
    change_table = pyqtSignal(str)
    edit_date = pyqtSignal(int, str)

    columns_dict = dict(Doctor=['DoctorID', 'DoctorName'],
                        Patient=['PatientID', 'PatientName', 'Phone', 'DateOfInsert'],
                        Service=['ServiceID', 'Title', 'Cost'],
                        Logbook=['Number', 'Date', 'Patient', 'Service', 'Doctor'])

    def __init__(self, table_widget, db_handler):
        super().__init__()
        self.table_widget = table_widget
        self.table_widget.installEventFilter(self)
        self.db_handler = db_handler
        self.edit_dialog = EditDateDialog()
        self.current_table = None
        self.data = None
        self.search_results = QTableWidget()
        self.search_results.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.search_results.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.search_results_window = QWidget()
        layout = QHBoxLayout(self.search_results_window)
        layout.addWidget(self.search_results)
        self.search_results_window.setLayout(layout)
        self.search_results_window.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.connect_signals()

    def connect_signals(self):
        self.table_widget.cellDoubleClicked.connect(self.on_cell_double_clicked)
        self.edit_date.connect(self.edit_dialog.edit_date)
        self.edit_dialog.send_date.connect(self.on_new_date)

    def show_table_widget(self):
        self.table_widget.show()
        self.widget_visibility_changed.emit(True)

    def hide_table_widget(self):
        self.table_widget.clear()
        self.table_widget.hide()
        self.widget_visibility_changed.emit(False)

    @staticmethod
    def set_columns(new_table, table):
        columns = TableHandler.columns_dict[new_table]
        num_columns = len(columns)
        table.setColumnCount(num_columns)
        table.setHorizontalHeaderLabels(columns)

    @staticmethod
    def set_rows(data, table):
        if not data:
            print("TableHandler: ERROR FETCHING DATA")
            return
        if data == "empty":
            return
        num_items = len(data)
        table.setRowCount(num_items)
        for row in range(num_items):
            for column in range(table.columnCount()):
                table.setItem(row, column, QTableWidgetItem(str(data[row][column])))

    def on_current_table_changed(self, new_table):
        self.current_table = new_table
        self.table_widget.clear()
        self.set_columns(new_table, self.table_widget)
        raw_data = self.db_handler.get_table(new_table)
        if new_table == "Logbook":
            doctors = self.db_handler.get_table("Doctor")
            patients = self.db_handler.get_table("Patient")
            services = self.db_handler.get_table("Service")
            doctors_dict = {doctor[0]: doctor[1] for doctor in doctors}
            patients_dict = {patient[0]: patient[1] for patient in patients}
            services_dict = {service[0]: service[1] for service in services}
            for log in raw_data:
                log[2] = patients_dict[log[2]]
                log[3] = services_dict[log[3]]
                log[4] = services_dict[log[4]]
        self.set_rows(raw_data, self.table_widget)

    def clear_current_table(self):
        if self.db_handler.clear_table(self.current_table):
            self.table_widget.clear()
            self.set_columns(self.current_table, self.table_widget)
        else:
            print('TableHandler: ERROR CLEARING CURRENT TABLE')

    def clear_all_tables(self):
        if self.db_handler.clear_all_tables():
            self.table_widget.clear()
        else:
            print("TableHandler: ERROR CLEARING ALL TABLES")

    def search_by_phone(self, phone):
        self.search_results.clear()
        self.set_columns("Patient", self.search_results)
        data = self.db_handler.search_by_phone(phone)
        if data == "empty":
            self.results.emit(False)
            return
        else:
            self.results.emit(True)
            self.set_rows(data, self.search_results)
            self.search_results_window.adjustSize()
            self.search_results_window.setWindowTitle("Search results for phone "+phone)
            self.search_results_window.show()

    def refresh(self, table):
        if self.current_table == table:
            self.on_current_table_changed(table)
        else:
            self.change_table.emit(table)

    def delete_by_phone(self, phone):
        self.db_handler.delete_by_phone(phone)
        self.refresh("Patient")

    def on_add_appointment(self, client, phone, doctor, service, date):
        self.db_handler.add_appointment(client, phone, doctor, service, date)
        self.refresh("Logbook")

    def on_cell_double_clicked(self, row, column):
        if self.current_table == "Logbook" and column == 1:
            self.edit_date.emit(row, self.table_widget.item(row, column).text())

    def on_new_date(self, row, date):
        self.db_handler.change_appointment_date(self.table_widget.item(row, 0).text(), date)
        self.refresh("Logbook")

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress and self.current_table == "Logbook":
            if event.key() == Qt.Key_Delete:
                item = self.table_widget.item(self.table_widget.currentRow(), 0)
                if item:
                    appointment_id = item.text()
                    self.db_handler.delete_apointment(appointment_id)
                    self.refresh("Logbook")
                    return True
        return obj.event(event)


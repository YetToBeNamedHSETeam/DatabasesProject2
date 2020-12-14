from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView
from PyQt5.QtCore import QObject, pyqtSignal


class TableHandler(QObject):
    widget_hidden = pyqtSignal()
    widget_shown = pyqtSignal()

    columns_dict = {
        'Doctor': ['DoctorID', 'DoctorName'],
        'Patient': ['PatientID', 'PatientName', 'Phone', 'DateOfInsert'],
        'Service': ['ServiceID', 'Title', 'Cost'],
        'Logbook': ['Number', 'Date', 'Patient']
    }

    def __init__(self, table_widget, db_handler):
        super().__init__()
        self.table_widget = table_widget
        self.db_handler = db_handler
        self.current_table = None
        self.connect_signals()

    def connect_signals(self):
        self.table_widget.cellChanged.connect(self.on_cell_edited)

    def show_table_widget(self):
        self.table_widget.show()
        self.widget_shown.emit()

    def hide_table_widget(self):
        self.table_widget.hide()
        self.widget_hidden.emit()

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

    def on_current_table_changed(self, new_table):
        self.current_table = new_table
        self.table_widget.clear()
        data = TableHandler.parse_data(self.db_handler.get_table(new_table))
        columns = TableHandler.columns_dict[new_table]
        num_columns = len(columns)
        num_items = len(data)
        self.table_widget.setColumnCount(num_columns)
        self.table_widget.setRowCount(num_items)
        self.table_widget.setHorizontalHeaderLabels(columns)
        for row in range(num_items):
            for column in range(num_columns):
                self.table_widget.setItem(row, column, QTableWidgetItem(str(data[row][column])))

    def on_edit_toggle(self, state):
        if state == 0:
            self.table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        else:
            self.table_widget.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.EditKeyPressed)

    def on_cell_edited(self, row, column):
        print(row, column)
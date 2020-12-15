from PyQt5.QtCore import pyqtSignal, QDate
from PyQt5.QtWidgets import QDialog
from ui.SetDateDialog import Ui_SetDateDialog


class SetDateDialog(QDialog, Ui_SetDateDialog):
    def __init__(self):
        super(SetDateDialog, self).__init__()
        self.setupUi(self)
        self.setup_connections()
        self.row = None
        self.column = None

    send_date = pyqtSignal(int, str)

    def setup_connections(self):
        self.cancel_button.clicked.connect(self.hide)
        self.set_button.clicked.connect(self.send_new_date)

    def edit_date(self, row, date):
        self.row = row
        date_split = date.split('-')
        date_split = [int(date) for date in date_split]
        self.date_edit.setDate(QDate(date_split[0], date_split[1], date_split[2]))
        self.show()

    def send_new_date(self):
        self.send_date.emit(self.row, self.date_edit.text().replace('.', '/'))
        self.hide()

from PyQt5.QtCore import pyqtSignal, QDate
from PyQt5.QtWidgets import QDialog
from ui.AddAppointmentDialog import Ui_AddAppointmentDialog


class AddAppointmentDialog(QDialog, Ui_AddAppointmentDialog):
    def __init__(self):
        super(AddAppointmentDialog, self).__init__()
        self.setupUi(self)
        self.setup_connections()
        self.date_edit.setDate(QDate.currentDate())
        self.error_label.hide()

    add_appointment = pyqtSignal(str, str, str, str, str)

    def setup_connections(self):
        self.button_cancel.clicked.connect(self.hide)
        self.button_add.clicked.connect(self.send_data)

    def hideEvent(self, hide_event):
        self.doctor_combobox.clear()
        self.service_combobox.clear()
        self.client_box.clear()
        self.phone_box.clear()
        self.date_edit.setDate(QDate.currentDate())
        return super().hideEvent(hide_event)

    def update_doctors_and_services(self, doctors, services):
        self.doctor_combobox.addItems(doctors)
        self.service_combobox.addItems(services)

    def send_data(self):
        self.add_appointment.emit(self.client_box.text(),
                                  self.phone_box.text(),
                                  self.doctor_combobox.currentText(),
                                  self.service_combobox.currentText(),
                                  self.date_edit.text().replace('.', '/'))

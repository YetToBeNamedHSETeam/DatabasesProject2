from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog
from ui.SearchDialog import Ui_SearchDialog


class SearchDialog(QDialog, Ui_SearchDialog):
    def __init__(self):
        super(SearchDialog, self).__init__()
        self.setupUi(self)
        self.setup_connections()
        self.search_string = ""
        self.no_results_label.hide()

    search = pyqtSignal(str)
    delete = pyqtSignal(str)

    def setup_connections(self):
        self.cancel_search_button.clicked.connect(self.hide)
        self.phone_number_box.textChanged.connect(self.on_text_changed)
        self.search_button.clicked.connect(self.emit_signal)

    def search_dialog(self):
        self.show()
        self.search_button.setText("Search")
        self.phone_number_box.setFocus()

    def delete_dialog(self):
        self.show()
        self.search_button.setText("Delete")
        self.phone_number_box.setFocus()

    def hideEvent(self, hide_event):
        self.phone_number_box.clear()
        return super().hideEvent(hide_event)

    def on_text_changed(self, text):
        self.search_string = text

    def emit_signal(self):
        if self.search_button.text() == "Search":
            self.search.emit(self.search_string)
        else:
            self.delete.emit(self.search_string)
        self.hide()

    def results(self, results):
        if results:
            self.no_results_label.hide()
        else:
            self.no_results_label.show()

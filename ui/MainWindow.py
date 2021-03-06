# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setObjectName("central_widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.central_widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 781, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.main_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setObjectName("main_layout")
        self.connection_layout = QtWidgets.QVBoxLayout()
        self.connection_layout.setObjectName("connection_layout")
        self.connection_status_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.connection_status_label.setObjectName("connection_status_label")
        self.connection_layout.addWidget(self.connection_status_label, 0, QtCore.Qt.AlignBottom)
        self.connect_button_layout = QtWidgets.QHBoxLayout()
        self.connect_button_layout.setObjectName("connect_button_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.connect_button_layout.addItem(spacerItem)
        self.connect_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.connect_button.setObjectName("connect_button")
        self.connect_button_layout.addWidget(self.connect_button, 0, QtCore.Qt.AlignTop)
        self.continue_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.continue_button.setObjectName("continue_button")
        self.connect_button_layout.addWidget(self.continue_button, 0, QtCore.Qt.AlignTop)
        self.delete_db_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.delete_db_button.setObjectName("delete_db_button")
        self.connect_button_layout.addWidget(self.delete_db_button, 0, QtCore.Qt.AlignTop)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.connect_button_layout.addItem(spacerItem1)
        self.connection_layout.addLayout(self.connect_button_layout)
        self.main_layout.addLayout(self.connection_layout)
        self.table_widget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.table_widget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(0)
        self.table_widget.setRowCount(0)
        self.table_widget.verticalHeader().setVisible(False)
        self.main_layout.addWidget(self.table_widget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clear_table_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clear_table_button.setObjectName("clear_table_button")
        self.horizontalLayout_2.addWidget(self.clear_table_button)
        self.add_appointment_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_appointment_button.setObjectName("add_appointment_button")
        self.horizontalLayout_2.addWidget(self.add_appointment_button)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.combo_box_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.combo_box_label.setObjectName("combo_box_label")
        self.horizontalLayout_2.addWidget(self.combo_box_label)
        self.select_table_combo_box = QtWidgets.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_table_combo_box.sizePolicy().hasHeightForWidth())
        self.select_table_combo_box.setSizePolicy(sizePolicy)
        self.select_table_combo_box.setMinimumSize(QtCore.QSize(80, 0))
        self.select_table_combo_box.setObjectName("select_table_combo_box")
        self.select_table_combo_box.addItem("")
        self.select_table_combo_box.addItem("")
        self.select_table_combo_box.addItem("")
        self.select_table_combo_box.addItem("")
        self.horizontalLayout_2.addWidget(self.select_table_combo_box)
        self.main_layout.addLayout(self.horizontalLayout_2)
        self.table_layout = QtWidgets.QHBoxLayout()
        self.table_layout.setObjectName("table_layout")
        self.main_layout.addLayout(self.table_layout)
        MainWindow.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(MainWindow)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menu_bar.setObjectName("menu_bar")
        self.menu_db = QtWidgets.QMenu(self.menu_bar)
        self.menu_db.setObjectName("menu_db")
        self.menu_table = QtWidgets.QMenu(self.menu_bar)
        self.menu_table.setObjectName("menu_table")
        self.menu_clear = QtWidgets.QMenu(self.menu_table)
        self.menu_clear.setObjectName("menu_clear")
        self.menu_phone = QtWidgets.QMenu(self.menu_bar)
        self.menu_phone.setObjectName("menu_phone")
        MainWindow.setMenuBar(self.menu_bar)
        self.action_disconnect = QtWidgets.QAction(MainWindow)
        self.action_disconnect.setObjectName("action_disconnect")
        self.action_disconnect_and_delete = QtWidgets.QAction(MainWindow)
        self.action_disconnect_and_delete.setObjectName("action_disconnect_and_delete")
        self.action_clear_current_table = QtWidgets.QAction(MainWindow)
        self.action_clear_current_table.setObjectName("action_clear_current_table")
        self.action_clear_all = QtWidgets.QAction(MainWindow)
        self.action_clear_all.setObjectName("action_clear_all")
        self.action_search_by_phone = QtWidgets.QAction(MainWindow)
        self.action_search_by_phone.setObjectName("action_search_by_phone")
        self.action_delete_by_phone = QtWidgets.QAction(MainWindow)
        self.action_delete_by_phone.setObjectName("action_delete_by_phone")
        self.menu_db.addAction(self.action_disconnect)
        self.menu_db.addAction(self.action_disconnect_and_delete)
        self.menu_clear.addAction(self.action_clear_current_table)
        self.menu_clear.addAction(self.action_clear_all)
        self.menu_table.addAction(self.menu_clear.menuAction())
        self.menu_phone.addAction(self.action_search_by_phone)
        self.menu_phone.addAction(self.action_delete_by_phone)
        self.menu_bar.addAction(self.menu_db.menuAction())
        self.menu_bar.addAction(self.menu_table.menuAction())
        self.menu_bar.addAction(self.menu_phone.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Клиника пластической хирургии \"Билли Джин\""))
        self.connection_status_label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Connection status</span></p></body></html>"))
        self.connect_button.setText(_translate("MainWindow", "Connect"))
        self.continue_button.setText(_translate("MainWindow", "Continue"))
        self.delete_db_button.setText(_translate("MainWindow", "Delete DB"))
        self.clear_table_button.setText(_translate("MainWindow", "Clear table"))
        self.add_appointment_button.setText(_translate("MainWindow", "Add new appointment"))
        self.combo_box_label.setText(_translate("MainWindow", "Choose table to view:"))
        self.select_table_combo_box.setItemText(0, _translate("MainWindow", "Doctor"))
        self.select_table_combo_box.setItemText(1, _translate("MainWindow", "Patient"))
        self.select_table_combo_box.setItemText(2, _translate("MainWindow", "Service"))
        self.select_table_combo_box.setItemText(3, _translate("MainWindow", "Logbook"))
        self.menu_db.setTitle(_translate("MainWindow", "Database"))
        self.menu_table.setTitle(_translate("MainWindow", "Table"))
        self.menu_clear.setTitle(_translate("MainWindow", "Clear"))
        self.menu_phone.setTitle(_translate("MainWindow", "Phone"))
        self.action_disconnect.setText(_translate("MainWindow", "Disconnect"))
        self.action_disconnect_and_delete.setText(_translate("MainWindow", "Disconnect and delete DB"))
        self.action_clear_current_table.setText(_translate("MainWindow", "Clear current table"))
        self.action_clear_all.setText(_translate("MainWindow", "Clear all"))
        self.action_search_by_phone.setText(_translate("MainWindow", "Search by phone"))
        self.action_delete_by_phone.setText(_translate("MainWindow", "Delete by phone"))

import sys
from PyQt5.QtWidgets import QApplication
from src.ProjectApp import ProjectApp as App


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = App()
    app.exec_()
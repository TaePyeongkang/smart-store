import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import *
import pymysql

thread_form = uic.loadUiType("threading.ui")[0]


class ThreadingWidget(QWidget, thread_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    th = ThreadingWidget()
    th.show()
    app.exec_()

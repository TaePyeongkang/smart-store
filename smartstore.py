import pymysql
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QComboBox
from datetime import datetime

form_class = uic.loadUiType('smartstore.ui')[0]

class smartStore(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.loginYN = False
        self.stackedWidget.setCurrentIndex(0)
        self.join_home_1.clicked.connect(self.MainPage)
        self.order_home_2.clicked.connect(self.MainPage)
        self.login_home_1.clicked.connect(self.MainPage)
        self.inquire_home_3.clicked.connect(self.MainPage)
        self.cancel.clicked.connect(self.MainPage)
        self.login_btn.clicked.connect(self.LoginPage)
        self.join_btn.clicked.connect(self.joinPage)
        self.order_manage.clicked.connect(self.order_btn)           # 주문 관리
        self.inventory_manage.clicked.connect(self.inventory_btn)   # 재고 관리


    def inventory_btn(self):
        self.stackedWidget.setCurrentIndex(4)

    def order_btn(self):
        self.stackedWidget.setCurrentIndex(3)

    def joinPage(self): # 회원가입 페이지로 이동
        self.stackedWidget.setCurrentIndex(2)

    def LoginPage(self): # 로그인 페이지로 이동
        self.stackedWidget.setCurrentIndex(1)

    def MainPage(self):  # 메인페이지로 이동하는 함수
        self.stackedWidget.setCurrentIndex(0)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = smartStore()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.show()
    app.exec_()
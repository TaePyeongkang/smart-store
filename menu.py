import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql

menu_form = uic.loadUiType("menu.ui")[0]


class MenuWidget(QWidget, menu_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.printMenu.clicked.connect(self.print_menu)
        self.addMenu.clicked.connect(self.add_menu)
        self.printStuff.clicked.connect(self.print_stuff)
        self.addStuff.clicked.connect(self.add_stuff)
        self.stuffMenu.returnPressed.connect(self.print_stuff)

    def print_menu(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        curs = conn.cursor()
        curs.execute("select * from store.menu")
        menus = curs.fetchall()
        self.menu.setRowCount(len(menus))
        for i in range(len(menus)):
            for j in range(len(menus[i])):
                self.menu.setItem(i, j, QTableWidgetItem(str(menus[i][j])))

    def add_menu(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        curs = conn.cursor()
        curs.execute("insert into store.menu (name, price) values ('%s', %d)" %
                     (self.menuName.text(), int(self.menuPrice.text())))
        conn.commit()
        self.print_menu()

    def print_stuff(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        curs = conn.cursor()
        curs.execute("select * from store.bom where 메뉴 = '%s'" % self.stuffMenu.text())
        stuff = curs.fetchall()
        self.stuff.setRowCount(len(stuff))
        for i in range(len(stuff)):
            for j in range(len(stuff[i])):
                self.stuff.setItem(i, j, QTableWidgetItem(str(stuff[i][j])))

    def add_stuff(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        curs = conn.cursor()
        curs.execute("insert into store.bom values ('%s', '%s', '%s', '%s', %f, %f, %d)" %
                     (self.stuffMenu.text(), self.stuffName.text(), self.hsCode.text(), self.whereFrom.text(),
                      int(self.heavy.text()), int(self.onePrice.text()), int(self.allPrice.text())))
        conn.commit()
        self.print_stuff()


# 테스트
if __name__ == "__main__":
    app = QApplication(sys.argv)

    menu = MenuWidget()
    menu.show()
    app.exec_()

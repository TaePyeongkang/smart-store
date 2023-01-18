import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pymysql

menu_form = uic.loadUiType("menu.ui")[0]


class MenuWidget(QWidget, menu_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menu.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.menu.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.stuff.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.stuff.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.printMenu.clicked.connect(self.print_menu)
        self.addMenu.clicked.connect(self.add_menu)
        self.printStuff.clicked.connect(self.print_stuff)
        self.addStuff.clicked.connect(self.add_stuff)
        self.stuffMenu.returnPressed.connect(self.print_stuff)
        self.menu.cellClicked.connect(self.cell_print_stuff)

    # def move_order(self):
    #     self.setCurrentIndex(2)

    # def move_question(self):
    #     self.setCurrentIndex(3)

    def print_menu(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        curs = conn.cursor()
        curs.execute("select * from store.menu")
        menus = curs.fetchall()
        self.menu.setRowCount(len(menus))
        for i in range(len(menus)):
            for j in range(len(menus[i])):
                self.menu.setItem(i, j, QTableWidgetItem(str(menus[i][j])))
        conn.close()

    def add_menu(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        curs = conn.cursor()
        curs.execute("insert into store.menu (name, price) values ('%s', %d)" %
                     (self.menuName.text(), int(self.menuPrice.text())))
        conn.commit()
        self.print_menu()
        conn.close()

    def print_stuff(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        curs = conn.cursor()
        curs.execute("select * from store.bom where 메뉴 = '%s'" % self.stuffMenu.text())
        stuff = curs.fetchall()
        self.stuff.setRowCount(len(stuff))
        for i in range(len(stuff)):
            for j in range(len(stuff[i])):
                self.stuff.setItem(i, j, QTableWidgetItem(str(stuff[i][j])))
        conn.close()

    def cell_print_stuff(self):
        self.stuffMenu.setText(self.menu.item(self.menu.currentRow(), 0).text())
        self.print_stuff()

    def add_stuff(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        curs = conn.cursor()
        curs.execute("insert into store.bom values ('%s', '%s', '%s', '%s', %f, %f, %d)" %
                     (self.stuffMenu.text(), self.stuffName.text(), self.hsCode.text(), self.whereFrom.text(),
                      int(self.heavy.text()), int(self.onePrice.text()), int(self.allPrice.text())))
        conn.commit()
        self.print_stuff()
        conn.close()


# 테스트
if __name__ == "__main__":
    app = QApplication(sys.argv)

    menu = MenuWidget()
    menu.show()
    app.exec_()

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
        self.loginYN = False
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
        self.join_double_check.clicked.connect(self.double_check)
        self.join.clicked.connect(self.signup)
        self.login.clicked.connect(self.Login)
        self.inquire.clicked.connect(self.order_list)
        self.order.clicked.connect(self.order_page)
        self.menu_order.clicked.connect(self.order_menu)

    def order_menu(self):
        price = 8000
        state = '접수대기'
        ch_state = '준비중'
        if self.menu1.isChecked() == False or self.menu1count.value() == 0:
            print('선택 X')
        elif self.menu1.isChecked() == True and self.menu1count.value() > 0:
            print(f"{self.menu1.text()} {self.menu1count.value()}개 주문")
            # print(self.menu1.text())
            # print(self.menu1count.value())
            # if self.menu1count.value() == 0:
            #     print('X')
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='smart-store',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(f"insert into menu_check (상품,개수,가격,주문상태) values ('{self.menu1.text()}','{self.menu1count.value()}','{price * self.menu1count.value()}','{state}')")
        conn.commit()
        conn.close()
        self.stackedWidget.setCurrentIndex(3)
        QMessageBox.information(self, "알림", f"{self.menu1.text()}{self.menu1count.value()}개")




    def order_list(self):
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='smart-store',
                               charset='utf8')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM menu_check")
        self.menu_check = cursor.fetchall()
        conn.close()
        print(self.menu_check)
        Row = 0
        self.order_table.setRowCount(len(self.menu_check))
        for i in self.menu_check:
            self.order_table.setItem(Row, 0, QTableWidgetItem(i[1]))       # 상품명
            self.order_table.setItem(Row, 1, QTableWidgetItem(str(i[2])))  # 개수
            self.order_table.setItem(Row, 2, QTableWidgetItem(str(i[3])))  # 가격
            self.order_table.setItem(Row, 3, QTableWidgetItem(str(i[4])))  # 주문상태
            self.order_table.setItem(Row, 4, QTableWidgetItem(i[5]))       # 가격
            Row += 1

    def signup(self):
        if self.Join_name.text() == '' or self.join_id.text() == '' or self.join_pw.text() == '' or self.join_pw_2.text() == '' or self.join_call.text() == '' or self.join_addredss.text() == '':
            QMessageBox.critical(self, "에러", "빈칸을 전부 입력해주세요")
        elif self.join_pw.text() != self.join_pw_2.text():
            QMessageBox.critical(self, "에러", "비밀번호와 비밀번호확인이 일치하지 않습니다.")
        elif self.join_double_check == False:
            QMessageBox.critical(self, "에러", "중복확인을 해주세요")
        else:
            conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='smart-store',
                                   charset='utf8')
            cur = conn.cursor()
            cur.execute(
                f'INSERT INTO login (이름, 아이디, 비밀번호, 연락처, 주소) VALUES ("{self.Join_name.text()}", "{self.join_id.text()}", '
                f'"{self.join_pw.text()}", "{self.join_call.text()}", "{self.join_addredss.text()}")')
            conn.commit()
            conn.close()
            QMessageBox.information(self, "확인", "회원가입에 성공하셨습니다")
            self.Join_name.clear()
            self.join_id.clear()
            self.join_pw.clear()
            self.join_pw_2.clear()
            self.join_call.clear()
            self.join_addredss.clear()
            self.stackedWidget.setCurrentIndex(0)

    def double_check(self):
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='smart-store',
                               charset='utf8')
        cur = conn.cursor()
        cur.execute(f'SELECT 아이디 FROM login WHERE 아이디 = "{self.join_id.text()}"')
        checking = cur.fetchall()
        conn.close()
        print(checking)
        self.join_double_check = False
        if self.join_id.text() == '':
            QMessageBox.critical(self, "에러", "아이디를 입력해주세요")
        elif checking != ():
            QMessageBox.critical(self, "에러", "중복된 아이디 입니다")
            self.loginYN = False
        else:
            self.join_double_check = True
            QMessageBox.information(self, "확인", "사용가능한 아이디입니다")
            # self.join_double_check = False
            # self.join_id.textChanged.connect(self.id_change_forbid)

    # def id_change_forbid(self):
    #     if self.join_double_check == False:
    #         QMessageBox.critical(self, "에러", "중복체크 다시해주세요")


    def Login(self):  # 로그인 할때

        self.id = self.login_id.text()  # 입력한 값이 id
        self.pw = self.login_pw.text()  # 입력한 값이 pw
        conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='smart-store',
                               charset='utf8')  # db 연결
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM login where 아이디 = %s", self.id)  # db에 있는 해당 아이디의 행의 값을 가져옴
        self.result = cursor.fetchall()
        conn.close()
        print(self.result)

        if self.login_id == '' or self.login_pw == '':  # 아이디나 비밀번호가 공백일때  로그인 오류 표시
            QMessageBox.critical(self, "로그인 오류", "정보를 입력하세요")

        elif self.result == ():  # 일치하는 값이 없으면 ()로 나옴 그때 오류 표시
            QMessageBox.critical(self, "로그인 오류", "일치하는 정보가 없습니다")

        elif self.result[0][1] == self.id and self.result[0][2] == self.pw:  # 아이디와 비밀번호가 일치했을때  로그인 성공 메시지 표시함
            QMessageBox.information(self, "로그인 성공", f"{self.result[0][0]}님 로그인 성공하셨습니다")
            self.loginYN = True  # 로그인 여부가 참
            self.stackedWidget.setCurrentIndex(0)

    def order_page(self):
        self.stackedWidget.setCurrentIndex(5)
    def inventory_btn(self):
        self.stackedWidget.setCurrentIndex(4)

    def order_btn(self):
        # if self.loginYN == True:
        self.stackedWidget.setCurrentIndex(3)
        # else:a
        #     QMessageBox.information(self, "주문관리", "로그인해야 이용가능합니다")


    def joinPage(self): # 회원가입 페이지로 이동
        self.join_double_check = False
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
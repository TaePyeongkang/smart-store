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

        # 회원가입 함수

    def Double_Check(self):  # 회원가입 페이지-중복 확인하는 함수
        user = self.join_id.text()  # id_lineEdit에 입력되는 텍스트
        dc = 0  # 임의로 지정한 변수
        lines = open('Userinfo.txt', 'r').read().split('\n')  # txt 파일에 저장된 정보를 \n로 구분된 리스트로 만듦
        for i in range(len(lines)):
            data = lines[i].split('\n')  # lisnes[i] 값을 ','로 구분된 리스트로 만듦
            # data가 lines의 요소라서(Userinfo.txt의 한 줄) 정보를 다 읽은 후에 알림을 띄우려면 변수로 리턴값을 주고 조건문으로 알림창이 나오게 해야됨
            if (user + '\n') in lines:
                dc = 1  # 변수에 임의의 값 저장
                break
            elif (user + '\n') not in lines:
                dc = 2
                self.checkStatus = True
                break
            else:
                pass
        if dc == 1:
            QMessageBox.critical(self, "알림", "아이디 중복")
        elif dc == 2:
            QMessageBox.information(self, "알림", "사용 가능한 아이디")

    def Double_change(self):
        self.checkStatus = False

    def Sign_Up(self):
        id = self.id_lineEdit.text()  # lineEdit에 입력받은 데이터
        pw1 = self.pw_lineEdit.text()
        pw2 = self.pw2_lineEdit.text()
        name = self.name_lineEdit.text()
        phone = self.phone_lineEdit.text()
        address = self.address_lineEdit.text()

        user = [id, pw1, name, phone, address]  # 정보 저장 순서

        with open('Userinfo.txt', 'a') as f:
            # 회원가입 시 필요한 조건
            if pw1 != pw2:
                QMessageBox.critical(self, "알림", "비밀번호가 일치하지 않습니다. 다시 확인해주세요")

            elif self.checkStatus == False:
                QMessageBox.critical(self, "알림", "아이디 중복 확인이 안 되어있습니다")

            elif id == '' or pw1 == '' or name == '' or phone == '' or address == '':
                QMessageBox.critical(self, "알림", "정보를 입력하세요")

            else:
                QMessageBox.information(self, "알림", "회원가입 됐습니다")
                f.writelines(f"\n{id},{pw1},{name},{phone},{address}")  # 사용자 정보 저장
                self.login_SW.setCurrentIndex(1)
                # Line_edit에 입력 받은 값 지워주기
                self.id_lineEdit.clear()
                self.pw_lineEdit.clear()
                self.pw2_lineEdit.clear()
                self.name_lineEdit.clear()
                self.phone_lineEdit.clear()
                self.address_lineEdit.clear()
                self.agree1_checkBox.setChecked(False)
                self.agree2_checkBox.setChecked(False)
                self.agree3_checkBox.setChecked(False)
                self.agree4_checkBox.setChecked(False)

    def Check_Box(self):
        if self.agree1_checkBox.isChecked() == True:
            self.agree2_checkBox.toggle()
            self.agree3_checkBox.toggle()
            self.agree4_checkBox.toggle()

        # 로그인

    def Login_Check(self):

        if self.login_id_lineEdit.text() == "":
            QMessageBox.critical(self, "로그인 오류", "정보를 입력하세요")
            return
        self.id = self.login_id_lineEdit.text()
        pw = self.login_pw_lineEdit.text()
        logined = 0
        lines = open('Userinfo.txt', 'r').read().split('\n')  # txt 파일에 저장된 정보를 \n로 구분된 리스트로 만듦
        for i in range(len(lines)):
            list = lines[i].split(',')  # lisnes[i] 값을 ','로 구분된 리스트로 만듦
            if self.id not in list[0]:  # list[0] = id
                logined = 1

            elif pw not in list[1]:  # list[1] = pw
                logined = 2
            else:
                logined = 3
                break  # 안해주면 마지막에 가입한 사람만 로그인 됨

        if logined == 1:
            QMessageBox.critical(self, "로그인 오류", "ID 정보가 없습니다. 회원가입 해주세요")
        elif logined == 2:
            QMessageBox.critical(self, "로그인 오류", "비밀번호를 다시 입력하세요")
        elif pw == '':
            QMessageBox.critical(self, "로그인 오류", "비밀번호를 입력하세요")
        else:
            return True  # 로그인 성공

    # def login(self):
    #
    #     self.id = self.login_id.text()  # 입력한 값이 id
    #     self.pw = self.login_pw.text()  # 입력한 값이 pw
    #     conn = pymysql.connect(host='10.10.21.119', port=3306, user='yh', password='00000000', db='smart-store',
    #                            charset='utf8')  # db 연결
    #     cursor = conn.cursor()
    #
    #     cursor.execute(f"SELECT * FROM beacon where 아이디 = %s", self.id)  # db에 있는 해당 아이디의 행의 값을 가져옴
    #     self.result = cursor.fetchall()
    #     conn.close()
    #     # print(self.result)
    #
    #     if self.id == '' or self.pw == '':  # 아이디나 비밀번호가 공백일때  로그인 오류 표시
    #         QMessageBox.critical(self, "로그인 오류", "정보를 입력하세요")
    #         # return # 의미는 무엇인가
    #
    #     elif self.result == ():  # 일치하는 값이 없으면 ()로 나옴 그때 오류 표시
    #         QMessageBox.critical(self, "로그인 오류", "일치하는 정보가 없습니다")
    #
    #     elif self.result[0][3] == self.id and self.result[0][4] == self.pw:  # 아이디와 비밀번호가 일치했을때  로그인 성공 메시지 표시함
    #         if self.result[0][1] <= 27:
    #             QMessageBox.information(self, "로그인 성공", f"{self.result[0][2]}님 로그인 성공하셨습니다")
    #             # print(self.result[0][2])
    #             self.stackedWidget_3.setCurrentIndex(1)  # 로그인 버튼이 로그아웃 버튼으로 변경
    #             self.stackedWidget.setCurrentIndex(1)  # 로그인시 메인페이지로 이동
    #             self.logyn = True  # 로그인 여부가 참
    #         else:
    #             QMessageBox.information(self, "로그인 성공", f"{self.result[0][2]} 교수님 로그인 성공하셨습니다")
    #             self.stackedWidget_3.setCurrentIndex(1)  # 로그인 버튼이 로그아웃 버튼으로 변경
    #             self.stackedWidget.setCurrentIndex(1)  # 로그인시 메인페이지로 이동
    #             self.logyn = True  # 로그인 여부가 참

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
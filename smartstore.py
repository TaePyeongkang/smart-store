import pymysql
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import *
import random

form_class = uic.loadUiType('smartstore.ui')[0]


class SmartStore(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.menu_check = None
        self.setupUi(self)
        self.loginYN = False
        self.stackedWidget.setCurrentIndex(0)
        self.join_home_1.clicked.connect(self.MainPage)
        self.order_home_2.clicked.connect(self.MainPage)
        self.login_home_1.clicked.connect(self.MainPage)
        self.inquire_home_3.clicked.connect(self.MainPage)
        self.inquire_home_4.clicked.connect(self.MainPage)
        self.inquire_home_5.clicked.connect(self.MainPage)
        self.inquire_home_6.clicked.connect(self.MainPage)
        self.cancel.clicked.connect(self.MainPage)
        self.login_btn.clicked.connect(self.LoginPage)
        self.join_btn.clicked.connect(self.joinPage)
        self.order_manage.clicked.connect(self.order_btn)
        self.inventory_manage.clicked.connect(self.inventory_btn)
        self.join_double_check_btn.clicked.connect(self.double_check)
        self.join.clicked.connect(self.signup)
        self.login.clicked.connect(self.Login)
        self.menu_btn.clicked.connect(self.menuPage)
        self.quest_btn.clicked.connect(self.questPage)
        self.inquire.clicked.connect(self.order_list)
        self.order.clicked.connect(self.order_page)
        self.menu_order.clicked.connect(self.order_menu)
        self.take_over.clicked.connect(self.change_state1)
        self.complete.clicked.connect(self.change_state2)
        self.inquire_2.clicked.connect(self.inventory)
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
        self.set_alarm()
        self.questions.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.questions.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.printQuestions.clicked.connect(self.print_questions)
        self.questions.cellClicked.connect(self.print_text)
        self.auto = AutoThread(self)
        self.test_btn.clicked.connect(self.auto.start)

    def order_menu(self):
        pig_price = 8000
        head = 7500
        sundae = 6500
        innards = 7000
        self.state = '접수대기'
        self.id = self.login_id.text()
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        cursor = conn.cursor()
        cursor.execute("select * from store.menu_check")
        length = cursor.fetchall()
        if self.menu1.isChecked() == True and self.menu1count.value() > 0:
            print(f"{self.menu1.text()} {self.menu1count.value()}개 주문")
            cursor.execute(f"insert into store.menu_check values "
                           f"('{len(length) + 1}','{self.id}','{self.menu1.text()}','{self.menu1count.value()}',"
                           f"'{pig_price * self.menu1count.value()}','{self.state}')")
            conn.commit()
            # QMessageBox.information(self, "알림", f"{self.menu1.text()}{self.menu1count.value()}개")

        elif self.menu2.isChecked() == True and self.menu2count.value() > 0:
            print(f"{self.menu2.text()} {self.menu2count.value()}개 주문")
            cursor.execute(f"insert into menu_check (번호,id,상품,개수,가격,주문상태) values "
                           f"('{len(length) + 1}','{self.id}','{self.menu2.text()}',"
                           f"'{self.menu2count.value()}','{head * self.menu2count.value()}','{self.state}')")
            conn.commit()
            # QMessageBox.information(self, "알림", f"{self.menu2.text()}{self.menu2count.value()}개")

        elif self.menu3.isChecked() == True and self.menu3count.value() > 0:
            print(f"{self.menu3.text()} {self.menu3count.value()}개 주문")
            cursor.execute(f"insert into menu_check (번호,id,상품,개수,가격,주문상태) values "
                           f"('{len(length) + 1}','{self.id}','{self.menu3.text()}',"
                           f"'{self.menu3count.value()}','{sundae * self.menu3count.value()}','{self.state}')")
            conn.commit()
            # QMessageBox.information(self, "알림", f"{self.menu3.text()}{self.menu3count.value()}개")

        elif self.menu4.isChecked() == True and self.menu4count.value() > 0:
            print(f"{self.menu4.text()} {self.menu4count.value()}개 주문")
            cursor.execute(f"insert into menu_check (번호,id,상품,개수,가격,주문상태) values "
                           f"('{len(length) + 1}','{self.id}','{self.menu4.text()}',"
                           f"'{self.menu4count.value()}','{innards * self.menu4count.value()}','{self.state}')")
            conn.commit()
            # QMessageBox.information(self, "알림", f"{self.menu4.text()}{self.menu4count.value()}개")

        print('어디가 문제냐')
        cursor.execute("select * from store.menu_check where 주문상태 = '접수대기'")
        self.menu_check = cursor.fetchall()
        conn.close()

        print('여기냐')
        self.stackedWidget.setCurrentIndex(0)
        self.label_16.setText(f"{len(self.menu_check)}")
        self.order_list()

    def order_list(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM menu_check")
        self.menu_check = cursor.fetchall()
        a = cursor.execute(f"SELECT * FROM menu_check where 주문상태 = '접수대기'")
        conn.close()
        Row = 0
        self.order_table.setRowCount(len(self.menu_check))
        for i in self.menu_check:
            self.order_table.setItem(Row, 0, QTableWidgetItem(str(i[0])))  # 번호
            self.order_table.setItem(Row, 1, QTableWidgetItem(i[1]))  # id
            self.order_table.setItem(Row, 2, QTableWidgetItem(str(i[2])))  # 상품명
            self.order_table.setItem(Row, 3, QTableWidgetItem(str(i[3])))  # 개수
            self.order_table.setItem(Row, 4, QTableWidgetItem(str(i[4])))  # 가격
            self.order_table.setItem(Row, 5, QTableWidgetItem(i[5]))  # 주문상태
            Row += 1
        self.label_16.setText(f"{a}")

    def change_state2(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        cursor = conn.cursor()
        cursor.execute(
            f"select 원재료명,소모량 from bom where 메뉴 = '{self.order_table.item(self.order_table.currentRow(), 2).text()}'")
        self.bom = cursor.fetchall()
        cursor.execute(
            f"select * from inventory where 메뉴 = '{self.order_table.item(self.order_table.currentRow(), 2).text()}'")
        self.inven = cursor.fetchall()
        list_inven = []
        for i in self.inven:
            list_inven.append(list(i))

        no_update = False
        for recipe in self.bom:
            for i in list_inven:
                if i[1] == recipe[0]:
                    i[2] -= recipe[1] * int(self.order_table.item(self.order_table.currentRow(), 3).text())
                    if i[2] < 0:
                        no_update = True
        if not no_update:
            for i in list_inven:
                self.ch_state = '완료'
                self.state = '준비중'
                orderitem = self.order_table.item(self.order_table.currentRow(), 0).text()
                self.order_table.item(self.order_table.currentRow(), 5).setText(self.ch_state)
                cursor.execute(f"update menu_check set 주문상태 = '{self.ch_state}' where 번호 = '{orderitem}';")
                cursor.execute("update inventory set 재고량 = %d where 메뉴 = '%s' and 원재료명 = '%s';" % (i[2], i[0], i[1]))
                conn.commit()
        else:
            self.order_table.item(self.order_table.currentRow(), 5).setText('재고부족')
        if i[2] <= 0:
            QMessageBox.information(self, "알림", "재고부족")

        self.inventory()
        a = cursor.execute(f"SELECT * FROM menu_check where 주문상태 = '접수대기'")
        self.label_16.setText(f"{a}")
        conn.close()

    def inventory(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        cursor = conn.cursor()
        cursor.execute(f"select * from inventory where 메뉴 = '돼지국밥'")
        inventory = cursor.fetchall()
        cursor.execute("select * from bom where 메뉴 = '돼지국밥'")
        bom = cursor.fetchall()
        pig = inventory[0][2] / bom[0][4]
        cursor.execute(f"select * from inventory where 메뉴 = '순대국밥'")
        a = cursor.fetchall()
        cursor.execute("select * from bom where 메뉴 = '순대국밥'")
        bom = cursor.fetchall()
        sun = a[0][2] / bom[0][4]
        cursor.execute(f"select * from inventory where 메뉴 = '머리국밥'")
        b = cursor.fetchall()
        cursor.execute("select * from bom where 메뉴 = '머리국밥'")
        bom = cursor.fetchall()
        head = b[0][2] / bom[0][4]
        cursor.execute(f"select * from inventory where 메뉴 = '내장국밥'")
        c = cursor.fetchall()
        cursor.execute("select * from bom where 메뉴 = '내장국밥'")
        bom = cursor.fetchall()
        insen = c[0][2] / bom[0][4]
        conn.close()
        self.inquire_table.setRowCount(len(inventory) + 1)
        self.inquire_table.setItem(0, 0, QTableWidgetItem(str(pig)))
        self.inquire_table.setItem(0, 1, QTableWidgetItem(str(sun)))
        self.inquire_table.setItem(0, 2, QTableWidgetItem(str(head)))
        self.inquire_table.setItem(0, 3, QTableWidgetItem(str(insen)))
        for i in range(len(inventory)):
            self.inquire_table.setItem(i + 1, 0, QTableWidgetItem(str(inventory[i][2])))

        self.inquire_table.setRowCount(len(a) + 1)
        for i in range(len(a)):
            self.inquire_table.setItem(i + 1, 1, QTableWidgetItem(str(a[i][2])))

        self.inquire_table.setRowCount(len(b) + 1)
        for i in range(len(b)):
            self.inquire_table.setItem(i + 1, 2, QTableWidgetItem(str(b[i][2])))

        self.inquire_table.setRowCount(len(c) + 1)
        for i in range(len(b)):
            self.inquire_table.setItem(i + 1, 3, QTableWidgetItem(str(c[i][2])))

    def change_state1(self):
        self.ch_state = '준비중'
        self.state = '접수대기'
        orderitem = self.order_table.item(self.order_table.currentRow(), 0).text()
        self.order_table.item(self.order_table.currentRow(), 5).setText(self.ch_state)
        orderqty = self.order_table.item(self.order_table.currentRow(), 5).text()

        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        cursor = conn.cursor()
        cursor.execute(f"update menu_check set 주문상태 = '{orderqty}' where 번호 = '{orderitem}'")
        conn.commit()
        a = cursor.execute(f"SELECT * FROM menu_check where 주문상태 = '접수대기'")
        self.label_16.setText(f"{a}")
        conn.close()

    def signup(self):
        if self.Join_name.text() == '' or self.join_id.text() == '' or self.join_pw.text() == '' or self.join_pw_2.text() == '' or self.join_call.text() == '' or self.join_addredss.text() == '':
            QMessageBox.critical(self, "에러", "빈칸을 전부 입력해주세요")
        elif self.join_pw.text() != self.join_pw_2.text():
            QMessageBox.critical(self, "에러", "비밀번호와 비밀번호확인이 일치하지 않습니다.")
        elif not self.join_double_check:
            QMessageBox.critical(self, "에러", "중복확인을 해주세요")
        else:
            conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
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
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        cur = conn.cursor()
        cur.execute(f'SELECT 아이디 FROM login WHERE 아이디 = "{self.join_id.text()}"')
        checking = cur.fetchall()
        conn.close()
        self.join_double_check = False
        if self.join_id.text() == '':
            QMessageBox.critical(self, "에러", "아이디를 입력해주세요")
        elif checking != ():
            QMessageBox.critical(self, "에러", "중복된 아이디 입니다")
            self.loginYN = False
        else:
            self.join_double_check = True
            QMessageBox.information(self, "확인", "사용가능한 아이디입니다")

    def Login(self):  # 로그인 할때
        self.id = self.login_id.text()  # 입력한 값이 id
        self.pw = self.login_pw.text()  # 입력한 값이 pw
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')  # db 연결
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM login where 아이디 = %s", self.id)  # db에 있는 해당 아이디의 행의 값을 가져옴
        conn.close()
        self.result = cursor.fetchall()

        if self.login_id == '' or self.login_pw == '':  # 아이디나 비밀번호가 공백일때  로그인 오류 표시
            QMessageBox.critical(self, "로그인 오류", "정보를 입력하세요")

        elif self.result == ():  # 일치하는 값이 없으면 ()로 나옴 그때 오류 표시
            QMessageBox.critical(self, "로그인 오류", "일치하는 정보가 없습니다")

        elif self.result[0][1] == self.id and self.result[0][2] == self.pw:  # 아이디와 비밀번호가 일치했을때  로그인 성공 메시지 표시함
            QMessageBox.information(self, "로그인 성공", f"{self.result[0][0]}님 로그인 성공하셨습니다")
            self.loginYN = True  # 로그인 여부가 참
            self.stackedWidget.setCurrentIndex(0)
            conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')  # db 연결
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM menu_check where 주문상태 = '접수대기'")
            conn.commit()
            conn.close()
            self.menu_check = cursor.fetchall()
            self.label_16.setText(f"{len(self.menu_check)}")
            self.userId.setText("%s님" % self.id)
            self.login_btn.setText("로그아웃")

    def order_page(self):
        if self.loginYN == True:
            self.stackedWidget.setCurrentIndex(5)
        else:
            QMessageBox.information(self, "주문하기", "로그인해야 이용가능합니다")

    def inventory_btn(self):
        if self.loginYN == True:
            self.stackedWidget.setCurrentIndex(4)
        else:
            QMessageBox.information(self, "재고관리", "로그인해야 이용가능합니다")

    def order_btn(self):
        if self.loginYN == True:
            self.stackedWidget.setCurrentIndex(3)
        else:
            QMessageBox.information(self, "주문관리", "로그인해야 이용가능합니다")

    def joinPage(self):  # 회원가입 페이지로 이동
        if self.loginYN == False:
            self.join_double_check = False
            self.stackedWidget.setCurrentIndex(2)

    def LoginPage(self):  # 로그인 페이지로 이동
        if self.login_btn.text() == "로그인":
            self.stackedWidget.setCurrentIndex(1)
            self.login_btn.setText("로그아웃")
        else:
            self.userId.setText("")
            self.login_btn.setText("로그인")
            self.loginYN = False

    def MainPage(self):  # 메인페이지로 이동하는 함수
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM menu_check")
        self.menu_check = cursor.fetchall()
        a = cursor.execute(f"SELECT * FROM menu_check where 주문상태 = '접수대기'")
        # self.label_16.setText(f"{a}")
        conn.commit()
        conn.close()
        self.stackedWidget.setCurrentIndex(0)

    def menuPage(self):
        if self.loginYN == True:
            self.stackedWidget.setCurrentIndex(6)
        else:
            QMessageBox.information(self, "주문관리", "로그인해야 이용가능합니다")

    def questPage(self):
        if self.loginYN == True:
            self.stackedWidget.setCurrentIndex(7)
        else:
            QMessageBox.information(self, "주문관리", "로그인해야 이용가능합니다")

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
        curs.execute("insert into store.menu values ('%s', %d)" %
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

    def print_questions(self):
        self.questId.clear()
        self.questProduct.clear()
        self.questOrder.clear()
        self.questText.clear()
        self.questions.clearContents()
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        curs = conn.cursor()
        curs.execute("select id, product, question_order, question_title from store.question where checked = '미확인'")
        questions = curs.fetchall()
        self.questions.setRowCount(len(questions))
        for i in range(len(questions)):
            for j in range(len(questions[i])):
                self.questions.setItem(i, j, QTableWidgetItem(str(questions[i][j])))
        conn.close()
        self.set_alarm()

    def print_text(self):
        self.questId.clear()
        self.questProduct.clear()
        self.questOrder.clear()
        self.questText.clear()

        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        curs = conn.cursor()
        curs.execute("select * from store.question where question_order = %d" %
                     int(self.questions.item(self.questions.currentRow(), 2).text()))
        now_question = curs.fetchall()
        if len(now_question) > 0:
            self.questId.setPlainText(now_question[0][0])
            self.questProduct.setPlainText(now_question[0][1])
            self.questOrder.setPlainText(str(now_question[0][2]))
            self.questText.setPlainText(now_question[0][3])
        curs.execute("update store.question set checked = '확인' where question_order = %d" %
                     int(self.questions.item(self.questions.currentRow(), 2).text()))
        conn.commit()
        conn.close()
        self.set_alarm()

    def quest(self):
        complain = random.randint(0, 1)
        title = random.randint(0, 2)
        if title == 0:
            quest_title = "맛있었어요"
            quest_text = "국밥이 너무 맛있었어요. 비결이 있으신가요?"
        elif title == 1:
            quest_title = "맛없었어요"
            quest_text = "국밥이 너무 맛없었어요. 환불 가능한가요?"
        else:
            quest_title = "알바 가능한가요?"
            quest_text = "여기서 일하고싶습니다. 알바 구하시나요?"
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        curs = conn.cursor()
        curs.execute("select * from store.menu_check")
        order_num = len(curs.fetchall())
        if complain == 1:
            print("문의가 들어왔다!")
            curs.execute("insert into store.question values ('%s', '국밥', %d, '%s', '%s', '미확인')" %
                         (self.userId.text(), order_num, quest_title, quest_text))
            conn.commit()
        self.questAlarm.setText(str(int(self.questAlarm.text()) + 1))
        self.print_questions()

    def set_alarm(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        curs = conn.cursor()
        curs.execute("select * from store.question where checked = '미확인'")
        self.questAlarm.setText(str(len(curs.fetchall())))
        conn.close()


class AutoThread(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.count = 0
        self.running = True

    def run(self):
        while self.running:
            menu_select = random.randint(0, 3)
            menu_number = random.randint(1, 4)
            if menu_select == 0:
                self.parent.menu1.setChecked(True)
                self.parent.menu1count.setValue(menu_number)
                self.parent.menu1.setChecked(False)
            elif menu_select == 1:
                self.parent.menu2.setChecked(True)
                self.parent.menu2count.setValue(menu_number)
                self.parent.menu2.setChecked(False)
            elif menu_select == 2:
                self.parent.menu3.setChecked(True)
                self.parent.menu3count.setValue(menu_number)
                self.parent.menu3.setChecked(False)
            else:
                self.parent.menu4.setChecked(True)
                self.parent.menu4count.setValue(menu_number)
                self.parent.menu3.setChecked(False)
            print("스레드 작동!")
            self.sleep(5)
            self.parent.order_menu()
            self.parent.quest()
            self.count += 1
            print("스레드 작동 완료!")
            if self.count > 4:
                self.running = False


if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QtWidgets.QStackedWidget()

    mainWindow = SmartStore()

    widget.addWidget(mainWindow)

    widget.setFixedHeight(720)
    widget.setFixedWidth(1280)
    widget.show()
    app.exec_()

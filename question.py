import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import *
import pymysql
import random

quest_form = uic.loadUiType("question.ui")[0]


class QuestionWidget(QWidget, quest_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_alarm()
        self.questions.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.questions.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.printQuestions.clicked.connect(self.print_questions)
        self.questions.cellClicked.connect(self.print_text)
        self.testQuest.clicked.connect(self.quest)

    # def move_menu(self):
    #     self.setCurrentIndex(1)

    # def move_order(self):
    #     self.setCurrentIndex(2)

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
        curs.execute("select * from store.question")
        order_num = len(curs.fetchall())
        if complain == 1:
            print("문의가 들어왔다!")
            curs.execute("insert into store.question values ('user', '국밥', %d, '%s', '%s', '미확인')" %
                         (order_num, quest_title, quest_text))
            conn.commit()
        self.questAlarm.setText(str(int(self.questAlarm.text()) + 1))
        self.print_questions()

    def set_alarm(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        curs = conn.cursor()
        curs.execute("select * from store.question where checked = '미확인'")
        self.questAlarm.setText(str(len(curs.fetchall())))
        conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    question = QuestionWidget()
    question.show()

    app.exec_()

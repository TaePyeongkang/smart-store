import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import *
import pymysql

quest_form = uic.loadUiType("question.ui")[0]


class QuestionWidget(QWidget, quest_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.questions.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.questions.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.printQuestions.clicked.connect(self.print_questions)
        self.questions.cellClicked.connect(self.print_text)
        # self.checking = Checking(self)
        # self.checking.start()

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


# class Checking(QThread):
#     def __init__(self, parent):
#         super().__init__(parent)
#         self.parent = parent
#
#     def run(self):
#         while True:
#             conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
#             curs = conn.cursor()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    question = QuestionWidget()
    question.show()

    app.exec_()

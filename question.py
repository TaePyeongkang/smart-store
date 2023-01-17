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
        self.titleSet.currentTextChanged.connect(self.print_question)

    def print_question(self):
        self.questId.clear()
        self.questProduct.clear()
        self.questText.clear()
        conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
        curs = conn.cursor()
        curs.execute("select * from store.question where question_title = '%s'" % self.titleSet.currentText())
        now_question = curs.fetchall()
        if len(now_question) > 0:
            self.questId.setPlainText(now_question[0][0])
            self.questProduct.setPlainText(now_question[0][1])
            self.questText.setPlainText(now_question[0][3])


class Checking(QThread):
    def run(self):
        while True:
            conn = pymysql.connect(host='127.0.0.1', user='root', password='486486', db='store')
            curs = conn.cursor()
            curs.execute("select * from store.question")
            questions = curs.fetchall()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    question = QuestionWidget()
    question.show()

    app.exec_()

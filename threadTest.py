import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

thread_form = uic.loadUiType("threading.ui")[0]


class ThreadingWidget(QWidget, thread_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.testing.clicked.connect(self.print_text)
        self.testing_2.clicked.connect(self.start_thread)
        self.thread = Thread(self)
        self.thread.start()
        self.thread.yes = True
        print("스레드가 켜집니다.")
        self.testText.append("시작합니다.")

    def print_text(self):
        self.testText.append("추가되었습니다.")

    def start_thread(self):
        if self.thread.yes:
            self.thread.yes = False
            print("스레드가 꺼집니다.")
        else:
            self.thread.yes = True
            self.thread.start()
            print("스레드가 켜집니다.")


class Thread(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.number = 0
        self.yes = False

    def run(self):
        while self.yes:
            self.parent.numberT.setText(str(self.number))
            self.number += 1
            self.parent.print_text()
            self.sleep(1)
            if self.number > 15:
                self.yes = False
                print("스레드가 꺼집니다.")
                self.number = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)

    th = ThreadingWidget()
    th.show()
    app.exec_()

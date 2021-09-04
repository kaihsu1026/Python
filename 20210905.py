import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class First(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 200)
        self.setWindowTitle("練習中")
        self.btn = QPushButton('Jump', self)
        self.btn.setGeometry(50, 100, 100, 50)
        self.btn.clicked.connect(self.slot_btn)
    def slot_btn(self):
        self.hide()
        self.s = SecondUI()
        self.s.show()

class SecondUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(500, 300)
        self.setWindowTitle("2222222")
        self.btn = QPushButton('Jump', self)
        self.btn.setGeometry(150, 100, 100, 50)
        self.btn.clicked.connect(self.slot_btn)
    def slot_btn(self):
        self.hide()
        self.s = First()
        self.s.show()

def main():
    app = QApplication(sys.argv)
    w = First()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

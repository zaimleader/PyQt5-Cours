from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
import sys

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700, 400)
        self.setWindowTitle("hbox Layout")
        self.setWindowIcon(QIcon("c:/Users/pc/Desktop/Programming/Python/PyQt5/images/cliquez-sur.png"))
        self.initUi()

    def initUi(self):
        hbox = QHBoxLayout()

        btn_1 = QPushButton("Button One")
        btn_2 = QPushButton("Button Two")
        btn_3 = QPushButton("Button Three")
        btn_4 = QPushButton("Button Four")

        hbox.addWidget(btn_1)
        hbox.addWidget(btn_2)
        hbox.addWidget(btn_3)
        hbox.addWidget(btn_4)

        self.setLayout(hbox)

def main():
    app = QApplication(sys.argv)
    win = mainWindow()
    win.show()
    sys.exit(app.exec_())

main()
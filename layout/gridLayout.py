from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
import sys

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700, 400)
        self.setWindowTitle("Grid Layout")
        self.setWindowIcon(QIcon("c:/Users/pc/Desktop/Programming/Python/PyQt5/images/cliquez-sur.png"))
        self.initUi()

    def initUi(self):
        grid = QGridLayout()

        btn_1 = QPushButton("Button One")
        btn_2 = QPushButton("Button Two")
        btn_3 = QPushButton("Button Three")

        btn_4 = QPushButton("Button Four")
        btn_5 = QPushButton("Button Five")
        btn_6 = QPushButton("Button Sex")
        
        btn_7 = QPushButton("Button Seven")
        btn_8 = QPushButton("Button Heigh")
        btn_9 = QPushButton("Button Nine")

        grid.addWidget(btn_1, 0, 0)
        grid.addWidget(btn_2, 0, 1)
        grid.addWidget(btn_3, 0, 2)

        grid.addWidget(btn_4, 0, 3)
        grid.addWidget(btn_5, 0, 4)
        grid.addWidget(btn_6, 0, 5)
        
        grid.addWidget(btn_7, 1, 0)
        grid.addWidget(btn_8, 1, 1)
        grid.addWidget(btn_9, 1, 2)

        self.setLayout(grid)

def main():
    app = QApplication(sys.argv)
    win = mainWindow()
    win.show()
    sys.exit(app.exec_())

main()
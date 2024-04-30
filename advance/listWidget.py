from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QLabel
import sys

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700, 400)
        self.setWindowTitle("hbox Layout")
        self.setWindowIcon(QIcon("c:/Users/pc/Desktop/Programming/Python/PyQt5/images/cliquez-sur.png"))
        self.initUi()

    def initUi(self):
        vbox = QVBoxLayout()

        self.list = QListWidget()

        self.list.insertItem(0, "Python")
        self.list.insertItem(1, "PHP")
        self.list.insertItem(2, "JavaScript")
        self.list.insertItem(3, "C++")
        self.list.insertItem(4, "Kotlen")
        self.list.clicked.connect(self.click_item)

        self.label = QLabel("")
        self.setFont(QFont("Sanserif", 15))
        self.setStyleSheet("color: #1E3BF9")

        vbox.addWidget(self.list)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def click_item(self):
        item = self.list.currentItem()
        self.label.setText("You selected : " + str(item.text()))

def main():
    app = QApplication(sys.argv)
    win = mainWindow()
    win.show()
    sys.exit(app.exec_())

main()
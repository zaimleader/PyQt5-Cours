from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
import sys

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700, 400)
        self.setWindowTitle("Table Widget")
        self.setWindowIcon(QIcon("c:/Users/pc/Desktop/Programming/Python/PyQt5/images/cliquez-sur.png"))
        self.initUi()

    def initUi(self):
        vbox = QVBoxLayout()

        # create table
        table = QTableWidget() 

        # number of row & column 
        table.setRowCount(3)
        table.setColumnCount(3)

        # add column name
        table.setItem(0, 0, QTableWidgetItem("Fullname"))
        table.setItem(0, 1, QTableWidgetItem("Email"))
        table.setItem(0, 2, QTableWidgetItem("Phone number"))

        # add items
        table.setItem(1, 0, QTableWidgetItem("Mohamed"))
        table.setItem(1, 1, QTableWidgetItem("mohamed@gmail.com"))
        table.setItem(1, 2, QTableWidgetItem("09876544321"))
        
        table.setItem(2, 0, QTableWidgetItem("Zaim"))
        table.setItem(2, 1, QTableWidgetItem("zaim@gmail.com"))
        table.setItem(2, 2, QTableWidgetItem("1234567890"))

        vbox.addWidget(table)

        self.setLayout(vbox)

def main():
    app = QApplication(sys.argv)
    win = mainWindow()
    win.show()
    sys.exit(app.exec_())

main()
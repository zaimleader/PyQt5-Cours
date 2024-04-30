from PyQt5 import QtCore, QtGui ,QtWidgets

import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.resize(700, 400)
win.setWindowTitle("Function")

def confirm():
    msgBox = QtWidgets.QMessageBox.question(win, "Confirmation", "Do you want to exsit from App?")
    if msgBox == QtWidgets.QMessageBox.Yes:
        print("Exit...")
        app.exit()

btn = QtWidgets.QPushButton("Exit", win)
btn.move(300, 150)
btn.clicked.connect(confirm)

win.show()

app.exec_()
from PyQt5 import QtCore, QtGui ,QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.resize(700, 400)
win.setWindowTitle("inputDialog")

number = QtWidgets.QInputDialog.getInt(win, "Number", "Enter a number:", 5, 0, 100, 1)
name = QtWidgets.QInputDialog.getText(win, "Username", "Enter your name:") # QtWidgets.QLineEdit.NoEcho 

win.show()

app.exec_()
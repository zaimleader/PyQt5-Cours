from PyQt5 import QtCore, QtGui ,QtWidgets

import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.resize(700, 400)
win.setWindowTitle("MessageBox")

question = QtWidgets.QMessageBox.question(win, "Title of quetion", "Your question?")
warning = QtWidgets.QMessageBox.warning(win, "Title of warning", "Your warning!!!")
about = QtWidgets.QMessageBox.about(win, "Title of about", "Your about..................................")
error = QtWidgets.QErrorMessage(win)
error.showMessage("Please install PyQt5 to run this progrmme")

win.show()

app.exec_()
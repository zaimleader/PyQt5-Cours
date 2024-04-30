from PyQt5 import QtCore, QtGui ,QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.resize(700, 400)
win.setWindowTitle("Radio")

question = QtWidgets.QLabel("<b>What is your language favorite?</b>", win)
question.move(10, 10)

rd_1 = QtWidgets.QRadioButton("Python", win)
rd_1.move(30, 30)
rd_2 = QtWidgets.QRadioButton("JS", win)
rd_2.move(30, 50)
rd_3 = QtWidgets.QRadioButton("PHP", win)
rd_3.move(30, 70)

win.show()

app.exec_()
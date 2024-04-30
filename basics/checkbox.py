from PyQt5 import QtCore, QtGui ,QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.resize(700, 400)
win.setWindowTitle("Checkbox")

question = QtWidgets.QLabel("<b>What is your language favorite?</b>", win)
question.move(30, 10)

box_1 = QtWidgets.QCheckBox("Python", win)
box_1.move(50, 30)
box_2 = QtWidgets.QCheckBox("PHP", win)
box_2.move(50, 50)
box_3 = QtWidgets.QCheckBox("C++", win)
box_3.move(50, 70)
box_4 = QtWidgets.QCheckBox("JS", win)
box_4.move(50, 90)

win.show()

app.exec_()
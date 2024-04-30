from PyQt5 import QtCore, QtGui ,QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.resize(700, 400)
win.setWindowTitle("Colors")

def selectColor():
    color = QtWidgets.QColorDialog.getColor()

txt = QtWidgets.QLabel("<b>Choose your color by click on the button bellow:</b>", win)
txt.move(150, 100)

btnColor = QtWidgets.QPushButton("Select Color", win)
btnColor.move(250, 130)
btnColor.clicked.connect(selectColor)


win.show()

app.exec_()
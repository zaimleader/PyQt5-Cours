from PyQt5 import QtCore, QtGui ,QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.resize(700, 400)
win.setWindowTitle("Fonts")

def selectFont():
    font = QtWidgets.QFontDialog.getFont()

txt = QtWidgets.QLabel("<b>Choose your font by click on the button bellow:</b>", win)
txt.move(150, 100)

btnFont = QtWidgets.QPushButton("Select Font", win)
btnFont.move(250, 130)
btnFont.clicked.connect(selectFont)


win.show()

app.exec_()
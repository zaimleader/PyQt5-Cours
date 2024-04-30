from PyQt5 import QtCore, QtGui ,QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.setWindowTitle("Fields")

field = QtWidgets.QLineEdit(win)

wid = 400
hei = 45
field.resize(wid, hei)

posX = 30
posY = 50
field.move(posX, posY)

style = """ 
   border: 2px solid rgb(255, 195, 0);
   border-radius: 5px;
   font-size: 17px;
   font-weight: 400;
   font-family: Tahomal;
   padding: 10px;
"""
field.setStyleSheet(style)

win.show()

app.exec_()
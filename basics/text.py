from PyQt5 import QtCore, QtGui ,QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.setWindowTitle("Text")

my_text = "Welcome to learn PyQt5"
txt = QtWidgets.QLabel(my_text, win)

widTxt = 400
heiTxt = 60
txt.resize(widTxt, heiTxt)

posXTxt = 50
posYTxt = 150
txt.move(posXTxt, posYTxt)

styleTxt = """ 
   background-color: #C70039;
   color: white;
   border: 2px solid rgb(255, 195, 0);
   border-radius: 5px;
   font-size: 30px;
   font-weight: 300;
   font-family: Tahomal;
   padding: 12px;
"""
txt.setStyleSheet(styleTxt)

win.show()

app.exec_()
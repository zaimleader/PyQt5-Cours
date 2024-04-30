from PyQt5 import QtCore, QtGui ,QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.setWindowTitle("Button")

btn = QtWidgets.QPushButton("My Button name", win)

widBtn = 200
heiBtn = 60
btn.resize(widBtn, heiBtn)

posXBtn = 150
posYBtn = 100
btn.move(posXBtn, posYBtn)

styleBtn = """ 
   background-color: #E3FFB0;
   color: IndianRed;
   border: 2px solid rgb(144, 12, 63);
   border-radius: 10px;
   font-size: 18px;
   font-weight: bold;
   font-family: Tahomal;
   cursor: pointer;
"""
btn.setStyleSheet(styleBtn)

btn.setToolTip("Exit")

path_icon = "c:/Users/pc/Desktop/Programming/Python/PyQt5/images/cliquez-sur.png" 
icon = QtGui.QIcon(path_icon)
btn.setIcon(icon)

btn.clicked.connect(exit)

win.show()

app.exec_()
from PyQt5 import QtCore, QtGui ,QtWidgets

import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.resize(700, 400)
win.setWindowTitle("Image")

img = QtWidgets.QLabel(win)
pixImg = QtGui.QPixmap("c:/Users/pc/Desktop/Programming/Python/PyQt5/images/owl cute.jpg").scaled(300, 300)
img.setPixmap(pixImg)
img.move(200, 50)


win.show()

app.exec_()
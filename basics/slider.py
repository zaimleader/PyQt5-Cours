from PyQt5 import QtCore, QtGui ,QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.resize(700, 400)
win.setWindowTitle("Slider")

txt = QtWidgets.QLabel("<b>Voice Control</b>", win)
txt.move(10, 10)

sld_1 = QtWidgets.QSlider(win)
sld_1.move(15, 30)
lb_1 = QtWidgets.QLabel("Volume", win)
lb_1.move(10, 120)

sld_2 = QtWidgets.QSlider(win)
sld_2.move(55, 30)
lb_2 = QtWidgets.QLabel("Filter", win)
lb_2.move(50, 120)

sld_3 = QtWidgets.QSlider(win)
sld_3.move(95, 30)
lb_3 = QtWidgets.QLabel("Opacity", win)
lb_3.move(90, 120)

win.show()

app.exec_()
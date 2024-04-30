from PyQt5 import QtCore, QtGui ,QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.resize(700, 400)
win.setWindowTitle("Calendar")

txt = QtWidgets.QLabel("<b>Enter your age by click on the button bellow:</b>", win)
txt.move(10, 10)

calendar = QtWidgets.QCalendarWidget(win)
calendar.move(10, 30)



win.show()

app.exec_()
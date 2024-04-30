from PyQt5 import QtCore, QtGui ,QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.resize(700, 400)
win.setWindowTitle("Progressbar")

txt = QtWidgets.QLabel("<b>Progress bar</b>", win)
txt.move(300, 20)

pbar = QtWidgets.QProgressBar(win)
pbar.move(100, 40)
pbar.resize(500, 20)
pbar.setValue(50)

win.show()

app.exec_()
from PyQt5 import QtCore, QtGui ,QtWidgets
from PyQt5.QtGui import QIcon
import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QMainWindow()
win.resize(700, 400)
win.setWindowTitle("MenuBar")

def ex():
    # win.destroy() # exit from window
    app.exit() # exit from app

menubar = win.menuBar() # Create menu bar

file = menubar.addMenu("file")
edit = menubar.addMenu("edit")
selection = menubar.addMenu("selection")
view = menubar.addMenu("view")

new = QtWidgets.QAction(QIcon("./images/new.png") ,"new", win)
open = QtWidgets.QAction(QIcon("./images/open.png") ,"open", win)
save = QtWidgets.QAction(QIcon("./images/save.png") ,"save", win)
exit = QtWidgets.QAction(QIcon("./images/exit.png") ,"exit", win)

new.setShortcut("Ctrl+N")
open.setShortcut("Ctrl+O")
save.setShortcut("Ctrl+S")
exit.setShortcut("Ctrl+Z")

exit.triggered.connect(ex)

file.addAction(new)
file.addAction(open)
file.addAction(save)
file.addAction(exit)

win.show()

app.exec_()
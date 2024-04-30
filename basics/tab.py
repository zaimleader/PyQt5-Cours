from PyQt5 import QtCore, QtGui ,QtWidgets
from PyQt5.QtGui import *
import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.resize(700, 400)
win.setWindowTitle("Tabs")

# 1- Create tab
mainTab = QtWidgets.QTabWidget(win)
mainTab.resize(700, 100)
mainTab.setStyleSheet("background-color: #f2f2f2")

# 2- Create widgets
tab_1 = QtWidgets.QWidget()
tab_2 = QtWidgets.QWidget()
tab_3 = QtWidgets.QWidget()

# 3- add widgets to main tab
mainTab.addTab(tab_1, "Title Tab 1")
mainTab.addTab(tab_2, "Title Tab 2")
mainTab.addTab(tab_3, "Title Tab 3")

# 4- fill widgets
title_1 = QtWidgets.QLabel("Content Tab 1", tab_1)
title_2 = QtWidgets.QLabel("Content Tab 2", tab_2)
title_3 = QtWidgets.QLabel("Content Tab 3", tab_3)

# 5-styling
title_1.setStyleSheet("color: #006eac; font-size: 18px;")
title_2.setStyleSheet("color: #43cb51; font-size: 18px;")
title_3.setStyleSheet("color: #e9b711; font-size: 18px;")

win.show()

app.exec_()
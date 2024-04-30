from PyQt5 import QtCore, QtGui ,QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

win = QtWidgets.QWidget()
win.resize(700, 400)
win.setWindowTitle("Combobox")

select = QtWidgets.QLabel("<b>Select your country: </b>", win)
select.move(30, 10)

combobox = QtWidgets.QComboBox(win)
combobox.addItem("")
combobox.addItem("Morocco")
combobox.addItem("Algerian")
combobox.addItem("Egypt")
combobox.addItem("Tuness")
combobox.move(150, 8)

win.show()

app.exec_()
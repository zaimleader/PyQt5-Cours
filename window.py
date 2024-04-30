from PyQt5 import QtCore, QtGui ,QtWidgets
import sys

# create app from QApplication Module
app = QtWidgets.QApplication(sys.argv)

# Create a window
win = QtWidgets.QWidget()

width = 900
height = 500

# win.resize(width, height) # control size of window (width & height)

posX = 250
posY = 100

# win.move(posX, posY) # move = control position of window (x & y)

win.setGeometry(posX, posY, width, height) # setGeometry = move + resize

win.setWindowTitle("Window App") # set title of your window App

# setStyleSheet: change color of window
# win.setStyleSheet("background-color: DarkSalmon")        # 1- with name of color
# win.setStyleSheet("background-color: rgb(144, 12, 63)")  # 2- with RGB of color (R: Red, G: Green, B: Blue)
# win.setStyleSheet("background-color: hsl(81, 33%, 81%)") # 3- with HSL of color (H: Hue, S: Saturation, L: Lightness)
win.setStyleSheet("background-color: #FF5733")             # 4- with hex of color (hex: #RRGGBB)

path_icon = "c:/Users/pc/Desktop/Programming/Python/PyQt5/images/owl cute.jpg" 
icon = QtGui.QIcon(path_icon)
win.setWindowIcon(icon) # Change icon fo window app

# show it
win.show()

# Exexute app
app.exec_()

# When app close display on "done"
print("done")
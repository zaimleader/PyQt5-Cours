from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize
import sys

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.path = "c:/Users/pc/Desktop/Programming/Python/PyQt5/images/"
        self.resize(700, 400)
        self.setWindowTitle("Grid Layout")
        self.setWindowIcon(QIcon(self.path + "cliquez-sur.png"))
        self.initUi()
        

    def initUi(self):

        vbox = QVBoxLayout()
        
        self.groupBox = QGroupBox("What's your favorite sport?")
        
        hbox = QHBoxLayout()

        self.rad1 = QRadioButton("Football")
        self.rad1.setChecked(True)
        self.rad1.setIcon(QIcon(self.path + "Sports/football.png"))
        self.rad1.setIconSize(QSize(40, 40))
        self.rad1.setFont(QFont("Sanserif", 14))
        self.rad1.toggled.connect(self.on_selected)
        
        self.rad2 = QRadioButton("Basketball")
        self.rad2.setIcon(QIcon(self.path + "Sports/basketball"))
        self.rad2.setIconSize(QSize(40, 40))
        self.rad2.setFont(QFont("Sanserif", 14))
        self.rad2.toggled.connect(self.on_selected)
        
        self.rad3 = QRadioButton("Volley ball")
        self.rad3.setIcon(QIcon(self.path + "Sports/volleyball.png"))
        self.rad3.setIconSize(QSize(40, 40))
        self.rad3.setFont(QFont("Sanserif", 14))
        self.rad3.toggled.connect(self.on_selected)
        
        self.rad4 = QRadioButton("Tennis")
        self.rad4.setIcon(QIcon(self.path + "Sports/tennis.png"))
        self.rad4.setIconSize(QSize(40, 40))
        self.rad4.setFont(QFont("Sanserif", 14))
        self.rad4.toggled.connect(self.on_selected)

        hbox.addWidget(self.rad1)
        hbox.addWidget(self.rad2)
        hbox.addWidget(self.rad3)
        hbox.addWidget(self.rad4)

        self.groupBox.setLayout(hbox)

        vbox.addWidget(self.groupBox)

        self.label = QLabel("")
        self.setFont(QFont("Sanserif", 13))

        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def on_selected(self):
        radio_btn = self.sender()

        if radio_btn.isChecked():
            self.label.setText("You have selected : " + radio_btn.text())

def main():
    app = QApplication(sys.argv)
    win = mainWindow()
    win.show()
    sys.exit(app.exec_())

main()
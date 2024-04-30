from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QLabel
import sys

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700, 400)
        self.setWindowTitle("Vbox Layout")
        self.setWindowIcon(QIcon("c:/Users/pc/Desktop/Programming/Python/PyQt5/images/cliquez-sur.png"))
        self.initUi()

    def initUi(self):
        self.label = QLabel("xxxxxxxx", self)
        self.label.setFont(QFont("Sanserif", 14))
        self.label.move(10, 10)
        self.label.resize(700, 40)

        self.btn = QPushButton("Open File", self)
        self.btn.move(10, 50)
        self.btn.clicked.connect(self.open_file)


    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Excel Files 'xlsx' (*.xlsx);;Excel Files 'csv' (*.csv)")
        
        if file_name: 
            file = file_name.split("/")[-1]

            print(file)

            self.label.setText(file_name)


def main():
    app = QApplication(sys.argv)
    win = mainWindow()
    win.show()
    sys.exit(app.exec_())

main()
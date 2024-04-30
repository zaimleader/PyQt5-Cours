from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton
import sys

class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700, 400)
        self.setWindowTitle("Vbox Layout")
        self.setWindowIcon(QIcon("c:/Users/pc/Desktop/Programming/Python/PyQt5/images/cliquez-sur.png"))
        self.initUi()

    def initUi(self):
        vbox = QVBoxLayout()
        self.form = QFormLayout()

        self.label = QLabel("This is Cool Label Row")
        self.setFont(QFont("Sanserif", 16))

        self.first_name = QLineEdit(self)
        self.last_name = QLineEdit(self)

        self.submit = QPushButton("Submit")
        self.submit.clicked.connect(self.submit_form)

        self.form.addRow(self.label)
        self.form.addRow("First name: ", self.first_name)
        self.form.addRow("Last name: ", self.last_name)
        self.form.addRow(self.submit)

        self.setLayout(self.form)

    def submit_form(self):
        self.label.setText(f"Your Fullname is: {self.first_name.text()} {self.last_name.text()}")

def main():
    app = QApplication(sys.argv)
    win = mainWindow()
    win.show()
    sys.exit(app.exec_())

main()
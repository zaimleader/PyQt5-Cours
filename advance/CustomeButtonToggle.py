import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QPropertyAnimation, QRect, Qt
from PyQt5.QtGui import QPainter


class CustomButtonToggle(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(70, 40)
        self.setCheckable(True)
        self.setStyleSheet("background-color: red;")
        self.rect = QRect(0, 0, 30, 30)
        self.rect.moveTo(0, 0)
        self.toggled.connect(self.handleToggle)

    def handleToggle(self, checked):
        if checked:
            self.setStyleSheet("background-color: green;")
            self.rect.moveTo(40, 0)
        else:
            self.setStyleSheet("background-color: red;")
            self.rect.moveTo(0, 0)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(Qt.white)
        painter.drawRect(self.rect)

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        qbtn = CustomButtonToggle(self)
        qbtn.setGeometry(50, 50, 70, 40)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
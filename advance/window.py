from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QWidget, QPushButton, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class WindowBase(QDialog):
    def __init__(self, label=None):
        super().__init__()

        # Set up the window layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create a label if one was provided
        if label is not None:
            self.label = label
            self.label.setScaledContents(True)
            layout.addWidget(self.label)

        # Set window properties
        self.setWindowTitle('WindowBase')
        self.setWindowModality(Qt.ApplicationModal)
        self.setGeometry(300, 300, 400, 300)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a button
        self.button = QPushButton('Open Window')
        self.button.clicked.connect(self.open_window)

        # Create a label with an image
        self.label = QLabel()
        pixmap = QPixmap('../images/owl cute.jpg')
        self.label.setPixmap(pixmap)

        # Create a layout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def open_window(self):
        # Create a WindowBase with the label
        window = WindowBase(self.label)
        window.exec_()


app = QApplication([])

# Create a label with an image
# label = QLabel("sds dff ezf zf ezfze")
# pixmap = QPixmap('../images/owl cute.jpg')
# label.setPixmap(pixmap)

# Create a WindowBase with the label
# window = WindowBase(label)
# window.show()

wid = MyWidget()
wid.show()

app.exec_()
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox

import sys

class CustomComboBox(QComboBox):
    def __init__(self,items=None, parent=None):
        super(CustomComboBox, self).__init__(parent)

        self.setStyleSheet("""
            QComboBox {
                border: 1px solid MediumVioletRed;
                border-radius: 3px;
                padding: 1px 18px 1px 3px;
                width: 200px;
                height: 40px;
                color: red;
            }
            QComboBox:editable {
                background: blue;
            }
            QComboBox:!editable, QComboBox::drop-down:editable {
                 background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                            stop: 0 #fff, stop: 0.4 #fff,
                                            stop: 0.5 #fff, stop: 1.0 #fff);
            }
            QComboBox:on {
                 padding: 10px 18px 10px 30px;
            }
            QComboBox QAbstractItemView {
                           color:blue;
                border: 2px solid red;
                selection-background-color: orange;
                selection-color: white;
                background-color: white;
            }
        """)

        self._items = items or []

        self._current_index = 0

        if len(self._items) > 0:
            self.set_items()

        # self.current_index()

    @property
    def current_index(self):
        return self._current_index

    @current_index.setter
    def current_index(self, value):
        self._current_index = value
        self.setCurrentIndex(value)

    def clear_selection(self):
        self.setCurrentIndex(-1)

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value
        self.clear()
        for item in value:
            self.addItem(item)

    def set_items(self):
        if self._items:
            self.clear()
            for item in self._items:
                self.addItem(item)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        items = ["Item 1", "Item 2", "Item 3"]
        combo_box = CustomComboBox(items, self)
        # combo_box.set_items()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
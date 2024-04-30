from PyQt5.QtWidgets import QTableWidget, QAbstractItemView,QApplication
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

class CustomTableWidget(QTableWidget):
    def __init__(self, num_rows, num_cols, parent=None):
        super().__init__(num_rows, num_cols, parent)

        # Set default properties
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setAlternatingRowColors(True)


        self.horizontalHeader().setStyleSheet('''
            QHeaderView::section {
                background-color: #F1AE3B;
                color: #fff;
                padding: 5px;
                font-size: 17px;
                font-weight: bold;
            }
        ''')

        self.setStyleSheet('''
            QTableWidget::item:selected {
                background-color: #ff0000;
            }
        ''')

         # set row height
        self.verticalHeader().setDefaultSectionSize(30)

    def set_row_colors(self, indexes, colors):
        """Set the background color of the rows at the given indexes.

        Args:
            indexes (list): List of row indexes to set the color for.
            colors (list): List of QColor objects representing the colors to set.
        """
        for i, index in enumerate(indexes):
            if 0 <= index < self.rowCount():
                item = self.item(index, 0)
                if item is not None:
                    item.setBackground(QtGui.QColorDialog.getColor(item.background(), self, "Choose color"))

    def set_column_widths(self, widths):
        """Set the width of each column.

        Args:
            widths (list): List of widths in pixels for each column.
        """
        for i, width in enumerate(widths):
            self.setColumnWidth(i, width)

app = QApplication([])

table = CustomTableWidget(10, 5)
# table.set_row_colors([1, 3, 6], [Qt.yellow, Qt.green, Qt.red])
# table.set_column_widths([100, 150, 200, 100, 150])
table.resize(800, 400)
table.show()

app.exec_()
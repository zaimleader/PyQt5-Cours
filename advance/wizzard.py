from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QMessageBox, QVBoxLayout, QLabel, QWizard, QDialog, QWizardPage
from PyQt5.QtCore import pyqtSignal, Qt

class Wizzard(QWizard):
    def __init__(self):
        super().__init__()

        # Initialize the wizzard's UI
        self.init_ui()

        # Connect the finished signal to a slot
        self.finished.connect(self.wizzard_closed)

    def init_ui(self):
        # Create a layout for the wizzard
        layout = QVBoxLayout()

        # Create a label for the wizzard's body
        label = QLabel("This is the wizzard's content.")

        # Add the label to the layout
        layout.addWidget(label)

        # Set the layout for the wizzard
        self.setLayout(layout)

    def wizzard_closed(self, result):
        # Ignore the finished signal when the Wizzard window is closed with the X button
        if result == QDialog.Rejected:
            return
        print("Wizzard window was closed")
        # The Wizzard window was closed with the "Next" or "Prev" button
        # ...

class Page1(QWizardPage):
    def __init__(self, wizard):
        super().__init__()

        self.wizard = wizard
        # self.wizard.button(QWizard.NextButton).clicked.connect(self.wizard.next)

        # Set the page title and icon
        self.setTitle("Page 1")
        s = QWizardPage()
        # Add a label to the page
        label = QLabel("Welcome to Page 1!")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

class Page2(QWizardPage):
    def __init__(self, wizard):
        super().__init__()

        self.wizard = wizard
        self.wizard.button(QWizard.NextButton).clicked.connect(self.change_state)

        # Set the page title and icon
        self.setTitle("Page 2")

        # Add a label to the page
        label = QLabel("Welcome to Page 2!")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

    def change_state(self):
        self.wizard.state_page = False

class Page3(QWizardPage):
    def __init__(self, wizard):
        super().__init__()

        self.wizard = wizard
        # self.wizard.button(QWizard.NextButton).clicked.connect(self.wizard.next)

        # Set the page title and icon
        self.setTitle("Page 3")

        # Add a label to the page
        label = QLabel("Welcome to Page 3!")
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

class MyWizard(QWizard):
    def __init__(self):
        super().__init__()

        # Create the three pages
        self.page1 = Page1(wizard=self)
        self.page2 = Page2(wizard=self)
        self.page3 = Page3(wizard=self)

        # Add the pages to the wizard
        self.addPage(self.page1)
        self.addPage(self.page2)
        self.addPage(self.page3)

        # Set the IDs of the pages
        # self.setPage(1, self.page1)
        # self.setPage(2, self.page2)
        # self.setPage(3, self.page3)

        # Add "Next" and "Prev" buttons to the wizard footer

        # Add "Next" and "Prev" buttons to the wizard footer
        # self.button(QWizard.NextButton).setText("Next")
        # self.button(QWizard.BackButton).setText("Prev")

        # self.button(QWizard.FinishButton).setText("save")
        layout = [QWizard.Stretch, QWizard.BackButton, QWizard.NextButton, QWizard.FinishButton]
        self.setButtonLayout(layout)

        # self.button(QWizard.BackButton).setStyleSheet("background: blue; color: white; border: 1px solid orange; border-radius: 40px;")
        # self.button(QWizard.NextButton).setStyleSheet("background: red; color: white;")
        self.button(QWizard.FinishButton).clicked.connect(self.close_wizard)

        self.setWindowTitle("WindowTitle")

        # self.setUpdatesEnabled(QWizard.NextButton, False)
        
        # Disconnect the default "Cancel" button handler
        # self.button(QWizard.CancelButton).disconnect()

        # Move the "Prev" button next to the "Next" button
        # prev_button = self.button(QWizard.BackButton)
        # prev_button.setGeometry(prev_button.x() + prev_button.width() + 10, prev_button.y(), prev_button.width(), prev_button.height())

        # Change the label of the "Prev" button to "Prev"
        # prev_button.setText("Prev")

        # Connect the "Cancel" button handler to a custom function
        # self.button(QWizard.CancelButton).clicked.connect(self.close_wizard)

        # Set the wizard style sheet
        self.setStyleSheet("""
            QWizard {
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 10px;
            }

            QWizard::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                left: 10px;
                top: -10px;
                font-size: 18px;
                font-weight: bold;
            }

            QWizardPage {
                background-color: white;
                border: none;
                padding: 20px;
            }

            QLabel {
                font-size: 16px;
            }

            QLineEdit {
                border: 1px solid #ccc;
                border-radius: 3px;
                padding: 5px;
                font-size: 14px;
            }

            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 3px;
                padding: 10px;
                font-size: 14px;
            }

            QPushButton:hover {
                background-color: #3e8e41;
            }

            QPushButton:pressed {
                background-color: #2b662a;
            }

            QWizard::button {
                border: none;
                border-radius: 3px;
                padding: 10px;
                font-size: 14px;
            }

            QWizard::button:hover {
                background-color: #ddd;
            }

            QWizard::button:pressed {
                background-color: #ccc;
            }

            QWizard::button:checked {
                background-color: #4CAF50;
            }

            QWizard::button:checked:hover {
                background-color: #3e8e41;
            }

            QWizard::button:checked:pressed {
                background-color: #2b662a;
            }
        """)

        self.state_page = None

    def page_is_valid(self):
        if self.state_page != None:
            # check the state of the page here and return True if it's valid, False otherwise
            print("------- pass ------")
        # pass

    def show_alert(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def nextId(self):
        self.page_is_valid()

        if (not self.state_page) and (self.state_page != None) :
            # show alert
            self.show_alert("Error", "Please fix the errors on this page before proceeding.")
            return -1  # return -1 to stay on the same page
        else:
            return super().nextId()
        
    def next_d_re(self):
        current_page_index = self.currentId()
        # if current_page_index == 0:  # replace 0 with the index of your first page
        if not self.page_is_valid():  # replace page_is_valid() with your own method to check the state of the page
            self.show_alert()  # replace show_alert() with your own method to show an alert
            return current_page_index  # stay on the current page
        return super().nextId()  # go to the next page

    def close_wizard(self):
        # Close the wizard when the "Cancel" button is clicked
        # self.close()
        print("xxxxxxxxxxxxxxxxxxxxxxx")

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the main widget's UI
        self.init_ui()

    def init_ui(self):
        # Create a layout for the main widget
        layout = QVBoxLayout()

        # Create a button for the main widget
        button = QPushButton("Open Wizzard")

        # Connect the button's clicked signal to the open_wizzard method
        button.clicked.connect(self.open_wizzard)

        # Add the button to the layout
        layout.addWidget(button)

        # Set the layout for the main widget
        self.setLayout(layout)

    def open_wizzard(self):
        # Create a new instance of the Wizzard window
        wizzard = MyWizard()

        # wizzard.setButtonEnabled(QWizard.NextButton, False)

        # Connect the finished signal of the Wizzard window to a slot
        # wizzard.finished.connect(self.wizzard_closed)

        # Show the Wizzard window and start its event loop
        wizzard.exec_()

    def wizzard_closed(self):
        # This method will be called when the Wizzard window is closed
        print("Wizzard window was closed")


# Create a new instance of the QApplication class
app = QApplication([])

# Create a new instance of the MainWidget class
main_widget = MainWidget()

main_widget.resize(400, 300)

# Show the main widget
main_widget.show()

# Run the application's event loop
app.exec_()
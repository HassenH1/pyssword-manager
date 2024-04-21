import sys
from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QGridLayout,
    QTableWidget,
    QHeaderView,
    QTableWidgetItem,
    QWidget,
    QMainWindow,
    QStyle,
    QVBoxLayout,
    QLabel,
    QHBoxLayout,
    QLineEdit,
    QApplication,
)
from PyQt6.QtCore import QSize, Qt, pyqtSlot
from db import Database
import random
import string

# TODO do not delete
# Activate venv - .\virtualenv\Scripts\Activate.ps1
# Deactivate venv - deactivate


class AddWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self, data: list):
        super().__init__()
        # self.db = Database()
        self.mock_data = data
        self.setWindowTitle("Add new password")

        layout = QVBoxLayout()
        self.setFixedSize(QSize(400, 250))
        self.setLayout(layout)

        self.siteName = QLabel("Site")
        self.siteName.setContentsMargins(0, 20, 0, 0)
        layout.addWidget(self.siteName)

        self.siteEdit = QLineEdit()
        layout.addWidget(self.siteEdit)

        self.username = QLabel("Username")
        self.username.setContentsMargins(0, 10, 0, 0)
        layout.addWidget(self.username)

        self.usernameEdit = QLineEdit()
        layout.addWidget(self.usernameEdit)

        self.password = QLabel("Password")
        self.password.setContentsMargins(0, 10, 0, 0)
        layout.addWidget(self.password)

        layout2 = QHBoxLayout()
        layout.addLayout(layout2)

        self.passwordEdit = QLineEdit()
        layout2.addWidget(self.passwordEdit)

        generateButton = QPushButton("Generate")
        generateButton.clicked.connect(self.generatePassword)
        layout2.addWidget(generateButton)

        layout3 = QHBoxLayout()
        layout.addLayout(layout3)

        saveButton = QPushButton("Save")
        saveButton.clicked.connect(self.saveNewPassword)
        cancelButton = QPushButton("Cancel")
        cancelButton.setStyleSheet("color: red;")
        cancelButton.clicked.connect(self.closeWindow)

        layout3.setContentsMargins(0, 10, 0, 0)
        layout3.addWidget(saveButton)
        layout3.addWidget(cancelButton)
        layout3.setAlignment(Qt.AlignmentFlag.AlignCenter)

    @pyqtSlot()
    def saveNewPassword(self):
        # TODO add to array here
        tuple = (
            self.siteEdit.text(),
            self.usernameEdit.text(),
            self.passwordEdit.text(),
            "",
            "",
            "",
        )
        self.mock_data.append(tuple)
        print(self.mock_data, "<-----what is this?")
        self.close()

    @pyqtSlot()
    def generatePassword(self):
        # TODO add cryptography
        # get random string of letters and digits
        source = string.ascii_letters + string.digits
        result_str = "".join((random.choice(source) for i in range(15)))
        self.passwordEdit.setText(result_str)

    @pyqtSlot()
    def closeWindow(self):
        self.close()


class MainWindow(QMainWindow):
    header_names = ["Site", "Username", "Password", "Created", "Last modified", ""]
    mock_data = [
        {
            "site": "Google",
            "username": "Hasan",
            "password": "password1",
            "created_date": "04-07-2024",
            "modified_date": "",
            "delete_icon": "",
        },
        {
            "site": "Apple",
            "username": "Hassen",
            "password": "password122",
            "created_date": "04-01-2000",
            "modified_date": "",
            "delete_icon": "",
        },
        {
            "site": "Windows",
            "username": "Hasen",
            "password": "password133",
            "create_date": "04-05-2024",
            "modified_date": "",
            "delete_icon": "",
        },
        {
            "site": "loooooooooooooooong strinnnnnnnnnnnnnnnnng",
            "username": "Haseen",
            "password": "password13355",
            "create_date": "04-05-2024",
            "modified_date": "04-07-2024",
            "delete_icon": "",
        },
    ]

    def __init__(self):
        super().__init__()
        self.w = None  # No external window yet.

        # Create the parent Widget
        self.setWindowTitle("My password manager")
        self.setFixedSize(QSize(1000, 500))

        # Create the buttons
        addButton = QPushButton("Add +")
        addButton.clicked.connect(self.addButtonWasClicked)

        # Create the table
        tableWidget = QTableWidget()
        tableWidget.setColumnCount(self.header_names.__len__())
        tableWidget.setRowCount(self.mock_data.__len__())
        tableWidget.setHorizontalHeaderLabels(self.header_names)
        tableWidget.verticalHeader().hide()
        tableWidget.cellDoubleClicked.connect(self.doubleClickedCell)

        style = "::section { background-color: lightblue; }"
        tableWidget.horizontalHeader().setStyleSheet(style)
        tableWidget.horizontalHeader().sectionPressed.disconnect()
        tableWidget.horizontalHeader().setSectionsClickable(False)
        tableWidget.setAlternatingRowColors(True)

        for row, (list) in enumerate(self.mock_data):
            for col, (key, value) in enumerate(list.items()):
                item_name = QTableWidgetItem(value)
                item_name.setFlags(Qt.ItemFlag.ItemIsEnabled)

                if key == "delete_icon":
                    pixmapi = QStyle.StandardPixmap.SP_MessageBoxCritical
                    icon = self.style().standardIcon(pixmapi)
                    item_name.setIcon(icon)

                tableWidget.setItem(row, col, item_name)

        tableHeader = tableWidget.horizontalHeader()
        tableHeader.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        tableHeader.setSectionResizeMode(
            len(self.mock_data[0]) - 1, QHeaderView.ResizeMode.ResizeToContents
        )

        # Create the QGrid Layout Manager
        mainLayout = QGridLayout()

        # Add button Widgets to the MainLayout QGridLayout
        # addWidget([object], [row number], [column number], [columnSpan], [rowSpan], Qt.Alignment)
        mainLayout.addWidget(addButton, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        # Add table Widgets to the MainLayout QGridLayout
        mainLayout.addWidget(tableWidget, 0, 0, 1, 1)

        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

    @pyqtSlot()
    def addButtonWasClicked(self):
        if self.w is None:
            self.w = AddWindow(self.mock_data)
            self.w.show()
        else:
            self.w.close()
            self.w = None  # Discard reference, close window.

    @pyqtSlot(int, int, result=int)
    def doubleClickedCell(self, row, col):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.mock_data[row][col])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

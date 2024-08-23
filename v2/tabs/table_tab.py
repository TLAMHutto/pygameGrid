from PyQt5 import QtWidgets

class TableTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TableTab, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("TableTab")
        self.setGeometry(0, 0, 300, 200)  # Adjust size and position as needed

        # Create a QTableWidget
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(10, 10, 280, 180)  # Adjust size and position as needed

        # Example setup for the table widget
        self.tableWidget.setColumnCount(3)  # Example column count
        self.tableWidget.setRowCount(3)     # Example row count

        # Set headers
        self.tableWidget.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3"])
        self.tableWidget.setVerticalHeaderLabels(["Row 1", "Row 2", "Row 3"])

        # Example data
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Data 1"))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("Data 2"))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem("Data 3"))

        # Additional setup can be done here

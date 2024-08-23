from PyQt5 import QtWidgets

class ListTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ListTab, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("ListTab")
        self.setGeometry(0, 0, 300, 200)  # Adjust size and position as needed

        # Create a list widget
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setGeometry(10, 10, 280, 180)  # Adjust size and position as needed

        # Example items
        self.listWidget.addItem("Item 1")
        self.listWidget.addItem("Item 2")
        self.listWidget.addItem("Item 3")

        # Additional setup can be done here

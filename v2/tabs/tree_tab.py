from PyQt5 import QtWidgets

class TreeTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(TreeTab, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("TreeTab")
        self.setGeometry(0, 0, 300, 200)  # Adjust size and position as needed

        # Create a QTreeWidget
        self.treeWidget = QtWidgets.QTreeWidget(self)
        self.treeWidget.setGeometry(10, 10, 280, 180)  # Adjust size and position as needed

        # Set column count
        self.treeWidget.setColumnCount(1)
        self.treeWidget.setHeaderLabels(["Tree View"])

        # Example items
        root = QtWidgets.QTreeWidgetItem(self.treeWidget, ["Root"])
        child1 = QtWidgets.QTreeWidgetItem(root, ["Child 1"])
        child2 = QtWidgets.QTreeWidgetItem(root, ["Child 2"])
        grandchild = QtWidgets.QTreeWidgetItem(child1, ["Grandchild"])

        # Expand all items
        self.treeWidget.expandAll()

        # Additional setup can be done here

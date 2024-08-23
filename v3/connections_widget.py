# connections_widget.py

from PyQt5 import QtCore, QtWidgets

class ConnectionsWidget(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(550, 360, 231, 231))
        self.setObjectName("tabWidget")

        # Tab 1: List Widget
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 211, 192))
        self.listWidget.setObjectName("listWidget")
        self.addTab(self.tab, "List")

        # Tab 2: Tree Widget
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab_3)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 221, 192))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "Header")
        self.addTab(self.tab_3, "Tree")

        # Tab 3: Table Widget
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 221, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.addTab(self.tab_4, "Table")

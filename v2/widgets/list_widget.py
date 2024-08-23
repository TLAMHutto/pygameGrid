from PyQt5 import QtWidgets, QtCore

class ListWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setObjectName("ListWidget")
        
        # Create and configure the QListView
        self.listView = QtWidgets.QListView(self)
        self.listView.setGeometry(QtCore.QRect(560, 20, 361, 111))
        self.listView.setObjectName("listView")

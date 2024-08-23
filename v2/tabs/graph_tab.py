from PyQt5 import QtWidgets

class GraphTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(GraphTab, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("graph")
        # Add any additional logic or widgets for the Graph tab here.

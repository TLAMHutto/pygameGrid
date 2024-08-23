from PyQt5 import QtWidgets

class SimTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SimTab, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("sim")
        # Add any additional logic or widgets for the Sim tab here.

from PyQt5 import QtWidgets, QtCore

class SimTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setObjectName("Sim")
        
        # Create and configure the Sim tab
        self.Sim = QtWidgets.QWidget(self)
        self.Sim.setObjectName("Sim")
        
        # Example widget initialization
        # Add any widgets you need to the Sim tab here

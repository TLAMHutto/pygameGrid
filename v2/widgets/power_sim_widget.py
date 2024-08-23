from PyQt5 import QtWidgets, QtCore

class PowerSimWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setObjectName("PowerSimWidget")
        self.setGeometry(QtCore.QRect(0, 0, 300, 150))  # Adjust size and position as needed
        
        self.PowerSim = QtWidgets.QTabWidget(self)
        self.PowerSim.setGeometry(QtCore.QRect(10, 50, 251, 80))
        self.PowerSim.setObjectName("PowerSim")
        
        # Additional setup for the PowerSim tab widget can go here

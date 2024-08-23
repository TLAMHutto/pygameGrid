from PyQt5 import QtWidgets, QtCore

class PowerTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setObjectName("power")
        
        # Create and configure the AddPower button
        self.AddPower = QtWidgets.QPushButton(self)
        self.AddPower.setGeometry(QtCore.QRect(0, 0, 75, 23))
        self.AddPower.setObjectName("AddPower")
        
        # Create and configure the lcdNumber
        self.lcdNumber = QtWidgets.QLCDNumber(self)
        self.lcdNumber.setGeometry(QtCore.QRect(110, 0, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        
        # Create and configure the lcdNumber_2
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self)
        self.lcdNumber_2.setGeometry(QtCore.QRect(110, 30, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        
        # Create and configure the Voltage label
        self.Voltage = QtWidgets.QLabel(self)
        self.Voltage.setGeometry(QtCore.QRect(180, 10, 47, 13))
        self.Voltage.setObjectName("Voltage")
        
        # Create and configure the Current label
        self.Current = QtWidgets.QLabel(self)
        self.Current.setGeometry(QtCore.QRect(180, 40, 47, 13))
        self.Current.setObjectName("Current")

# power_sim_widget.py

from PyQt5 import QtCore, QtWidgets
from power_select import PowerSelectDialog


class PowerSimWidget(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(QtCore.QRect(10, 270, 251, 80))
        self.setObjectName("PowerSim")

        # First tab
        self.Power_tab = QtWidgets.QWidget()
        self.Power_tab.setObjectName("Power_tab")

        self.pushButton = QtWidgets.QPushButton(self.Power_tab)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Add Power")
        self.pushButton.clicked.connect(self.open_power_select_dialog)

        self.lcdNumber = QtWidgets.QLCDNumber(self.Power_tab)
        self.lcdNumber.setGeometry(QtCore.QRect(110, 0, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber_voltage")

        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.Power_tab)
        self.lcdNumber_2.setGeometry(QtCore.QRect(110, 30, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_current")

        self.label = QtWidgets.QLabel(self.Power_tab)
        self.label.setGeometry(QtCore.QRect(180, 10, 47, 13))
        self.label.setObjectName("label")
        self.label.setText('V')
        self.label_2 = QtWidgets.QLabel(self.Power_tab)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("I")
        self.addTab(self.Power_tab, "Power Tab")

        # Second tab
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.addTab(self.tab_2, "Tab 2")


    def open_power_select_dialog(self):
        dialog = PowerSelectDialog(self)
        result = dialog.exec_()

        if result == QtWidgets.QDialog.Accepted:
            voltage, current = dialog.get_values()
            if voltage is not None:
                self.lcdNumber.display(voltage)
            if current is not None:
                self.lcdNumber_2.display(current)
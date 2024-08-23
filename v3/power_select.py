# power_select.py

from PyQt5 import QtCore, QtWidgets

class PowerSelectDialog(QtWidgets.QDialog):
    voltageChanged = QtCore.pyqtSignal(float)
    currentChanged = QtCore.pyqtSignal(float)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Power Select")

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.setGeometry(100, 100, 250, 300)  # Set the size of the dialog

        # TextEdits
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 60, 101, 21))
        self.textEdit.setObjectName("textEdit_voltage")
        self.textEdit.textChanged.connect(self.update_voltage)

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 120, 101, 21))
        self.textEdit_2.setObjectName("textEdit_current")
        self.textEdit_2.textChanged.connect(self.update_current)

        # Labels
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 47, 13))
        self.label.setObjectName("label")
        self.label.setText("Voltage")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("V")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("Current")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 120, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("I")

        # Push Buttons
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 170, 75, 23))
        self.pushButton.setObjectName("pushButton_okay")
        self.pushButton.setText("Okay")
        self.pushButton.clicked.connect(self.accept)  # Use QDialog's accept method

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 210, 75, 23))
        self.pushButton_2.setObjectName("pushButton_cancel")
        self.pushButton_2.setText("Cancel")
        self.pushButton_2.clicked.connect(self.reject)
    def update_voltage(self):
        try:
            voltage = float(self.textEdit.toPlainText())
            self.voltageChanged.emit(voltage)
        except ValueError:
            pass

    def update_current(self):
        try:
            current = float(self.textEdit_2.toPlainText())
            self.currentChanged.emit(current)
        except ValueError:
            pass

    def get_values(self):
        try:
            voltage = float(self.textEdit.toPlainText())
        except ValueError:
            voltage = None
        try:
            current = float(self.textEdit_2.toPlainText())
        except ValueError:
            current = None
        return voltage, current

        # Connect slots by name
        QtCore.QMetaObject.connectSlotsByName(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = PowerSelectDialog()
    dialog.exec_()

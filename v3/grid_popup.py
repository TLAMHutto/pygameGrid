from PyQt5 import QtCore, QtGui, QtWidgets

class GridPopup(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Form")
        self.resize(242, 313)

        # ComboBox
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(20, 80, 201, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        # Radio Buttons
        self.radioButton = QtWidgets.QRadioButton(self)
        self.radioButton.setGeometry(QtCore.QRect(40, 150, 82, 17))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 150, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")

        # Labels
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(80, 60, 91, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(80, 180, 121, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(100, 110, 47, 13))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(90, 20, 81, 31))
        self.label_4.setObjectName("label_4")

        # ComboBox 2
        self.comboBox_2 = QtWidgets.QComboBox(self)
        self.comboBox_2.setGeometry(QtCore.QRect(70, 210, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")

        # TextEdit
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(80, 130, 81, 16))
        self.textEdit.setObjectName("textEdit")

        # Push Buttons
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(30, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 260, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Grid Popup"))
        self.label.setText(_translate("Form", "Label"))
        self.label_2.setText(_translate("Form", "Label 2"))
        self.label_3.setText(_translate("Form", "Label 3"))
        self.label_4.setText(_translate("Form", "Label 4"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = GridPopup()
    dialog.show()
    sys.exit(app.exec_())

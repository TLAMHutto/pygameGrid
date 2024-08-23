# main.py

from PyQt5 import QtCore, QtGui, QtWidgets
from grid import GridWidget
from power_sim_widget import PowerSimWidget
from connections_widget import ConnectionsWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 896)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = GridWidget(self.centralwidget)  # Use GridWidget from grid.py
        self.widget.setGeometry(QtCore.QRect(10, 360, 531, 481))
        self.widget.setObjectName("widget")

        self.power_sim_widget = PowerSimWidget(self.centralwidget)
        self.power_sim_widget.setGeometry(QtCore.QRect(10, 270, 251, 80))
        self.power_sim_widget.setObjectName("power_sim_widget")

        self.connections_widget = ConnectionsWidget(self.centralwidget)
        self.connections_widget.setGeometry(QtCore.QRect(550, 360, 231, 231))
        self.connections_widget.setObjectName("connections_widget")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

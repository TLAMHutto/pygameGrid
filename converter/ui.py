# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './uiv3.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 896)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(10, 360, 531, 481))
        self.widget.setObjectName("widget")
        self.PowerSim = QtWidgets.QTabWidget(self.centralwidget)
        self.PowerSim.setGeometry(QtCore.QRect(10, 270, 251, 80))
        self.PowerSim.setObjectName("PowerSim")
        self.Power_tab = QtWidgets.QWidget()
        self.Power_tab.setObjectName("Power_tab")
        self.pushButton = QtWidgets.QPushButton(self.Power_tab)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lcdNumber = QtWidgets.QLCDNumber(self.Power_tab)
        self.lcdNumber.setGeometry(QtCore.QRect(110, 0, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.Power_tab)
        self.lcdNumber_2.setGeometry(QtCore.QRect(110, 30, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label = QtWidgets.QLabel(self.Power_tab)
        self.label.setGeometry(QtCore.QRect(180, 10, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.Power_tab)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 47, 13))
        self.label_2.setObjectName("label_2")
        self.PowerSim.addTab(self.Power_tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.PowerSim.addTab(self.tab_2, "")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(550, 360, 231, 231))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 211, 192))
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab_3)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 221, 192))
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_4)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 221, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.PowerSim.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.PowerSim.setTabText(self.PowerSim.indexOf(self.Power_tab), _translate("MainWindow", "Tab 1"))
        self.PowerSim.setTabText(self.PowerSim.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

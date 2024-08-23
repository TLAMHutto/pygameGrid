from PyQt5 import QtWidgets, QtCore
import sys
from widgets.pygame_widget import PygameWidget  # Import the PygameWidget
from widgets.power_sim_widget import PowerSimWidget
from tabs.power_tab import PowerTab
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setObjectName("MainWindow")
        self.resize(936, 904)
        
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        
        # Set the central widget
        self.setCentralWidget(self.centralwidget)
        
        # Create and add the PygameWidget
        self.pygame_widget = PygameWidget(self.centralwidget)
        self.pygame_widget.setGeometry(QtCore.QRect(0, 0, 800, 600))  # Adjust size and position as needed

        self.power_sim_widget = PowerSimWidget(self.centralwidget)
        self.power_sim_widget.setGeometry(QtCore.QRect(0, 0, 300, 150))

        self.PowerSim = QtWidgets.QTabWidget(self)
        self.PowerSim.setGeometry(QtCore.QRect(10, 50, 251, 80))
        self.PowerSim.setObjectName("PowerSim")
        
        # Create and add the PowerTab
        self.power_tab = PowerTab()
        self.PowerSim.addTab(self.power_tab, "Power Tab")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

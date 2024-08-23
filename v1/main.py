from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import sys
from grid_widget import GridWidget
from power_source import create_power_source_button  # Import the function to create the button
from display_widget import DisplayWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window with Grid')

        # Set initial size and position of the window
        self.setGeometry(1920, 30, 820, 900)  # x, y, width, height
        
        # Create a central widget and set the layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create the grid widget and add it to the layout
        self.grid_widget = GridWidget(width=600, height=600, rows=10, cols=10)
        layout.addWidget(self.grid_widget)
        self.display_widget = DisplayWidget()
        self.display_widget.setGeometry(10, 750, 590, 120)
        layout.addWidget(self.display_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

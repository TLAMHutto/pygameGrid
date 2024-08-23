# main.py

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
import sys
from grid_widget import GridWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window with Grid')
        self.setGeometry(100, 100, 800, 600)  # Set initial size of the window
        
        # Create a central widget and set the layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create the grid widget and add it to the layout
        self.grid_widget = GridWidget(width=600, height=600, rows=10, cols=10)
        layout.addWidget(self.grid_widget)

        # Add more UI elements here
        
        # Move the window to the desired position
        self.move(3226, 5)  # Set the position of the window

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

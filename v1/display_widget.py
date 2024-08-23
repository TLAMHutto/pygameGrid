# display_widget.py

from PyQt5.QtWidgets import QWidget, QPushButton, QHBoxLayout

class DisplayWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setLayout(QHBoxLayout())  # Use horizontal layout to arrange buttons in a row
        
        # Create buttons
        self.power_source_button = QPushButton("Power Source", self)
        self.button1 = QPushButton("Button 1", self)
        self.button2 = QPushButton("Button 2", self)
        self.button3 = QPushButton("Button 3", self)
        
        # Add buttons to the horizontal layout
        self.layout().addWidget(self.power_source_button)
        self.layout().addWidget(self.button1)
        self.layout().addWidget(self.button2)
        self.layout().addWidget(self.button3)
        
        # Apply a stylesheet to add an outline
        self.setStyleSheet("border: 2px solid black;")  # Black border with 2px width

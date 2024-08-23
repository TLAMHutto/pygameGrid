# popup.py

from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton

class CellInfoDialog(QDialog):
    def __init__(self, coord, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cell Information")
        self.coord = coord

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel(f"Cell Coordinate: {self.coord}", self)
        layout.addWidget(self.label)

        self.closeButton = QPushButton("Close", self)
        self.closeButton.clicked.connect(self.close)
        layout.addWidget(self.closeButton)

        self.setLayout(layout)

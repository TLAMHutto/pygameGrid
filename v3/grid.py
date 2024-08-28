# grid.py

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from grid_popup import GridPopup
class GridWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(10, 360, 531, 481)  # Set the geometry to match the dimensions
        self.width = 531
        self.height = 481
        self.rows = 10
        self.cols = 10
        self.cell_width = self.width // self.cols
        self.cell_height = self.height // self.rows
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.setFixedSize(self.width, self.height)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 1))
        
        for row in range(self.rows):
            for col in range(self.cols):
                color = QColor(0, 255, 0) if self.grid[row][col] == 1 else QColor(255, 255, 255)
                painter.fillRect(col * self.cell_width, row * self.cell_height, self.cell_width, self.cell_height, color)
                painter.drawRect(col * self.cell_width, row * self.cell_height, self.cell_width, self.cell_height)

        # Draw x-axis labels
        for col in range(self.cols):
            label = chr(ord('A') + col)
            painter.drawText(col * self.cell_width + self.cell_width // 2, self.height - 10, label)
        
        # Draw y-axis labels
        for row in range(self.rows):
            label = str(row + 1)
            painter.drawText(self.width - 30, row * self.cell_height + self.cell_height // 2, label)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = event.x()
            y = event.y()
            col = x // self.cell_width
            row = y // self.cell_height
            if 0 <= row < self.rows and 0 <= col < self.cols:
                self.grid[row][col] = 1 - self.grid[row][col]
                self.update()  # Redraw the widget
                
                # Show the popup dialog
                col_letter = chr(ord('A') + col)  # Convert column index to letter
                row_number = row + 1  # Convert row index to number
                coord = f"{col_letter}{row_number}"
                dialog = GridPopup(self)
                dialog.exec_()

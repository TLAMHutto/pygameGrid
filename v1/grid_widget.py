# grid_widget.py

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from popup import CellInfoDialog
import sys

class GridWidget(QWidget):
    def __init__(self, width=600, height=600, rows=10, cols=10):
        super().__init__()
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        self.cell_width = width // cols
        self.cell_height = height // rows
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.setFixedSize(width, height)

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
                dialog = CellInfoDialog(coord, self)
                dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = GridWidget()
    widget.show()
    sys.exit(app.exec_())

# # grid_module.py

# import pygame
# import sys
# from window_defaults import set_window_position

# class GridApp:
#     def __init__(self, width=600, height=600, rows=10, cols=10, x_pos=3226, y_pos=5):
#         pygame.init()
#         self.width = width
#         self.height = height
#         self.rows = rows
#         self.cols = cols
#         self.cell_width = width // cols
#         self.cell_height = height // rows
#         self.screen = pygame.display.set_mode((width, height))
#         pygame.display.set_caption("Pygame Grid Example")
#         pygame.display.update()  # Ensure the window is created before positioning
#         set_window_position("Pygame Grid Example", x_pos, y_pos, width, height)
#         self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
#         self.WHITE = (255, 255, 255)
#         self.BLACK = (0, 0, 0)
#         self.GREEN = (0, 255, 0)
#         self.FONT = pygame.font.Font(None, 24)  # Default font and size

#     def draw_grid(self):
#         # Draw the grid cells
#         for row in range(self.rows):
#             for col in range(self.cols):
#                 color = self.GREEN if self.grid[row][col] == 1 else self.WHITE
#                 pygame.draw.rect(self.screen, color, (col * self.cell_width, row * self.cell_height, self.cell_width, self.cell_height))
#                 pygame.draw.rect(self.screen, self.BLACK, (col * self.cell_width, row * self.cell_height, self.cell_width, self.cell_height), 1)

#         # Draw x-axis labels (A-Z)
#         for col in range(self.cols):
#             label = chr(ord('A') + col)  # Convert column index to letter
#             text_surface = self.FONT.render(label, True, self.BLACK)
#             self.screen.blit(text_surface, (col * self.cell_width + self.cell_width // 2 - text_surface.get_width() // 2, self.height - 20))

#         # Draw y-axis labels (1-10)
#         for row in range(self.rows):
#             label = str(row + 1)  # Row index starts from 0, so add 1
#             text_surface = self.FONT.render(label, True, self.BLACK)
#             self.screen.blit(text_surface, (self.width - 30, row * self.cell_height + self.cell_height // 2 - text_surface.get_height() // 2))

#     def toggle_cell(self, pos):
#         x, y = pos
#         col = x // self.cell_width
#         row = y // self.cell_height
#         self.grid[row][col] = 1 - self.grid[row][col]  # Toggle between 0 and 1
        
#         # Convert row and column to coordinates
#         col_letter = chr(ord('A') + col)  # Convert column index to letter
#         row_number = row + 1  # Convert row index to number
#         coord = f"{col_letter}{row_number}"
#         print(f"Clicked on: {coord}")

#     def run(self):
#         running = True
#         while running:
#             self.screen.fill(self.WHITE)
#             self.draw_grid()

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if event.button == 1:  # Left-click
#                         self.toggle_cell(pygame.mouse.get_pos())

#             pygame.display.flip()

#         pygame.quit()
#         sys.exit()
# grid_widget.py

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QRect
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = GridWidget()
    widget.show()
    sys.exit(app.exec_())

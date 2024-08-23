from PyQt5 import QtWidgets, QtCore

class PygameWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setObjectName("PygameWidget")
        self.setGeometry(QtCore.QRect(0, 0, 800, 600))  # Adjust as needed
        
        self.pygame_grid = QtWidgets.QGraphicsView(self)
        self.pygame_grid.setGeometry(QtCore.QRect(10, 140, 541, 621))
        self.pygame_grid.setObjectName("pygame_grid")

        # Additional setup for the pygame grid can go here

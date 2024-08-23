from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QOpenGLWidget

class MatplotTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MatplotTab, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MatplotTab")
        self.setGeometry(0, 0, 300, 200)  # Adjust size and position as needed

        # Create a QOpenGLWidget
        self.matplotWidget = QOpenGLWidget(self)
        self.matplotWidget.setGeometry(10, 10, 280, 180)  # Adjust size and position as needed

        # Example setup for the OpenGL widget
        self.matplotWidget.setObjectName("matplotWidget")

        # Additional setup can be done here

from PyQt5 import QtWidgets, QtCore

class MatGraphWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setObjectName("MatGraphWidget")
        
        # Create and configure the MatGraph QTabWidget
        self.MatGraph = QtWidgets.QTabWidget(self)
        self.MatGraph.setGeometry(QtCore.QRect(560, 460, 361, 301))
        self.MatGraph.setObjectName("MatGraph")
        
        # Create the first tab with a QGraphicsView
        self.graph_2 = QtWidgets.QWidget()
        self.graph_2.setObjectName("graph_2")
        self.graph = QtWidgets.QGraphicsView(self.graph_2)
        self.graph.setGeometry(QtCore.QRect(0, 0, 351, 271))
        self.graph.setObjectName("graph")
        self.MatGraph.addTab(self.graph_2, "Graph")
        
        # Create the second tab with another QGraphicsView
        self.matplot_2 = QtWidgets.QWidget()
        self.matplot_2.setObjectName("matplot_2")
        self.matplot = QtWidgets.QGraphicsView(self.matplot_2)
        self.matplot.setGeometry(QtCore.QRect(0, 0, 351, 271))
        self.matplot.setObjectName("matplot")
        self.MatGraph.addTab(self.matplot_2, "Matplot")

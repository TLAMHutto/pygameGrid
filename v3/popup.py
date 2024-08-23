
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QDialog,
    QPushButton,
    QRadioButton
)

class CellInfoDialog(QDialog):
    def __init__(self, cell_coord, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cell Information")

        # Create widgets for the dialog
        self.label = QLabel(f"Cell Coordinate: {cell_coord}", self)
        self.check_box1 = QCheckBox("Input", self)
        self.check_box2 = QCheckBox("Output", self)
        self.combo_box1 = QComboBox(self)
        self.combo_box1.addItems(["Resistor", "Capacitor", "Load"])
        self.combo_box2 = QComboBox(self)
        self.combo_box2.addItems(["V", "Ohms", "Watts"])
        self.line_edit = QLineEdit(self)
        self.radio_button = QRadioButton("Connect to grid", self)
        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.accept)  # Close the dialog on OK

        # Create layouts
        main_layout = QVBoxLayout()
        check_box_layout = QHBoxLayout()
        combo_box_layout = QHBoxLayout()  # Layout for combo boxes

        # Add widgets to the horizontal layout for check boxes
        check_box_layout.addWidget(self.check_box1)
        check_box_layout.addWidget(self.check_box2)

        # Add widgets to the horizontal layout for combo boxes
        combo_box_layout.addWidget(self.combo_box1)
        combo_box_layout.addWidget(self.combo_box2)

        # Add layouts and other widgets to the main vertical layout
        main_layout.addWidget(self.label)
        main_layout.addLayout(check_box_layout)  # Add the horizontal layout here
        main_layout.addLayout(combo_box_layout)  # Add the horizontal combo box layout here
        main_layout.addWidget(self.line_edit)
        main_layout.addWidget(self.radio_button)
        main_layout.addWidget(self.ok_button)
        
        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = CellInfoDialog("A1")
    dialog.exec_()

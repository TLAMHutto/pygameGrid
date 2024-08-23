from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QApplication

def create_power_source_button(parent=None):
    # Create the 'Add Power Source' button
    button = QPushButton("Add Power Source")
    button.setFixedSize(120, 30)
    
    # Connect the button's click event to the method that shows the dialog
    button.clicked.connect(lambda: show_power_source_dialog(parent))
    
    return button

def show_power_source_dialog(parent=None):
    # Create the dialog box
    dialog = QDialog(parent)
    dialog.setWindowTitle("Power Source Details")
    
    # Create widgets for the dialog
    voltage_label = QLabel("Voltage:", dialog)
    voltage_input = QLineEdit(dialog)
    voltage_unit_label = QLabel("V", dialog)
    current_label = QLabel("Current:", dialog)
    current_input = QLineEdit(dialog)
    current_unit_label = QLabel("I", dialog)
    
    # Create layouts
    main_layout = QVBoxLayout(dialog)
    
    # Voltage layout
    voltage_layout = QHBoxLayout()
    voltage_layout.addWidget(voltage_input)
    voltage_layout.addWidget(voltage_unit_label)
    
    # Current layout
    current_layout = QHBoxLayout()
    current_layout.addWidget(current_input)
    current_layout.addWidget(current_unit_label)
    
    # Create the Add button
    add_button = QPushButton("Add", dialog)
    
    # Add widgets and layouts to the main vertical layout
    main_layout.addWidget(voltage_label)
    main_layout.addLayout(voltage_layout)
    main_layout.addWidget(current_label)
    main_layout.addLayout(current_layout)
    main_layout.addWidget(add_button)  # Add the Add button to the layout
    
    # Set the layout to the dialog
    dialog.setLayout(main_layout)
    
    # Show the dialog
    dialog.exec_()

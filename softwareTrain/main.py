import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox
from PyQt6.QtCore import QTimer

class TrainControllerGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Create labels for displaying information
        self.power_label = QLabel('Power: N/A')
        self.failures_label = QLabel('Failures: N/A')
        self.speed_label = QLabel('Speed: N/A')
        self.distance_label = QLabel('Distance to Travel: N/A')

        # Create a combo box for mode selection
        self.mode_combo = QComboBox()
        self.mode_combo.addItem('Automatic Mode')
        self.mode_combo.addItem('Manual Mode')
        self.mode_combo.currentIndexChanged.connect(self.update_info)

        # Create buttons for adjusting speed in manual mode
        self.increase_speed_button = QPushButton('Increase Speed', self)
        self.increase_speed_button.clicked.connect(self.increase_speed)

        self.decrease_speed_button = QPushButton('Decrease Speed', self)
        self.decrease_speed_button.clicked.connect(self.decrease_speed)

        # Create an emergency brake button
        self.emergency_brake_button = QPushButton('Emergency Brake', self)
        self.emergency_brake_button.clicked.connect(self.emergency_brake)
        self.emergency_brake_button.setStyleSheet('background-color: red; color: white; font-size: 16px; padding: 10px;')

        # Create a service brake button
        self.service_brake_button = QPushButton('Service Brake', self)
        self.service_brake_button.clicked.connect(self.start_service_brake)
        self.service_brake_button.setStyleSheet('background-color: orange; color: white; font-size: 16px; padding: 10px;')

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.power_label)
        layout.addWidget(self.failures_label)
        layout.addWidget(self.speed_label)
        layout.addWidget(self.distance_label)
        layout.addWidget(self.mode_combo)

        # Add buttons for adjusting speed in manual mode
        layout.addWidget(self.increase_speed_button)
        layout.addWidget(self.decrease_speed_button)

        layout.addWidget(self.emergency_brake_button)
        layout.addWidget(self.service_brake_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Set window properties
        self.setWindowTitle('Train Controller')
        self.setGeometry(100, 100, 400, 200)  # (x, y, width, height)

        # Set default speed
        self.current_speed = 20
        self.update_speed_label()

        # Create QTimer for service brake
        self.service_brake_timer = QTimer(self)
        self.service_brake_timer.timeout.connect(self.service_brake)
        self.service_brake_timer.setInterval(1000)  # Decrease speed every second

        # Update information initially
        self.update_info()

    def update_info(self):
        # Replace the following lines with actual data retrieval logic based on the selected mode
        mode = self.mode_combo.currentText()
        power = '1000 W'
        failures = '0'
        distance = '10 miles'

        # Update labels with new information
        self.power_label.setText(f'Power: {power}')
        self.failures_label.setText(f'Failures: {failures}')
        self.distance_label.setText(f'Distance to Travel: {distance}')

        # Disable/enable buttons based on the selected mode
        manual_mode_enabled = mode == 'Manual Mode'
        self.increase_speed_button.setVisible(manual_mode_enabled)
        self.decrease_speed_button.setVisible(manual_mode_enabled)
        self.service_brake_button.setVisible(manual_mode_enabled)
        self.service_brake_button.setEnabled(manual_mode_enabled)

    def increase_speed(self):
        # Add logic to increase speed in manual mode
        self.current_speed += 1
        self.update_speed_label()

    def decrease_speed(self):
        # Add logic to decrease speed in manual mode
        self.current_speed = max(0, self.current_speed - 1)  # Ensure speed doesn't go below 0
        self.update_speed_label()

    def emergency_brake(self):
        # Add logic for emergency brake (set speed to 0)
        self.current_speed = 0
        self.update_speed_label()

    def start_service_brake(self):
        # Start the service brake timer when the button is clicked
        self.service_brake_timer.start()

    def service_brake(self):
        # Add logic for service brake (decrease speed by 3 per second until 0)
        if self.current_speed > 0:
            self.current_speed = max(0, self.current_speed - 3)
            self.update_speed_label()
        else:
            # Stop the timer when speed reaches 0
            self.service_brake_timer.stop()

    def update_speed_label(self):
        self.speed_label.setText(f'Speed: {self.current_speed} mph')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TrainControllerGUI()
    window.show()
    sys.exit(app.exec())

from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow
# Only needed for access to command line arguments


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication([])

# Create a Qt widget, which will be our window.

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Track Model")

    def initDropdown(self):
        dropdown = QComboBox()
        # dropdown.addItems([List of Block names])
        dropdown.addItem("Option 1")
        dropdown.addItem("Option 2")
        dropdown.activated.connect(self.update)
        self.setCentralWidget(dropdown)

    def update(self):
        pass
        
        


window = MainScreen()
window.initDropdown()

window.show()  # IMPORTANT!!!!! Windows are hidden by default.



# Start the event loop.
app.exec()
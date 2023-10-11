import sys
from HWTrackDisplay import Ui_MainWindow
from PyQt6 import QtWidgets

def booleanTest():
    print("hi")

#Code below to run the UI
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

if(ui.updatedOccu == "yes"):
    booleanTest

sys.exit(app.exec())
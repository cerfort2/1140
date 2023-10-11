import sys
from HWTrackDisplay import Ui_MainWindow
from PyQt6 import QtWidgets

#Code below to run the UI
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
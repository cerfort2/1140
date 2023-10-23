import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow, QFileDialog
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets

from HWTrackDisplay import Ui_MainWindow

class HWTrackControllerGUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

        #Buttons/Setup for Automatic Mode
        self.ui.listWidget_3.itemClicked.connect(self.checkListAutomatic) #Check if Line Selected
        self.ui.comboBox.currentIndexChanged.connect(self.checkWaysideSelectionAutomatic) #Checks if a Wayside Selected

        #Stuff to be changeed
        self.ui.comboBox_5.currentTextChanged.connect(self.defaultLight)
        self.ui.comboBox_6.currentTextChanged.connect(self.defaultCrossroad)
        self.ui.comboBox_7.currentTextChanged.connect(self.defaultSwitch)


        #Buttons/Setup for Manual Mode



        #Buttons/Setup for Test Bench



        #Buttons/Setup for Whole UI
        self.ui.pushButton_3.clicked.connect(self.openArduinoFile) #Opens PLC File

    def init_ui(self): #SetupUI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    #Functions used in Whole UI
    def openArduinoFile(self): #Functionality for PLC File Opening
        dialog = QFileDialog()
        dialog.setNameFilter("Arduino File (*.ino)")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialogSuccessful = dialog.exec()
        if dialogSuccessful:
            fileLocation = dialog.selectedFiles()[0]
            self.ui.label_4.setText(fileLocation)
            arduino = "C:\Program Files (x86)\Arduino\\arduino.exe"
            command = f'"{arduino}" "{fileLocation}"'
            subprocess.run(command, shell=True)    


    #Functions used in Automatic Mode
    def checkListAutomatic(self): #Checks if a Line is selected or not to grey out combo boxes and list
        if self.ui.listWidget_3.currentItem() is not None:
            self.ui.comboBox.setEnabled(True)
    def checkWaysideSelectionAutomatic(self): #Checks if still selecting crossroad to grey out button
        if self.ui.comboBox.currentText() == "Select Wayside":
            for combo_box in [self.ui.comboBox_5, self.ui.comboBox_6, self.ui.comboBox_7, self.ui.listWidget_7, self.ui.listWidget_8]:
                combo_box.setDisabled(True)
        else:
            for combo_box in [self.ui.comboBox_5, self.ui.comboBox_6, self.ui.comboBox_7, self.ui.listWidget_7, self.ui.listWidget_8]:
                combo_box.setEnabled(True)


    #Functions used in Manual Mode



    #Functions used in Test Bench




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HWTrackControllerGUI()
    window.show()
    sys.exit(app.exec())
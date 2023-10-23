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
        self.ui.listWidget_3.itemClicked.connect(self.checkListAutomatic)
        self.ui.comboBox.currentIndexChanged.connect(self.checkWaysideSelectionAutomatic)

        #Stuff to be changed
        """
        self.ui.comboBox_5.currentTextChanged.connect(self.defaultLight)
        self.ui.comboBox_6.currentTextChanged.connect(self.defaultCrossroad)
        self.ui.comboBox_7.currentTextChanged.connect(self.defaultSwitch)
        """

        #Buttons/Setup for Manual Mode
        self.ui.listWidget.itemClicked.connect(self.checkListManual)
        self.ui.comboBox_2.currentIndexChanged.connect(self.lightChangeManual)
        self.ui.comboBox_3.currentIndexChanged.connect(self.crossChangeManual)
        self.ui.comboBox_12.currentIndexChanged.connect(self.checkWaysideSelectionManual)
        self.ui.comboBox_4.currentIndexChanged.connect(self.switchChangeManual)

        #Stuff to be changed
        """
        self.ui.listWidget_2.itemClicked.connect(lambda item=red: self.saveLight(item.text()))
        self.ui.comboBox_2.currentTextChanged.connect(self.defaultLight)
        self.ui.pushButton.clicked.connect(self.crossroadUpdater)
        self.ui.comboBox_3.currentTextChanged.connect(self.defaultCrossroad)
        self.ui.pushButton_2.clicked.connect(self.switchUpdater)
        self.ui.comboBox_4.currentTextChanged.connect(self.defaultSwitch)
        #This way of running PLC code is wrong will be changed a lot
        self.ui.listWidget_5.model().rowsInserted.connect(self.plcCode)
        self.ui.listWidget_5.model().rowsRemoved.connect(self.plcCode)
        """

        #Buttons/Setup for Test Bench
        self.ui.listWidget_9.itemClicked.connect(self.checkListTest)
        self.ui.comboBox_8.currentIndexChanged.connect(self.trackChangeTest)
        self.ui.comboBox_9.currentIndexChanged.connect(self.lightChangeTest)
        self.ui.comboBox_10.currentIndexChanged.connect(self.crossChangeTest)
        self.ui.comboBox_11.currentIndexChanged.connect(self.switchChangeTest)
        self.ui.comboBox_13.currentIndexChanged.connect(self.checkWaysideSelectionTest)

        #Needs to be configured properly to display info properly
        self.ui.comboBox_11.currentTextChanged.connect(self.switchSelection)

        #Stuff to be changed
        """
        self.ui.pushButton_4.clicked.connect(lambda: self.toggleOccu(self.comboBox_8.currentText()))
        self.ui.pushButton_5.clicked.connect(lambda: self.toggleFailure(self.comboBox_8.currentText()))
        self.ui.listWidget_4.itemClicked.connect(lambda item=redTest: self.changeLight(item.text()))
        self.ui.listWidget_10.itemClicked.connect(lambda item=cross: self.changeCrossroad(item.text()))
        self.ui.listWidget_11.itemClicked.connect(lambda item=switch: self.changeSwitch(item.text()))
        """
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
    def crossChangeManual(self): #Checks if still selecting crossroad to grey out button
        if self.ui.comboBox_3.currentText() == "Select Crossroad":
            self.ui.pushButton.setDisabled(True)
        else:
            self.ui.pushButton.setDisabled(False)
    def switchChangeManual(self): #Checks if still selecting switch to grey out button
        if self.ui.comboBox_4.currentText() == "Select Switch":
            self.ui.pushButton_2.setDisabled(True)
        else:
            self.ui.pushButton_2.setDisabled(False)
    def lightChangeManual(self): #Checks if still selecting light to grey out list
        if self.ui.comboBox_2.currentText() == "Select Light":
            self.ui.listWidget_2.setDisabled(True)
        else:
            self.ui.listWidget_2.setDisabled(False)
    def checkListManual(self): #Checks if a wayside is selected or not to grey out combo boxes or not
        if self.ui.listWidget.currentItem() is not None:
            self.ui.comboBox_12.setEnabled(True)
    def checkWaysideSelectionManual(self): #Checks if still selecting crossroad to grey out button
        if self.ui.comboBox_12.currentText() == "Select Wayside":
            for combo_box in [self.ui.comboBox_2, self.ui.comboBox_3, self.ui.comboBox_4, self.ui.listWidget_5, self.ui.listWidget_6]:
                combo_box.setDisabled(True)
        else:
            for combo_box in [self.ui.comboBox_2, self.ui.comboBox_3, self.ui.comboBox_4, self.ui.listWidget_5, self.ui.listWidget_6]:
                combo_box.setEnabled(True)


    #Functions used in Test Bench
    def checkListTest(self): #Checks if a line is selected or not to grey out combo boxes
        if self.ui.listWidget_9.currentItem() is not None:
            self.ui.comboBox_13.setEnabled(True)
    def checkWaysideSelectionTest(self): #Checks if still selecting wayside to grey out button
        if self.ui.comboBox_13.currentText() == "Select Wayside":
            for combo_box in [self.ui.comboBox_9, self.ui.comboBox_10, self.ui.comboBox_11, self.ui.comboBox_8]:
                combo_box.setDisabled(True)
        else:
            for combo_box in [self.ui.comboBox_9, self.ui.comboBox_10, self.ui.comboBox_11, self.ui.comboBox_8]:
                combo_box.setEnabled(True)
    def crossChangeTest(self): #Checks if still selecting crossroad to grey out list
        if self.ui.comboBox_10.currentText() == "Select Crossroad":
            self.ui.listWidget_10.setDisabled(True)
        else:
            self.ui.listWidget_10.setDisabled(False)
    def switchChangeTest(self): #Checks if still selecting switch to grey out list
        if self.ui.comboBox_11.currentText() == "Select Switch":
            self.ui.listWidget_11.setDisabled(True)
        else:
            self.ui.listWidget_11.setDisabled(False)
    def lightChangeTest(self): #Checks if still selecting light to grey out list
        if self.ui.comboBox_9.currentText() == "Select Light":
            self.ui.listWidget_4.setDisabled(True)
        else:
            self.ui.listWidget_4.setDisabled(False)
    def trackChangeTest(self):
        if self.ui.comboBox_8.currentText() == "Track Selection":
            self.ui.pushButton_4.setDisabled(True)
            self.ui.pushButton_5.setDisabled(True)
        else:
            self.ui.pushButton_4.setDisabled(False)
            self.ui.pushButton_5.setDisabled(False)

    def switchSelection(self, item): #NEEDS TO BE CONFIGURED PROPERLY
        if item == "Switch 1":
            temp = self.ui.listWidget_11.item(0)
            temp.setText("A->B")
            temp = self.ui.listWidget_11.item(1)
            temp.setText("C->A")
        elif item == "Switch 2":
            temp = self.ui.listWidget_11.item(0)
            temp.setText("B->D")
            temp = self.ui.listWidget_11.item(1)
            temp.setText("B->E")
        else:
            temp = self.ui.listWidget_11.item(0)
            temp.setText("")
            temp = self.ui.listWidget_11.item(1)
            temp.setText("")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HWTrackControllerGUI()
    window.show()
    sys.exit(app.exec())
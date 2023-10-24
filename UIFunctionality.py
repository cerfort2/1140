import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow, QFileDialog
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets
from HWTrackDisplay import Ui_MainWindow
from WaysideClass import Wayside
#from UI_Breadboard_Class import Operations

#operate = Operations() #Class to perform operations on the breadboard

class HWTrackControllerGUI(QMainWindow):
    
    Waysides = [Wayside(), Wayside(), Wayside(), Wayside()] #All The waysides going int order of 1,2,3,4 for Green Line
    #Configuration of all tracks in Green Line Waysides
    #Wayside 1
    Waysides[0].createTrack(False, False, True, False) #A1 [0]
    Waysides[0].createTrack(False, False, False, True) #A2 [1]
    Waysides[0].createTrack(False, False, False, False) #A3 [2]
    Waysides[0].createTrack(False, False, False, False) #B4 [3]
    Waysides[0].createTrack(False, False, False, False) #B5 [4]
    Waysides[0].createTrack(False, False, False, False) #B6 [5]
    Waysides[0].createTrack(False, False, False, False) #C7 [6]
    Waysides[0].createTrack(False, False, False, False) #C8 [7]
    Waysides[0].createTrack(False, False, False, True) #C9 [8]
    Waysides[0].createTrack(False, False, False, False) #C10 [9]
    Waysides[0].createTrack(False, False, False, False) #C11 [10]
    Waysides[0].createTrack(False, False, False, False) #C12 [11]
    Waysides[0].createTrack(True, False, True, False, "A1", "C12") #D13 [12]
    Waysides[0].createTrack(False, False, False, False) #D14 [13]
    Waysides[0].createTrack(False, False, False, False) #D15 [14]
    Waysides[0].createTrack(False, False, False, True) #D16 [15]
    Waysides[0].createTrack(False, False, False, False) #E17 [16]
    Waysides[0].createTrack(False, False, False, False) #E18 [17]
    Waysides[0].createTrack(False, True, False, False) #E19 [18]
    Waysides[0].createTrack(False, False, False, False) #E20 [19]
    Waysides[0].createTrack(False, False, False, False) #F21 [20]
    Waysides[0].createTrack(False, False, False, True) #F22 [21]
    Waysides[0].createTrack(False, False, False, False) #F23 [22]
    Waysides[0].createTrack(False, False, False, False) #F24 [23]
    Waysides[0].createTrack(False, False, False, False) #F25 [24]
    Waysides[0].createTrack(False, False, False, False) #F26 [25]
    Waysides[0].createTrack(False, False, False, False) #F27 [26]
    Waysides[0].createTrack(False, False, False, False) #F28 [27]
    Waysides[0].createTrack(True, False, True, False, "Z150", "G30") #G29 [28]
    Waysides[0].createTrack(False, False, False, False) #G30 [29]
    Waysides[0].createTrack(False, False, False, True) #G31 [30]
    Waysides[0].createTrack(False, False, False, False) #G32 [31]
    Waysides[0].createTrack(False, False, True, False) #Z150 [32]
    #Wayside 2
    #switch:bool, crossroad:bool, light:bool, station:bool
    Waysides[1].createTrack(False, False, False, False) #H33 [0]
    Waysides[1].createTrack(False, False, False, False) #H34 [1]
    Waysides[1].createTrack(False, False, False, False) #H35 [2]
    Waysides[1].createTrack(False, False, False, False) #I36 [3]
    Waysides[1].createTrack(False, False, False, False) #I37 [4]
    Waysides[1].createTrack(False, False, False, False) #I38 [5]
    Waysides[1].createTrack(False, False, False, True) #I39 [6]
    Waysides[1].createTrack(False, False, False, False) #I40 [7]
    Waysides[1].createTrack(False, False, False, False) #I41 [8]
    Waysides[1].createTrack(False, False, False, False) #I42 [9]
    Waysides[1].createTrack(False, False, False, False) #I43 [10]
    Waysides[1].createTrack(False, False, False, False) #I44 [11]
    Waysides[1].createTrack(False, False, False, False) #I45 [12]
    Waysides[1].createTrack(False, False, False, False) #I46 [13]
    Waysides[1].createTrack(False, False, False, False) #I47 [14]
    Waysides[1].createTrack(False, False, False, True) #I48 [15]
    Waysides[1].createTrack(False, False, False, False) #I49 [16]
    Waysides[1].createTrack(False, False, False, False) #I50 [17]
    Waysides[1].createTrack(False, False, False, False) #I51 [18]
    Waysides[1].createTrack(False, False, False, False) #I52 [19]
    Waysides[1].createTrack(False, False, False, False) #I53 [20]
    Waysides[1].createTrack(False, False, False, False) #I54 [21]
    Waysides[1].createTrack(False, False, False, False) #I55 [22]
    Waysides[1].createTrack(False, False, False, False) #I56 [23]
    Waysides[1].createTrack(False, False, False, True) #I57 [24]
    Waysides[1].createTrack(True, False, True, False, "J59", "YARD") #J58 [25]
    Waysides[1].createTrack(False, False, False, False) #J59 [26]
    Waysides[1].createTrack(False, False, False, False) #J60 [27]
    Waysides[1].createTrack(False, False, True, False) #J61 [28]
    Waysides[1].createTrack(True, False, False, False, "YARD", "J61") #J62 [29]
    Waysides[1].createTrack(False, False, False, False) #K63 [30]
    Waysides[1].createTrack(False, False, False, False) #K64 [31]
    Waysides[1].createTrack(False, False, False, True) #K65 [32]
    Waysides[1].createTrack(False, False, False, False) #K66 [33]
    Waysides[1].createTrack(False, False, False, False) #K67 [34]
    Waysides[1].createTrack(False, False, False, False) #K68 [35]
    Waysides[1].createTrack(False, False, False, False) #L69 [36]
    Waysides[1].createTrack(False, False, False, False) #L70 [37]
    Waysides[1].createTrack(False, False, False, False) #L71 [38]
    Waysides[1].createTrack(False, False, False, False) #L72 [39]
    Waysides[1].createTrack(False, False, False, True) #L73 [40]
    Waysides[1].createTrack(False, False, True, False) #YARD [41]
    #Wayside 3



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
        value = self.ui.listWidget_3.currentItem()
        if value.text() == "Green Line":
            self.configureWaysidesAutomaticGreen()
        elif value.text() == "Red Line":
            for i in range(self.ui.comboBox.count(), 0, -1):
                self.ui.comboBox.removeItem(i)
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
        value = self.ui.listWidget.currentItem()
        if value.text() == "Green Line":
            self.configureWaysidesManualGreen()
        elif value.text() == "Red Line":
            for i in range(self.ui.comboBox_12.count(), 0, -1):
                self.ui.comboBox_12.removeItem(i)
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
        value = self.ui.listWidget_9.currentItem()
        if value.text() == "Green Line":
            self.configureWaysidesTestGreen()
        elif value.text() == "Red Line":
            for i in range(self.ui.comboBox_13.count(), 0, -1):
                self.ui.comboBox_13.removeItem(i)
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

    #Code for configuration of Green Line Values
    #Automatic Mode
    def configureWaysidesAutomaticGreen(self):
        for i in range(self.ui.comboBox.count(), 0, -1):
            self.ui.comboBox.removeItem(i)
        self.ui.comboBox.addItem("Wayside 1")
        self.ui.comboBox.addItem("Wayside 2")
        self.ui.comboBox.addItem("Wayside 3")
        self.ui.comboBox.addItem("Wayside 4")
    def configureLightsAutomaticGreen(self, currentWayside): #Sets proper lights for each wayside selection
        if(currentWayside == "Wayside 1"):
            return
        elif(currentWayside == "Wayside 2"):
            return
        elif(currentWayside == "Wayside 3"):
            return
        elif(currentWayside == "Wayside 4"):
            return
    def configureCrossroadsAutomaticGreen(self, currentWayside): #Sets proper crossroads for each wayside selection
        if(currentWayside == "Wayside 1"):
            return
        elif(currentWayside == "Wayside 2"):
            return
        elif(currentWayside == "Wayside 3"):
            return
        elif(currentWayside == "Wayside 4"):
            return
    def configureSwitchAutomaticGreen(self, currentWayside): #Sets proper switches for each wayside selection
        if(currentWayside == "Wayside 1"):
            return
        elif(currentWayside == "Wayside 2"):
            return
        elif(currentWayside == "Wayside 3"):
            return
        elif(currentWayside == "Wayside 4"):
            return
        
    
    #Manual Mode
    def configureWaysidesManualGreen(self):
        for i in range(self.ui.comboBox_12.count(), 0, -1):
            self.ui.comboBox_12.removeItem(i)
        self.ui.comboBox_12.addItem("Wayside 1")
        self.ui.comboBox_12.addItem("Wayside 2")
        self.ui.comboBox_12.addItem("Wayside 3")
        self.ui.comboBox_12.addItem("Wayside 4")
    def configureLightsManualGreen(self, currentWayside): #Sets proper lights for each wayside selection
        if(currentWayside == "Wayside 1"):
            return
        elif(currentWayside == "Wayside 2"):
            return
        elif(currentWayside == "Wayside 3"):
            return
        elif(currentWayside == "Wayside 4"):
            return
    def configureCrossroadsManualGreen(self, currentWayside): #Sets proper crossroads for each wayside selection
        if(currentWayside == "Wayside 1"):
            return
        elif(currentWayside == "Wayside 2"):
            return
        elif(currentWayside == "Wayside 3"):
            return
        elif(currentWayside == "Wayside 4"):
            return
    def configureSwitchManualGreen(self, currentWayside): #Sets proper switches for each wayside selection
        if(currentWayside == "Wayside 1"):
            return
        elif(currentWayside == "Wayside 2"):
            return
        elif(currentWayside == "Wayside 3"):
            return
        elif(currentWayside == "Wayside 4"):
            return
        

    #Test Bench
    def configureWaysidesTestGreen(self):
        for i in range(self.ui.comboBox_13.count(), 0, -1):
            self.ui.comboBox_13.removeItem(i)
        self.ui.comboBox_13.addItem("Wayside 1")
        self.ui.comboBox_13.addItem("Wayside 2")
        self.ui.comboBox_13.addItem("Wayside 3")
        self.ui.comboBox_13.addItem("Wayside 4")
    def configureLightsTestGreen(self, currentWayside): #Sets proper lights for each wayside selection
        if(currentWayside == "Wayside 1"):
            return
        elif(currentWayside == "Wayside 2"):
            return
        elif(currentWayside == "Wayside 3"):
            return
        elif(currentWayside == "Wayside 4"):
            return
    def configureCrossroadsTestGreen(self, currentWayside): #Sets proper crossroads for each wayside selection
        if(currentWayside == "Wayside 1"):
            return
        elif(currentWayside == "Wayside 2"):
            return
        elif(currentWayside == "Wayside 3"):
            return
        elif(currentWayside == "Wayside 4"):
            return
    def configureSwitchTestGreen(self, currentWayside): #Sets proper switches for each wayside selection
        if(currentWayside == "Wayside 1"):
            return
        elif(currentWayside == "Wayside 2"):
            return
        elif(currentWayside == "Wayside 3"):
            return
        elif(currentWayside == "Wayside 4"):
            return
    def configureTrackSelectionGreen(self, currentWayside):
        if(currentWayside == "Wayside 1"):
            return
        elif(currentWayside == "Wayside 2"):
            return
        elif(currentWayside == "Wayside 3"):
            return
        elif(currentWayside == "Wayside 4"):
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HWTrackControllerGUI()
    window.show()
    sys.exit(app.exec())
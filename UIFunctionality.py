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
    
    Waysides = [Wayside(), Wayside(), Wayside(), Wayside()] #All The waysides going in order of 1,2,3,4 for Green Line

    #Configuration of all tracks in Green Line Waysides
    #switch:bool, crossroad:bool, light:bool, station:bool, trackName:str, right = "", left = ""
    #Wayside 1
    Waysides[0].createTrack(False, False, True, False, "A1") #A1 [0]
    Waysides[0].createTrack(False, False, False, True, "A2") #A2 [1]
    Waysides[0].createTrack(False, False, False, False, "A3") #A3 [2]
    Waysides[0].createTrack(False, False, False, False, "B4") #B4 [3]
    Waysides[0].createTrack(False, False, False, False, "B5") #B5 [4]
    Waysides[0].createTrack(False, False, False, False, "B6") #B6 [5]
    Waysides[0].createTrack(False, False, False, False, "C7") #C7 [6]
    Waysides[0].createTrack(False, False, False, False, "C8") #C8 [7]
    Waysides[0].createTrack(False, False, False, True, "C9") #C9 [8]
    Waysides[0].createTrack(False, False, False, False, "C10") #C10 [9]
    Waysides[0].createTrack(False, False, False, False, "C11") #C11 [10]
    Waysides[0].createTrack(False, False, False, False, "C12") #C12 [11]
    Waysides[0].createTrack(True, False, True, False, "D13", "A1", "C12") #D13 [12]
    Waysides[0].createTrack(False, False, False, False, "D14") #D14 [13]
    Waysides[0].createTrack(False, False, False, False, "D15") #D15 [14]
    Waysides[0].createTrack(False, False, False, True, "D16") #D16 [15]
    Waysides[0].createTrack(False, False, False, False, "E17") #E17 [16]
    Waysides[0].createTrack(False, False, False, False, "E18") #E18 [17]
    Waysides[0].createTrack(False, True, False, False, "E19") #E19 [18]
    Waysides[0].createTrack(False, False, False, False, "E20") #E20 [19]
    Waysides[0].createTrack(False, False, False, False, "F21") #F21 [20]
    Waysides[0].createTrack(False, False, False, True, "F22") #F22 [21]
    Waysides[0].createTrack(False, False, False, False, "F23") #F23 [22]
    Waysides[0].createTrack(False, False, False, False, "F24") #F24 [23]
    Waysides[0].createTrack(False, False, False, False, "F25") #F25 [24]
    Waysides[0].createTrack(False, False, False, False, "F26") #F26 [25]
    Waysides[0].createTrack(False, False, False, False, "F27") #F27 [26]
    Waysides[0].createTrack(False, False, False, False, "F28") #F28 [27]
    Waysides[0].createTrack(True, False, True, False, "G29", "Z150", "G30") #G29 [28]
    Waysides[0].createTrack(False, False, False, False, "G30") #G30 [29]
    Waysides[0].createTrack(False, False, False, True, "G31") #G31 [30]
    Waysides[0].createTrack(False, False, False, False, "G32") #G32 [31]
    Waysides[0].createTrack(False, False, True, False, "Z150") #Z150 [32]
    #Wayside 2
    Waysides[1].createTrack(False, False, False, False, "H33") #H33 [0]
    Waysides[1].createTrack(False, False, False, False, "H34") #H34 [1]
    Waysides[1].createTrack(False, False, False, False, "H35") #H35 [2]
    Waysides[1].createTrack(False, False, False, False, "I36") #I36 [3]
    Waysides[1].createTrack(False, False, False, False, "I37") #I37 [4]
    Waysides[1].createTrack(False, False, False, False, "I38") #I38 [5]
    Waysides[1].createTrack(False, False, False, True, "I39") #I39 [6]
    Waysides[1].createTrack(False, False, False, False, "I40") #I40 [7]
    Waysides[1].createTrack(False, False, False, False, "I41") #I41 [8]
    Waysides[1].createTrack(False, False, False, False, "I42") #I42 [9]
    Waysides[1].createTrack(False, False, False, False, "I43") #I43 [10]
    Waysides[1].createTrack(False, False, False, False, "I44") #I44 [11]
    Waysides[1].createTrack(False, False, False, False, "I45") #I45 [12]
    Waysides[1].createTrack(False, False, False, False, "I46") #I46 [13]
    Waysides[1].createTrack(False, False, False, False, "I47") #I47 [14]
    Waysides[1].createTrack(False, False, False, True, "I48") #I48 [15]
    Waysides[1].createTrack(False, False, False, False, "I49") #I49 [16]
    Waysides[1].createTrack(False, False, False, False, "I50") #I50 [17]
    Waysides[1].createTrack(False, False, False, False, "I51") #I51 [18]
    Waysides[1].createTrack(False, False, False, False, "I52") #I52 [19]
    Waysides[1].createTrack(False, False, False, False, "I53") #I53 [20]
    Waysides[1].createTrack(False, False, False, False, "I54") #I54 [21]
    Waysides[1].createTrack(False, False, False, False, "I55") #I55 [22]
    Waysides[1].createTrack(False, False, False, False, "I56") #I56 [23]
    Waysides[1].createTrack(False, False, False, True, "I57") #I57 [24]
    Waysides[1].createTrack(True, False, True, False, "J58","J59", "YARD") #J58 [25]
    Waysides[1].createTrack(False, False, False, False, "J59") #J59 [26]
    Waysides[1].createTrack(False, False, False, False, "J60") #J60 [27]
    Waysides[1].createTrack(False, False, True, False, "J61") #J61 [28]
    Waysides[1].createTrack(True, False, False, False, "J62","YARD", "J61") #J62 [29]
    Waysides[1].createTrack(False, False, False, False, "K63") #K63 [30]
    Waysides[1].createTrack(False, False, False, False, "K64") #K64 [31]
    Waysides[1].createTrack(False, False, False, True, "K65") #K65 [32]
    Waysides[1].createTrack(False, False, False, False, "K66") #K66 [33]
    Waysides[1].createTrack(False, False, False, False, "K67") #K67 [34]
    Waysides[1].createTrack(False, False, False, False, "K68") #K68 [35]
    Waysides[1].createTrack(False, False, False, False, "L69") #L69 [36]
    Waysides[1].createTrack(False, False, False, False, "L70") #L70 [37]
    Waysides[1].createTrack(False, False, False, False, "L71") #L71 [38]
    Waysides[1].createTrack(False, False, False, False, "L72") #L72 [39]
    Waysides[1].createTrack(False, False, False, True, "L73") #L73 [40]
    Waysides[1].createTrack(False, False, True, False, "YARD") #YARD [41]
    #Wayside 3
    Waysides[2].createTrack(False, False, False, False, "M74") #M74 [0]
    Waysides[2].createTrack(False, False, False, False, "M75") #M75 [1]
    Waysides[2].createTrack(False, False, True, False, "M76") #M76 [2]
    Waysides[2].createTrack(True, False, True, True, "N77", "M76", "R101") #N77 [3]
    Waysides[2].createTrack(False, False, False, False, "N78") #N78 [4]
    Waysides[2].createTrack(False, False, False, False, "N79") #N79 [5]
    Waysides[2].createTrack(False, False, False, False, "N80") #N80 [6]
    Waysides[2].createTrack(False, False, False, False, "N81") #N81 [7]
    Waysides[2].createTrack(False, False, False, False, "N82") #N82 [8]
    Waysides[2].createTrack(False, False, False, False, "N83") #N83 [9]
    Waysides[2].createTrack(False, False, False, False, "N84") #N84 [10]
    Waysides[2].createTrack(True, False, True, False, "N85", "Q100", "O86") #N85 [11]
    Waysides[2].createTrack(False, False, False, False, "O86") #O86 [12]
    Waysides[2].createTrack(False, False, False, False, "O87") #O87 [13]
    Waysides[2].createTrack(False, False, False, True, "O88") #O88 [14]
    Waysides[2].createTrack(False, False, False, False, "P89") #P89 [15]
    Waysides[2].createTrack(False, False, False, False, "P90") #P90 [16]
    Waysides[2].createTrack(False, False, False, False, "P91") #P91 [17]
    Waysides[2].createTrack(False, False, False, False, "P92") #P92 [18]
    Waysides[2].createTrack(False, False, False, False, "P93") #P93 [19]
    Waysides[2].createTrack(False, False, False, False, "P94") #P94 [20]
    Waysides[2].createTrack(False, False, False, False, "P95") #P95 [21]
    Waysides[2].createTrack(False, False, False, True, "P96") #P96 [22]
    Waysides[2].createTrack(False, False, False, False, "P97") #P97 [23]
    Waysides[2].createTrack(False, False, False, False, "Q98") #Q98 [24]
    Waysides[2].createTrack(False, False, False, False, "Q99") #Q99 [25]
    Waysides[2].createTrack(False, False, True, False, "Q100") #Q100 [26]
    Waysides[2].createTrack(False, False, False, False, "R101") #R101 [27]
    #Wayside 4
    Waysides[3].createTrack(False, False, False, False, "S102") #S102 [0]
    Waysides[3].createTrack(False, False, False, False, "S103") #S103 [1]
    Waysides[3].createTrack(False, False, False, False, "S104") #S104 [2]
    Waysides[3].createTrack(False, False, False, True, "T105") #T105 [3]
    Waysides[3].createTrack(False, False, False, False, "T106") #T106 [4]
    Waysides[3].createTrack(False, False, False, False, "T107") #T107 [5]
    Waysides[3].createTrack(False, False, False, False, "T108") #T108 [6]
    Waysides[3].createTrack(False, False, False, False, "T109") #T109 [7]
    Waysides[3].createTrack(False, False, False, False, "U110") #U110 [8]
    Waysides[3].createTrack(False, False, False, False, "U111") #U111 [9]
    Waysides[3].createTrack(False, False, False, False, "U112") #U112 [10]
    Waysides[3].createTrack(False, False, False, False, "U113") #U113 [11]
    Waysides[3].createTrack(False, False, False, True, "U114") #U114 [12]
    Waysides[3].createTrack(False, False, False, False, "U115") #U115 [13]
    Waysides[3].createTrack(False, False, False, False, "U116") #U116 [14]
    Waysides[3].createTrack(False, False, False, False, "V117") #V117 [15]
    Waysides[3].createTrack(False, False, False, False, "V118") #V118 [16]
    Waysides[3].createTrack(False, False, False, False, "V119") #V119 [17]
    Waysides[3].createTrack(False, False, False, False, "V120") #V120 [18]
    Waysides[3].createTrack(False, False, False, False, "V121") #V121 [19]
    Waysides[3].createTrack(False, False, False, False, "W122") #W122 [20]
    Waysides[3].createTrack(False, False, False, True, "W123") #W123 [21]
    Waysides[3].createTrack(False, False, False, False, "W124") #W124 [22]
    Waysides[3].createTrack(False, False, False, False, "W125") #W125 [23]
    Waysides[3].createTrack(False, False, False, False, "W126") #W126 [24]
    Waysides[3].createTrack(False, False, False, False, "W127") #W127 [25]
    Waysides[3].createTrack(False, False, False, False, "W128") #W128 [26]
    Waysides[3].createTrack(False, False, False, False, "W129") #W129 [27]
    Waysides[3].createTrack(False, False, False, False, "W130") #W130 [28]
    Waysides[3].createTrack(False, False, False, False, "W131") #W131 [29]
    Waysides[3].createTrack(False, False, False, True, "W132") #W132 [30]
    Waysides[3].createTrack(False, False, False, False, "W133") #W133 [31]
    Waysides[3].createTrack(False, False, False, False, "W134") #W134 [32]
    Waysides[3].createTrack(False, False, False, False, "W135") #W135 [33]
    Waysides[3].createTrack(False, False, False, False, "W136") #W136 [34]
    Waysides[3].createTrack(False, False, False, False, "W137") #W137 [35]
    Waysides[3].createTrack(False, False, False, False, "W138") #W138 [36]
    Waysides[3].createTrack(False, False, False, False, "W139") #W139 [37]
    Waysides[3].createTrack(False, False, False, False, "W140") #W140 [38]
    Waysides[3].createTrack(False, False, False, True, "W141") #W141 [39]
    Waysides[3].createTrack(False, False, False, False, "W142") #W142 [40]
    Waysides[3].createTrack(False, False, False, False, "W143") #W143 [41]
    Waysides[3].createTrack(False, False, False, False, "X144") #X144 [42]
    Waysides[3].createTrack(False, False, False, False, "X145") #X145 [43]
    Waysides[3].createTrack(False, False, False, False, "X146") #X146 [44]
    Waysides[3].createTrack(False, False, False, False, "Y147") #Y147 [45]
    Waysides[3].createTrack(False, False, False, False, "Y148") #Y148 [46]
    Waysides[3].createTrack(False, False, False, False, "Y149") #Y149 [47]
    
    def __init__(self):
        super().__init__()
        self.init_ui()

        #Buttons/Setup for Automatic Mode
        self.ui.listWidget_3.itemClicked.connect(self.checkListAutomatic)
        self.ui.comboBox.currentIndexChanged.connect(self.checkWaysideSelectionAutomatic)
        self.ui.comboBox_5.currentTextChanged.connect(self.defaultLight)
        self.ui.comboBox_6.currentTextChanged.connect(self.defaultCrossroad)
        self.ui.comboBox_7.currentTextChanged.connect(self.defaultSwitch)

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
        self.ui.comboBox_11.currentTextChanged.connect(self.switchSelection)
        self.ui.comboBox_13.currentIndexChanged.connect(self.checkWaysideSelectionTest)

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
        value = self.ui.comboBox.currentText()
        if value == "Select Wayside":
            for combo_box in [self.ui.comboBox_5, self.ui.comboBox_6, self.ui.comboBox_7, self.ui.listWidget_7, self.ui.listWidget_8]:
                combo_box.setDisabled(True)
        else:
            for combo_box in [self.ui.comboBox_5, self.ui.comboBox_6, self.ui.comboBox_7, self.ui.listWidget_7, self.ui.listWidget_8]:
                combo_box.setEnabled(True)
        self.configureLightsAutomaticGreen(value)
        self.configureCrossroadsAutomaticGreen(value)
        self.configureSwitchAutomaticGreen(value)
    def defaultLight(self):
        text = self.ui.comboBox_5.currentText()
        properText = text.replace("Light ", "") #Get Just track Number and letter into a string
        waysideNumber = self.ui.comboBox.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.Waysides[waysideNumber].amountOfTracks()):
            if(properText == self.Waysides[waysideNumber].getTrackName(i)):
                break
        #operate.changeLight(self.Waysides[waysideNumber].getTrack(i).getLight())
    def defaultCrossroad(self):
        text = self.ui.comboBox_6.currentText()
        properText = text.replace("Crossroad ", "") #Get Just track Number and letter into a string
        waysideNumber = self.ui.comboBox.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.Waysides[waysideNumber].amountOfTracks()):
            if(properText == self.Waysides[waysideNumber].getTrackName(i)):
                break
        #operate.crossroad(self.Waysides[waysideNumber].getTrack(i).getCrossroad())
    def defaultSwitch(self):
        text = self.ui.comboBox_7.currentText()
        properText = text.replace("Light ", "") #Get Just track Number and letter into a string
        waysideNumber = self.ui.comboBox.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.Waysides[waysideNumber].amountOfTracks()):
            if(properText == self.Waysides[waysideNumber].getTrackName(i)):
                break
        #operate.switch(self.Waysides[waysideNumber].getTrack(i).getSwitch())

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
        value = self.ui.comboBox_12.currentText()
        if value == "Select Wayside":
            for combo_box in [self.ui.comboBox_2, self.ui.comboBox_3, self.ui.comboBox_4, self.ui.listWidget_5, self.ui.listWidget_6]:
                combo_box.setDisabled(True)
        else:
            for combo_box in [self.ui.comboBox_2, self.ui.comboBox_3, self.ui.comboBox_4, self.ui.listWidget_5, self.ui.listWidget_6]:
                combo_box.setEnabled(True)
        self.configureLightsManualGreen(value)
        self.configureCrossroadsManualGreen(value)
        self.configureSwitchManualGreen(value)


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
        value = self.ui.comboBox_13.currentText()
        if value == "Select Wayside":
            for combo_box in [self.ui.comboBox_9, self.ui.comboBox_10, self.ui.comboBox_11, self.ui.comboBox_8]:
                combo_box.setDisabled(True)
        else:
            for combo_box in [self.ui.comboBox_9, self.ui.comboBox_10, self.ui.comboBox_11, self.ui.comboBox_8]:
                combo_box.setEnabled(True)
        self.configureLightsTestGreen(value)
        self.configureCrossroadsTestGreen(value)
        self.configureSwitchTestGreen(value)
        self.configureTrackSelectionGreen(value)
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
    def switchSelection(self, item): #Displays proper options for each switch in test bench
        temp = self.ui.listWidget_11.item(0)
        temp.setText("")
        temp = self.ui.listWidget_11.item(1)
        temp.setText("")
        if item == "D13":
            temp = self.ui.listWidget_11.item(0)
            temp.setText("D14->C12")
            temp = self.ui.listWidget_11.item(1)
            temp.setText("A1->D14")
        elif item == "G29":
            temp = self.ui.listWidget_11.item(0)
            temp.setText("F28->G30")
            temp = self.ui.listWidget_11.item(1)
            temp.setText("Z150->F28")
        elif item == "J58":
            temp = self.ui.listWidget_11.item(0)
            temp.setText("I57->YARD")
            temp = self.ui.listWidget_11.item(1)
            temp.setText("I57->J59")
        elif item == "J62":
            temp = self.ui.listWidget_11.item(0)
            temp.setText("J61->K63")
            temp = self.ui.listWidget_11.item(1)
            temp.setText("YARD->K63")
        elif item == "N77":
            temp = self.ui.listWidget_11.item(0)
            temp.setText("N78->R101")
            temp = self.ui.listWidget_11.item(1)
            temp.setText("M76->N78")
        elif item == "N85":
            temp = self.ui.listWidget_11.item(0)
            temp.setText("N84->O86")
            temp = self.ui.listWidget_11.item(1)
            temp.setText("Q100->N84")


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
        for i in range(self.ui.comboBox_5.count(), 0, -1):
            self.ui.comboBox_5.removeItem(i)
        if(currentWayside == "Wayside 1"):
            self.ui.comboBox_5.addItem("Light A1")
            self.ui.comboBox_5.addItem("Light D13")
            self.ui.comboBox_5.addItem("Light G29")
            self.ui.comboBox_5.addItem("Light Z150")
        elif(currentWayside == "Wayside 2"):
            self.ui.comboBox_5.addItem("Light J58")
            self.ui.comboBox_5.addItem("Light J61")
            self.ui.comboBox_5.addItem("Light YARD")
        elif(currentWayside == "Wayside 3"):
            self.ui.comboBox_5.addItem("Light M76")
            self.ui.comboBox_5.addItem("Light N77")
            self.ui.comboBox_5.addItem("Light N85")
            self.ui.comboBox_5.addItem("Light Q100")
    def configureCrossroadsAutomaticGreen(self, currentWayside): #Sets proper crossroads for each wayside selection
        for i in range(self.ui.comboBox_6.count(), 0, -1):
            self.ui.comboBox_6.removeItem(i)
        if(currentWayside == "Wayside 1"):
            self.ui.comboBox_6.addItem("Crossroad E19")
    def configureSwitchAutomaticGreen(self, currentWayside): #Sets proper switches for each wayside selection
        for i in range(self.ui.comboBox_7.count(), 0, -1):
            self.ui.comboBox_7.removeItem(i)
        if(currentWayside == "Wayside 1"):
            self.ui.comboBox_7.addItem("D13")
            self.ui.comboBox_7.addItem("G29")
        elif(currentWayside == "Wayside 2"):
            self.ui.comboBox_7.addItem("J58")
            self.ui.comboBox_7.addItem("J62")
        elif(currentWayside == "Wayside 3"):
            self.ui.comboBox_7.addItem("N77")
            self.ui.comboBox_7.addItem("N85")
        
    
    #Manual Mode
    def configureWaysidesManualGreen(self):
        for i in range(self.ui.comboBox_12.count(), 0, -1):
            self.ui.comboBox_12.removeItem(i)
        self.ui.comboBox_12.addItem("Wayside 1")
        self.ui.comboBox_12.addItem("Wayside 2")
        self.ui.comboBox_12.addItem("Wayside 3")
        self.ui.comboBox_12.addItem("Wayside 4")
    def configureLightsManualGreen(self, currentWayside): #Sets proper lights for each wayside selection
        for i in range(self.ui.comboBox_2.count(), 0, -1):
            self.ui.comboBox_2.removeItem(i)
        if(currentWayside == "Wayside 1"):
            self.ui.comboBox_2.addItem("Light A1")
            self.ui.comboBox_2.addItem("Light D13")
            self.ui.comboBox_2.addItem("Light G29")
            self.ui.comboBox_2.addItem("Light Z150")
        elif(currentWayside == "Wayside 2"):
            self.ui.comboBox_2.addItem("Light J58")
            self.ui.comboBox_2.addItem("Light J61")
            self.ui.comboBox_2.addItem("Light YARD")
        elif(currentWayside == "Wayside 3"):
            self.ui.comboBox_2.addItem("Light M76")
            self.ui.comboBox_2.addItem("Light N77")
            self.ui.comboBox_2.addItem("Light N85")
            self.ui.comboBox_2.addItem("Light Q100")
    def configureCrossroadsManualGreen(self, currentWayside): #Sets proper crossroads for each wayside selection
        for i in range(self.ui.comboBox_3.count(), 0, -1):
            self.ui.comboBox_3.removeItem(i)
    def configureSwitchManualGreen(self, currentWayside): #Sets proper switches for each wayside selection
        for i in range(self.ui.comboBox_4.count(), 0, -1):
            self.ui.comboBox_4.removeItem(i)
        if(currentWayside == "Wayside 1"):
            self.ui.comboBox_4.addItem("D13")
            self.ui.comboBox_4.addItem("G29")
        elif(currentWayside == "Wayside 2"):
            self.ui.comboBox_4.addItem("J58")
            self.ui.comboBox_4.addItem("J62")
        elif(currentWayside == "Wayside 3"):
            self.ui.comboBox_4.addItem("N77")
            self.ui.comboBox_4.addItem("N85")
        

    #Test Bench
    def configureWaysidesTestGreen(self):
        for i in range(self.ui.comboBox_13.count(), 0, -1):
            self.ui.comboBox_13.removeItem(i)
        self.ui.comboBox_13.addItem("Wayside 1")
        self.ui.comboBox_13.addItem("Wayside 2")
        self.ui.comboBox_13.addItem("Wayside 3")
        self.ui.comboBox_13.addItem("Wayside 4")
    def configureLightsTestGreen(self, currentWayside): #Sets proper lights for each wayside selection
        for i in range(self.ui.comboBox_9.count(), 0, -1):
            self.ui.comboBox_9.removeItem(i)
        if(currentWayside == "Wayside 1"):
            self.ui.comboBox_9.addItem("Light A1")
            self.ui.comboBox_9.addItem("Light D13")
            self.ui.comboBox_9.addItem("Light G29")
            self.ui.comboBox_9.addItem("Light Z150")
        elif(currentWayside == "Wayside 2"):
            self.ui.comboBox_9.addItem("Light J58")
            self.ui.comboBox_9.addItem("Light J61")
            self.ui.comboBox_9.addItem("Light YARD")
        elif(currentWayside == "Wayside 3"):
            self.ui.comboBox_9.addItem("Light M76")
            self.ui.comboBox_9.addItem("Light N77")
            self.ui.comboBox_9.addItem("Light N85")
            self.ui.comboBox_9.addItem("Light Q100")
    def configureCrossroadsTestGreen(self, currentWayside): #Sets proper crossroads for each wayside selection
        for i in range(self.ui.comboBox_10.count(), 0, -1):
            self.ui.comboBox_10.removeItem(i)
    def configureSwitchTestGreen(self, currentWayside): #Sets proper switches for each wayside selection
        for i in range(self.ui.comboBox_11.count(), 0, -1):
            self.ui.comboBox_11.removeItem(i)
        if(currentWayside == "Wayside 1"):
            self.ui.comboBox_11.addItem("D13")
            self.ui.comboBox_11.addItem("G29")
        elif(currentWayside == "Wayside 2"):
            self.ui.comboBox_11.addItem("J58")
            self.ui.comboBox_11.addItem("J62")
        elif(currentWayside == "Wayside 3"):
            self.ui.comboBox_11.addItem("N77")
            self.ui.comboBox_11.addItem("N85")
    def configureTrackSelectionGreen(self, currentWayside):
        for i in range(self.ui.comboBox_8.count(), 0, -1):
            self.ui.comboBox_8.removeItem(i)
        if(currentWayside == "Wayside 1"):
            for i in range(self.Waysides[0].amountOfTracks()):
                self.ui.comboBox_8.addItem(self.Waysides[0].getTrackName(i))
        elif(currentWayside == "Wayside 2"):
            for i in range(self.Waysides[1].amountOfTracks()):
                self.ui.comboBox_8.addItem(self.Waysides[1].getTrackName(i))
        elif(currentWayside == "Wayside 3"):
            for i in range(self.Waysides[2].amountOfTracks()):
                self.ui.comboBox_8.addItem(self.Waysides[2].getTrackName(i))
        elif(currentWayside == "Wayside 4"):
            for i in range(self.Waysides[3].amountOfTracks()):
                self.ui.comboBox_8.addItem(self.Waysides[3].getTrackName(i))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HWTrackControllerGUI()
    window.show()
    sys.exit(app.exec())
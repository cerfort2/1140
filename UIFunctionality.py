import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow, QFileDialog
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets
from HWTrackDisplay import Ui_MainWindow
from TrackClass import Track
from UI_Breadboard_Class import Operations
from GreenLineWaysides import GreenLine

operate = Operations() #Class to perform operations on the breadboard

class HWTrackControllerGUI(QMainWindow):
    
    greenLine = GreenLine()
    pureOccupancy = []
    yardSwitchAuthority = int
    route = []
    suggestedSpeed = int

    greenLine.Waysides[0].getTrack(12).setOccupancy(True) 
    greenLine.Waysides[0].getTrack(13).setOccupancy(True) 
    greenLine.Waysides[0].getTrack(14).setOccupancy(True)
    greenLine.Waysides[0].getTrack(15).setOccupancy(True) 

    greenLine.Waysides[1].getTrack(0).setOccupancy(True) 
    greenLine.Waysides[1].getTrack(1).setOccupancy(True) 
    greenLine.Waysides[1].getTrack(2).setOccupancy(True) 
    greenLine.Waysides[1].getTrack(3).setOccupancy(True) 
    greenLine.Waysides[1].getTrack(18).setOccupancy(True) 
    greenLine.Waysides[1].getTrack(19).setOccupancy(True) 
    greenLine.Waysides[1].getTrack(20).setOccupancy(True) 
    greenLine.Waysides[1].getTrack(21).setOccupancy(True) 

    for i in range(4):
        for j in range(greenLine.Waysides[i].amountOfTracks()):
            print(j)
            pureOccupancy.append(greenLine.Waysides[i].getTrack(j).getOccupancy())
            print(greenLine.Waysides[i].getTrack(j).getOccupancy())

    #Testing for functionality
    greenLine.Waysides[0].getTrack(32).setLight(False) #Z150 Red
    greenLine.Waysides[2].getTrack(26).setLight(False) #Q100 Red
    greenLine.Waysides[0].getTrack(18).setCrossroad(True) #E19 Crossroad Down


    greenLine.Waysides[1].getTrack(25).setSwitch(False)
    greenLine.Waysides[2].getTrack(11).setSwitch(False)

    def __init__(self):
        super().__init__()
        self.init_ui()

        #Buttons/Setup for Automatic Mode
        self.ui.listWidget_3.itemClicked.connect(self.checkListAutomatic)
        self.ui.comboBox.currentIndexChanged.connect(self.checkWaysideSelectionAutomatic)
        self.ui.comboBox_5.currentTextChanged.connect(self.defaultLight)
        self.ui.comboBox_6.currentTextChanged.connect(self.defaultCrossroad)
        self.ui.comboBox_7.currentTextChanged.connect(self.defaultSwitch)

        #Temp need to implement timer for this
        self.ui.comboBox.currentIndexChanged.connect(self.setListsOccupancyAutomatic)
        self.ui.comboBox.currentIndexChanged.connect(self.setListsFailureAutomatic)

        #Buttons/Setup for Manual Mode
        self.ui.listWidget.itemClicked.connect(self.checkListManual)
        self.ui.comboBox_2.currentIndexChanged.connect(self.lightChangeManual)
        self.ui.comboBox_3.currentIndexChanged.connect(self.crossChangeManual)
        self.ui.comboBox_12.currentIndexChanged.connect(self.checkWaysideSelectionManual)
        self.ui.comboBox_4.currentIndexChanged.connect(self.switchChangeManual)
        red = self.ui.listWidget_2
        self.ui.listWidget_2.itemClicked.connect(lambda item=red: self.editLight(item.text()))
        self.ui.comboBox_2.currentTextChanged.connect(self.defaultLightManual)
        self.ui.pushButton.clicked.connect(self.editCrossroad)
        self.ui.comboBox_3.currentTextChanged.connect(self.defaultCrossroadManual)
        self.ui.pushButton_2.clicked.connect(self.editSwitch)
        self.ui.comboBox_4.currentTextChanged.connect(self.defaultSwitchManual)

        #Temp need to implement timer for this
        self.ui.comboBox_12.currentIndexChanged.connect(self.setListsOccupancyManual)
        self.ui.comboBox_12.currentIndexChanged.connect(self.setListsFailureManual)

        #Stuff to be changed
        """
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
        redTest = self.ui.listWidget_4
        self.ui.listWidget_4.itemClicked.connect(lambda item=redTest: self.editLightTest(item.text()))
        cross = self.ui.listWidget_10
        self.ui.listWidget_10.itemClicked.connect(lambda item=cross: self.editCrossroadTest(item.text()))
        self.ui.listWidget_11.currentRowChanged.connect(self.editSwitchTest)
        self.ui.pushButton_4.clicked.connect(self.toggleTrack)
        self.ui.pushButton_5.clicked.connect(self.toggleFailure)

        #Buttons/Setup for Whole UI
        self.ui.pushButton_3.clicked.connect(self.openArduinoFile) #Opens PLC File
        
        
        self.ui.comboBox.currentIndexChanged.connect(lambda: operate.plcCode(self.pureOccupancy))

    def init_ui(self): #SetupUI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    #Time dependent Functions
    def sendData(self): #Data of track to be sent to CTC and Track Model
        data = [[],[],[]]
        blocks:Track = []
        for i in range (len(self.greenLine.Waysides)):
            for j in range (len(self.greenLine.Waysides[i].tracks)):
                blocks.append(self.greenLine.Waysides[i].tracks[j])

        for i in range (len(blocks)):
            for j in range (i, len(blocks)):
                if(blocks[i].getName() > blocks[j].getName()):
                    hold = blocks[i]
                    blocks[i] = blocks[j]
                    blocks[j] = hold

        for i in range (len(blocks)):
            if(blocks[i].getIsSwitch()):
                data[0].append(blocks[i].getSwitch())
            else:
                data[0].append(False)
            if(blocks[i].getIsCrossroad()):
                data[1].append(blocks[i].getCrossroad())
            else:
                data[1].append(False)
            if(blocks[i].getIsLight()):
                data[2].append(blocks[i].getLight())
            else:
                data[2].append(False) 
        return data
    def sendOccupancy(self): #Occupancy sent to CTC
        return self.pureOccupancy
    def getOccupancy(self, occupancy:[]): #Current Occupancy from Track Model
        self.pureOccupancy = occupancy
        #All for Wayside 1
        for i in range(31): #A1-G32
            self.greenLine.Waysides[0].getTrack(i).setOccupancy(occupancy[i])
        self.greenLine.Waysides[0].getTrack(32).setOccupancy(occupancy[len(occupancy)-2]) #Z150
        #All for Wayside 2
        for i in range(40): #H33-L73
            self.greenLine.Waysides[1].getTrack(i).setOccupancy(occupancy[i+32])
        self.greenLine.Waysides[1].getTrack(41).setOccupancy(occupancy[len(occupancy)-1]) #Z151/YARD
        #All for Wayside 3
        for i in range(27): #M74-R101
            self.greenLine.Waysides[2].getTrack(i).setOccupancy(occupancy[i+73])
        #All for Wayside 4
        for i in range(47): #S102-Y149
            self.greenLine.Waysides[3].getTrack(i).setOccupancy(occupancy[i+101])
    def getRoute(self, route): #Route from the CTC
        self.route = route
    def sendRoute(self): #Route sent to Track Model
        return self.route
    def sendFailures(self): #Failures sent to CTC
        failures = []
        for i in range(len(self.greenLine.Waysides)):
            for j in range(len(self.greenLine.Waysides[i])):
                failures.append(self.greenLine.Waysides[i].getTrack(j).getFailure())
        return failures
    def sendSpeed(self): #Speed sent to Track Model
        return self.suggestedSpeed
    def getSpeed(self, speed): #Speed from CTC
        self.suggestedSpeed = speed

    #Authority functions
    def getInitAuthority(self, auth):
        self.yardSwitchAuthority = auth
    def editAuthority(self):
        return
    def sendAuthority(self):
        return



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
        if text == "Select Light":
            return
        properText = text.replace("Light ", "") #Get Just track Number and letter into a string
        waysideNumber = self.ui.comboBox.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(properText == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        operate.changeLight(self.greenLine.Waysides[waysideNumber].getTrack(i).getLight())
    def defaultCrossroad(self):
        text = self.ui.comboBox_6.currentText()
        if text == "Select Crossroad":
            return
        properText = text.replace("Crossroad ", "") #Get Just track Number and letter into a string
        waysideNumber = self.ui.comboBox.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(properText == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        operate.crossroad(self.greenLine.Waysides[waysideNumber].getTrack(i).getCrossroad())
    def defaultSwitch(self):
        text = self.ui.comboBox_7.currentText()
        if text == "Select Switch":
            return
        waysideNumber = self.ui.comboBox.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(text == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        trackStatus = self.greenLine.Waysides[waysideNumber].getTrack(i).getSwitch()
        if trackStatus == True: #Right
            operate.switch(self.greenLine.Waysides[waysideNumber].getTrackName(i), self.greenLine.Waysides[waysideNumber].getTrack(i).getRightDest(), trackStatus)
        elif trackStatus == False: #Left
            operate.switch(self.greenLine.Waysides[waysideNumber].getTrackName(i), self.greenLine.Waysides[waysideNumber].getTrack(i).getLeftDest(), trackStatus)
    def setListsOccupancyAutomatic(self): #Shows occupancy on the lists for displaying
        waysideNumber = self.ui.comboBox.currentIndex()-1 #Gets the current wayside selected
        self.ui.listWidget_7.clear()
        for j in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if self.greenLine.Waysides[waysideNumber].getTrack(j).getOccupancy() == True:
                self.ui.listWidget_7.addItem(self.greenLine.Waysides[waysideNumber].getTrackName(j))
    def setListsFailureAutomatic(self): #Shows failures on the list for displaying
        waysideNumber = self.ui.comboBox.currentIndex()-1 #Gets the current wayside selected
        self.ui.listWidget_8.clear()
        for j in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if self.greenLine.Waysides[waysideNumber].getTrack(j).getFailure() == True:
                self.ui.listWidget_8.addItem(self.greenLine.Waysides[waysideNumber].getTrackName(j))


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
    def editLight(self, text): #Edits the light when selection made on UI in manual and updates track
        light = self.ui.comboBox_2.currentText()
        if light == "Select Light":
            return
        properText = light.replace("Light ", "") #Get Just track Number and letter into a string
        waysideNumber = self.ui.comboBox_12.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(properText == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        if text == "Red":
            color = True
        elif text == "Green":
            color = False
        self.greenLine.Waysides[waysideNumber].getTrack(i).setLight(color)
        operate.changeLight(self.greenLine.Waysides[waysideNumber].getTrack(i).getLight())
    def editCrossroad(self): #Edits crossroad when toggle switch pressed
        text = self.ui.comboBox_3.currentText()
        if text == "Select Crossroad":
            return
        properText = text.replace("Crossroad ", "") #Get Just track Number and letter into a string
        waysideNumber = self.ui.comboBox_12.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(properText == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        newVal = not self.greenLine.Waysides[waysideNumber].getTrack(i).getCrossroad() #Toggling the current value
        self.greenLine.Waysides[waysideNumber].getTrack(i).setCrossroad(newVal) #Setting it to the track it is associated with
        operate.crossroad(self.greenLine.Waysides[waysideNumber].getTrack(i).getCrossroad())
    def editSwitch(self): #Edits switch data when toggle switch is pressed
        text = self.ui.comboBox_4.currentText()
        if text == "Select Crossroad":
            return
        waysideNumber = self.ui.comboBox_12.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(text == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        newVal = not self.greenLine.Waysides[waysideNumber].getTrack(i).getSwitch() #Toggling the current value
        self.greenLine.Waysides[waysideNumber].getTrack(i).setSwitch(newVal) #Setting it to the track it is associated with
        trackStatus = self.greenLine.Waysides[waysideNumber].getTrack(i).getSwitch()
        if trackStatus == True: #Right
            operate.switch(self.greenLine.Waysides[waysideNumber].getTrackName(i), self.greenLine.Waysides[waysideNumber].getTrack(i).getRightDest(), trackStatus)
        elif trackStatus == False: #Left
            operate.switch(self.greenLine.Waysides[waysideNumber].getTrackName(i), self.greenLine.Waysides[waysideNumber].getTrack(i).getLeftDest(), trackStatus)
    def defaultLightManual(self): #Displaying default value of light
        text = self.ui.comboBox_2.currentText()
        if text == "Select Light":
            return
        properText = text.replace("Light ", "") #Get Just track Number and letter into a string
        waysideNumber = self.ui.comboBox_12.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(properText == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        operate.changeLight(self.greenLine.Waysides[waysideNumber].getTrack(i).getLight())
    def defaultCrossroadManual(self): #Displaying default value of Crossroad
        text = self.ui.comboBox_3.currentText()
        if text == "Select Crossroad":
            return
        properText = text.replace("Crossroad ", "") #Get Just track Number and letter into a string
        waysideNumber = self.ui.comboBox_12.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(properText == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        operate.crossroad(self.greenLine.Waysides[waysideNumber].getTrack(i).getCrossroad())
    def defaultSwitchManual(self): #Displaying default value of switch
        text = self.ui.comboBox_4.currentText()
        if text == "Select Switch":
            return
        waysideNumber = self.ui.comboBox_12.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(text == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        trackStatus = self.greenLine.Waysides[waysideNumber].getTrack(i).getSwitch()
        if trackStatus == True: #Right
            operate.switch(self.greenLine.Waysides[waysideNumber].getTrackName(i), self.greenLine.Waysides[waysideNumber].getTrack(i).getRightDest(), trackStatus)
        elif trackStatus == False: #Left
            operate.switch(self.greenLine.Waysides[waysideNumber].getTrackName(i), self.greenLine.Waysides[waysideNumber].getTrack(i).getLeftDest(), trackStatus)
    def setListsOccupancyManual(self): #Shows occupancy on the lists for displaying
        waysideNumber = self.ui.comboBox_12.currentIndex()-1 #Gets the current wayside selected
        self.ui.listWidget_5.clear()
        for j in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if self.greenLine.Waysides[waysideNumber].getTrack(j).getOccupancy() == True:
                self.ui.listWidget_5.addItem(self.greenLine.Waysides[waysideNumber].getTrackName(j))
    def setListsFailureManual(self): #Shows failures on the list for displaying
        waysideNumber = self.ui.comboBox_12.currentIndex()-1 #Gets the current wayside selected
        self.ui.listWidget_6.clear()
        for j in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if self.greenLine.Waysides[waysideNumber].getTrack(j).getFailure() == True:
                self.ui.listWidget_6.addItem(self.greenLine.Waysides[waysideNumber].getTrackName(j))


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
    def editLightTest(self, text):
        light = self.ui.comboBox_9.currentText()
        if light == "Select Light":
            return
        properText = light.replace("Light ", "") #Get Just track Number and letter into a string
        waysideNumber = self.ui.comboBox_13.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(properText == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        if text == "Red":
            color = True
        elif text == "Green":
            color = False
        self.greenLine.Waysides[waysideNumber].getTrack(i).setLight(color)
    def editCrossroadTest(self, current):
        text = self.ui.comboBox_10.currentText()
        if text == "Select Crossroad":
            return
        properText = text.replace("Crossroad ", "") #Get Just track Number and letter into a string
        waysideNumber = self.ui.comboBox_13.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(properText == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        if current == "On":
            self.greenLine.Waysides[waysideNumber].getTrack(i).setCrossroad(True)
        elif current == "Off":
            self.greenLine.Waysides[waysideNumber].getTrack(i).setCrossroad(False)
        print(self.greenLine.Waysides[waysideNumber].getTrack(i).getCrossroad())
    def editSwitchTest(self, current_row):
        text = self.ui.comboBox_11.currentText()
        if text == "Select Switch":
            return
        waysideNumber = self.ui.comboBox_13.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(text == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        index = current_row
        if index == 1: #Right
            self.greenLine.Waysides[waysideNumber].getTrack(i).setSwitch(True) #Setting it to the track it is associated with
        elif index == 0: #Left
            self.greenLine.Waysides[waysideNumber].getTrack(i).setSwitch(False) #Setting it to the track it is associated with
    def toggleTrack(self):
        text = self.ui.comboBox_8.currentText()
        if text == "Track Selection":
            return
        waysideNumber = self.ui.comboBox_13.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(text == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        newVal = not self.greenLine.Waysides[waysideNumber].getTrack(i).getOccupancy() #Toggling the current value
        self.greenLine.Waysides[waysideNumber].getTrack(i).setOccupancy(newVal) #Setting it to the track it is associated with
    def toggleFailure(self):
        text = self.ui.comboBox_8.currentText()
        if text == "Track Selection":
            return
        waysideNumber = self.ui.comboBox_13.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(text == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        newVal = not self.greenLine.Waysides[waysideNumber].getTrack(i).getFailure() #Toggling the current value
        self.greenLine.Waysides[waysideNumber].getTrack(i).setFailure(newVal) #Setting it to the track it is associated with


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
        self.ui.comboBox_5.setCurrentIndex(0)
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
        self.ui.comboBox_6.setCurrentIndex(0)
        for i in range(self.ui.comboBox_6.count(), 0, -1):
            self.ui.comboBox_6.removeItem(i)
        if(currentWayside == "Wayside 1"):
            self.ui.comboBox_6.addItem("Crossroad E19")
    def configureSwitchAutomaticGreen(self, currentWayside): #Sets proper switches for each wayside selection
        self.ui.comboBox_7.setCurrentIndex(0)
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
        self.ui.comboBox_2.setCurrentIndex(0)
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
        self.ui.comboBox_3.setCurrentIndex(0)
        for i in range(self.ui.comboBox_3.count(), 0, -1):
            self.ui.comboBox_3.removeItem(i)
        if(currentWayside == "Wayside 1"):
            self.ui.comboBox_3.addItem("Crossroad E19")
    def configureSwitchManualGreen(self, currentWayside): #Sets proper switches for each wayside selection
        self.ui.comboBox_4.setCurrentIndex(0)
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
        self.ui.comboBox_9.setCurrentIndex(0)
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
        self.ui.comboBox_10.setCurrentIndex(0)
        for i in range(self.ui.comboBox_10.count(), 0, -1):
            self.ui.comboBox_10.removeItem(i)
        if(currentWayside == "Wayside 1"):
            self.ui.comboBox_10.addItem("Crossroad E19")
    def configureSwitchTestGreen(self, currentWayside): #Sets proper switches for each wayside selection
        self.ui.comboBox_11.setCurrentIndex(0)
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
        self.ui.comboBox_8.setCurrentIndex(0)
        for i in range(self.ui.comboBox_8.count(), 0, -1):
            self.ui.comboBox_8.removeItem(i)
        if(currentWayside == "Wayside 1"):
            for i in range(self.greenLine.Waysides[0].amountOfTracks()):
                self.ui.comboBox_8.addItem(self.greenLine.Waysides[0].getTrackName(i))
        elif(currentWayside == "Wayside 2"):
            for i in range(self.greenLine.Waysides[1].amountOfTracks()):
                self.ui.comboBox_8.addItem(self.greenLine.Waysides[1].getTrackName(i))
        elif(currentWayside == "Wayside 3"):
            for i in range(self.greenLine.Waysides[2].amountOfTracks()):
                self.ui.comboBox_8.addItem(self.greenLine.Waysides[2].getTrackName(i))
        elif(currentWayside == "Wayside 4"):
            for i in range(self.greenLine.Waysides[3].amountOfTracks()):
                self.ui.comboBox_8.addItem(self.greenLine.Waysides[3].getTrackName(i))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HWTrackControllerGUI()
    window.show()
    sys.exit(app.exec())
import sys
import subprocess
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow, QFileDialog
from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6 import QtCore, QtGui, QtWidgets
from Hardware_Track_Controller.HWTrackUI import Ui_Form
from Hardware_Track_Controller.TrackClass import Track
#from Hardware_Track_Controller.UI_Breadboard_Class import Operations
from Hardware_Track_Controller.GreenLineWaysides import GreenLine
from Hardware_Track_Controller.RedLineWaysides import RedLine

#operate = Operations() #Class to perform operations on the breadboard

class HWTrackControllerGUI(Ui_Form, QObject):
    
    #Signals sent out
    CTCOccupancy = pyqtSignal(list)
    CTCTrackFailures = pyqtSignal(list)
    trackModelSendRoute = pyqtSignal(list)
    trackModelSuggestedSpeed = pyqtSignal(list)
    trackModelTrackData = pyqtSignal(list)
    trackModelAuthority = pyqtSignal(list)
    trackModelStoppedTrains = pyqtSignal(list)
    trackModelFixes = pyqtSignal(str)
    trackModelClose = pyqtSignal(str)

    #Global Variables
    greenLine = GreenLine()
    redLine = RedLine()
    pureOccupancy = []
    oldOccupancy = []
    firstRun = True

    def connectFunctions(self):
        #Buttons/Setup for Automatic Mode
        self.listWidget_3.itemClicked.connect(self.checkListAutomatic)
        self.comboBox.currentIndexChanged.connect(self.checkWaysideSelectionAutomatic)
        self.comboBox_5.currentTextChanged.connect(self.defaultLight)
        self.comboBox_6.currentTextChanged.connect(self.defaultCrossroad)
        self.comboBox_7.currentTextChanged.connect(self.defaultSwitch)

        #Comment this out for when the system is fully integrated
        self.comboBox.currentIndexChanged.connect(self.setListsOccupancyAutomatic)
        self.comboBox.currentIndexChanged.connect(self.setListsFailureAutomatic)

        #Buttons/Setup for Manual Mode
        self.listWidget.itemClicked.connect(self.checkListManual)
        self.comboBox_2.currentIndexChanged.connect(self.lightChangeManual)
        self.comboBox_3.currentIndexChanged.connect(self.crossChangeManual)
        self.comboBox_12.currentIndexChanged.connect(self.checkWaysideSelectionManual)
        self.comboBox_4.currentIndexChanged.connect(self.switchChangeManual)
        red = self.listWidget_2
        self.listWidget_2.itemClicked.connect(lambda item=red: self.editLight(item.text()))
        self.comboBox_2.currentTextChanged.connect(self.defaultLightManual)
        self.pushButton.clicked.connect(self.editCrossroad)
        self.comboBox_3.currentTextChanged.connect(self.defaultCrossroadManual)
        self.pushButton_2.clicked.connect(self.editSwitch)
        self.comboBox_4.currentTextChanged.connect(self.defaultSwitchManual)

        #Comment this out for when the system is fully integrated
        self.comboBox_12.currentIndexChanged.connect(self.setListsOccupancyManual)
        self.comboBox_12.currentIndexChanged.connect(self.setListsFailureManual)

        #Buttons/Setup for Test Bench - No longer in use at this point
        self.tabWidget.removeTab(2)
        # self.listWidget_9.itemClicked.connect(self.checkListTest)
        # self.comboBox_8.currentIndexChanged.connect(self.trackChangeTest)
        # self.comboBox_9.currentIndexChanged.connect(self.lightChangeTest)
        # self.comboBox_10.currentIndexChanged.connect(self.crossChangeTest)
        # self.comboBox_11.currentIndexChanged.connect(self.switchChangeTest)
        # self.comboBox_11.currentTextChanged.connect(self.switchSelection)
        # self.comboBox_13.currentIndexChanged.connect(self.checkWaysideSelectionTest)
        # redTest = self.listWidget_4
        # self.listWidget_4.itemClicked.connect(lambda item=redTest: self.editLightTest(item.text()))
        # cross = self.listWidget_10
        # self.listWidget_10.itemClicked.connect(lambda item=cross: self.editCrossroadTest(item.text()))
        # self.listWidget_11.currentRowChanged.connect(self.editSwitchTest)
        # self.pushButton_4.clicked.connect(self.toggleTrack)
        # self.pushButton_5.clicked.connect(self.toggleFailure)

        #Buttons/Setup for Whole UI
        self.pushButton_3.clicked.connect(self.openArduinoFile) #Opens PLC File

    def __init__(self): #Initalizer
        super().__init__()
    
    #Getting data functions
    def getOccupancy(self, occupancy:[]): #Current Occupancy from Track Model
        self.pureOccupancy = occupancy
        if(len(occupancy) == 151):
            #All for Wayside 1
            for i in range(32): #A1-G32
                self.greenLine.Waysides[0].getTrack(i).setOccupancy(occupancy[i])
            self.greenLine.Waysides[0].getTrack(32).setOccupancy(occupancy[len(occupancy)-2]) #Z150
            #All for Wayside 2
            for i in range(41): #H33-L73
                self.greenLine.Waysides[1].getTrack(i).setOccupancy(occupancy[i+32])
            self.greenLine.Waysides[1].getTrack(41).setOccupancy(occupancy[len(occupancy)-1]) #Z151/YARD
            #All for Wayside 3
            for i in range(28): #M74-R101
                self.greenLine.Waysides[2].getTrack(i).setOccupancy(occupancy[i+73])
            #All for Wayside 4
            for i in range(48): #S102-Y149
                self.greenLine.Waysides[3].getTrack(i).setOccupancy(occupancy[i+101])
            
            check = False #Checking if the new input has changed occupancy or not
            if(self.firstRun == False):
                for i in range(len(occupancy)):
                    if(self.pureOccupancy[i] != self.oldOccupancy[i]):
                        check = True

            #Runs the functions accordingly after recieving new occupancies
            if(self.tabWidget.currentIndex() == 0):
                if(check):
                    newStates = operate.plcCode(occupancy) #Everytime get new occupancy run plc logic in arduino
                    self.setNewDataGreenLine(newStates)
                self.setListsOccupancyAutomatic()
                self.setListsOccupancyManual()
            elif(self.tabWidget.currentIndex() == 1):
                self.setListsOccupancyAutomatic()
                self.setListsOccupancyManual()

            self.sendStopGreen(occupancy) #Runs the light stop logic each time new occupancy given
            self.oldOccupancy = occupancy
            self.sendOccupancy()
            self.firstRun = False
        else:
            for i in range(len(occupancy)):
                    self.redLine.Waysides[0].getTrack(i).setOccupancy(occupancy[i])
            #Runs the functions accordingly after recieving new occupancies
            if(self.tabWidget.currentIndex() == 0):
                self.redLinePLCLogic()
                self.setListsOccupancyAutomatic()
                self.setListsOccupancyManual()
            elif(self.tabWidget.currentIndex() == 1):
                self.setListsOccupancyAutomatic()
                self.setListsOccupancyManual()
            self.sendStopRed()
            self.sendOccupancy()
            self.oldOccupancy = occupancy
            self.firstRun = False
    def createNewTrainData(self, traveling, Auth, speed): #Created by CTC
        self.trackModelAuthority.emit(Auth)
        self.trackModelSuggestedSpeed.emit(speed)
        self.trackModelSendRoute.emit(traveling)
    def getFailure(self, fails): #Failures send to CTC from Track Model
        if(len(self.pureOccupancy) == 151):
            for i in range(32): #A1-G32
                self.greenLine.Waysides[0].getTrack(i).setFailure([i])
            self.greenLine.Waysides[0].getTrack(32).setFailure(fails[len(fails)-2]) #Z150
            #All for Wayside 2
            for i in range(41): #H33-L73
                self.greenLine.Waysides[1].getTrack(i).setFailure(fails[i+32])
            self.greenLine.Waysides[1].getTrack(41).setFailure(fails[len(fails)-1]) #Z151/YARD
            #All for Wayside 3
            for i in range(28): #M74-R101
                self.greenLine.Waysides[2].getTrack(i).setFailure(fails[i+73])
            #All for Wayside 4
            for i in range(48): #S102-Y149
                self.greenLine.Waysides[3].getTrack(i).setFailure(fails[i+101])
        else:
            for i in range(len(fails)):
                self.redLine.Waysides[0].getTrack(i).setFailure(fails[i])
        self.CTCTrackFailures.emit(fails)
    

    #Sending out functions
    def sendData(self): #Data of track to be sent to CTC and Track Model
        data = [[],[],[]]
        if(len(self.pureOccupancy) == 151):
            blocks = []
            for i in range (len(self.greenLine.Waysides)):
                for j in range (self.greenLine.Waysides[i].amountOfTracks()):
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
        else:
            blocks:Track = []
            for i in range (len(self.redLine.Waysides)):
                for j in range (len(self.redLine.Waysides[i].tracks)):
                    blocks.append(self.redLine.Waysides[i].tracks[j])
            
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
        self.trackModelTrackData.emit(data)
    def sendOccupancy(self): #Occupancy sent to CTC
        self.CTCOccupancy.emit(self.pureOccupancy)
    def fix(self, fixers): #Fix the tracks
        self.trackModelFixes.emit(fixers)
    def close(self, closers): #Close the tracks
        self.trackModelClose.emit(closers)
    def changeSwitch(self, name, value):
        if(len(self.pureOccupancy) == 151):
            #All for Wayside 1
            for i in range(32): #A1-G32
                if(self.greenLine.Waysides[0].getTrack(i).getName() == name):
                    self.greenLine.Waysides[0].getTrack(i).setSwitch(value)
                    return
            if(self.greenLine.Waysides[0].getTrack(32).getName() == name):
                self.greenLine.Waysides[0].getTrack(32).setSwitch(value) #Z150
                return

            #All for Wayside 2
            for i in range(41): #H33-L73
                if(self.greenLine.Waysides[1].getTrack(i).getName() == name):
                    self.greenLine.Waysides[1].getTrack(i).setSwitch(value)
                    return
            if(self.greenLine.Waysides[1].getTrack(41).getName() == name):
                self.greenLine.Waysides[1].getTrack(41).setSwitch(value) #Z151/YARD
                return
            
            #All for Wayside 3
            for i in range(28): #M74-R101
                if(self.greenLine.Waysides[2].getTrack(i).getName() == name):
                    self.greenLine.Waysides[2].getTrack(i).setSwitch(value)
                    return
            #All for Wayside 4
            for i in range(48): #S102-Y149
                if(self.greenLine.Waysides[3].getTrack(i).getName() == name):
                    self.greenLine.Waysides[3].getTrack(i).setSwitch(value)
                    return
        else:
            for i in range(self.redLine.Waysides[0].amountOfTracks()):
                if(self.redLine.Waysides[0].getTrack(i).getName() == name):
                    self.redLine.Waysides[0].getTrack(i).setSwitch(value)
                    return

    #Functions for setting data/PLC Logic
    def setNewDataGreenLine(self, states):
        self.greenLine.Waysides[1].getTrack(29).setSwitch(states[0][0])
        self.greenLine.Waysides[2].getTrack(3).setSwitch(states[0][1])
        self.greenLine.Waysides[2].getTrack(11).setSwitch(states[0][2])
        self.greenLine.Waysides[0].getTrack(28).setSwitch(states[0][3])
        self.greenLine.Waysides[0].getTrack(12).setSwitch(states[0][4])
        #self.greenLine.Waysides[1].getTrack(25).setSwitch(states[0][5])

        self.greenLine.Waysides[1].getTrack(41).setLight(states[1][0])
        self.greenLine.Waysides[1].getTrack(28).setLight(states[1][1])
        self.greenLine.Waysides[2].getTrack(2).setLight(states[1][2])
        self.greenLine.Waysides[2].getTrack(3).setLight(states[1][3])
        self.greenLine.Waysides[2].getTrack(11).setLight(states[1][4])
        self.greenLine.Waysides[2].getTrack(26).setLight(states[1][5])
        self.greenLine.Waysides[0].getTrack(32).setLight(states[1][6])
        self.greenLine.Waysides[0].getTrack(28).setLight(states[1][7])
        self.greenLine.Waysides[0].getTrack(12).setLight(states[1][8])
        self.greenLine.Waysides[0].getTrack(0).setLight(states[1][9])
        #self.greenLine.Waysides[1].getTrack(25).setLight(states[1][10])

        #Do switch 6 logic here
        if(self.greenLine.Waysides[1].getTrack(24).getOccupancy() == True):
            self.greenLine.Waysides[1].getTrack(25).setSwitch(False)
        
        #Crossroad logic
        if(self.greenLine.Waysides[0].getTrack(16).getOccupancy() or self.greenLine.Waysides[0].getTrack(17).getOccupancy() or self.greenLine.Waysides[0].getTrack(18).getOccupancy() or self.greenLine.Waysides[0].getTrack(19).getOccupancy() or self.greenLine.Waysides[0].getTrack(20).getOccupancy()):
            self.greenLine.Waysides[0].getTrack(18).setCrossroad(True)
        else:
            self.greenLine.Waysides[0].getTrack(18).setCrossroad(False)
    def redLinePLCLogic(self): #Red line logic
        loop1 = False
        loop2 = False
        leg = False
        for i in range(0, 16):
            loop1 = loop1 or self.redLine.Waysides[0].getTrack(i).getOccupancy()
        for i in range(43, 67):
            loop2 = loop2 or self.redLine.Waysides[0].getTrack(i).getOccupancy()
        for i in range(32, 38):
            leg = leg or self.redLine.Waysides[0].getTrack(i).getOccupancy()


        #Switch C10 - YARD(T77) , C10 - D11
        if((True) or self.redLine.Waysides[0].getTrack(76).getOccupancy()):
            self.redLine.Waysides[0].getTrack(9).setSwitch(False)
        if(not (True) or self.redLine.Waysides[0].getTrack(10).getOccupancy()):
            self.redLine.Waysides[0].getTrack(9).setSwitch(True)
        #Signal C10
        if(self.redLine.Waysides[0].getTrack(9).getOccupancy()):
            self.redLine.Waysides[0].getTrack(9).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(9).setLight(True)
        #Signal D11
        if(self.redLine.Waysides[0].getTrack(10).getOccupancy()):
            self.redLine.Waysides[0].getTrack(10).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(10).setLight(True)
        #Signal Yard
        if(not loop1 and self.redLine.Waysides[0].getTrack(76).getOccupancy()):
            self.redLine.Waysides[0].getTrack(76).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(76).setLight(True)


        #Switch  F16 - A1, F16 - E15
        if(self.redLine.Waysides[0].getTrack(0).getOccupancy() or self.redLine.Waysides[0].getTrack(15).getOccupancy()):
            self.redLine.Waysides[0].getTrack(15).setSwitch(False)
        if(self.redLine.Waysides[0].getTrack(14).getOccupancy()):
            self.redLine.Waysides[0].getTrack(15).setSwitch(True)
        #Signal A1
        if(self.redLine.Waysides[0].getTrack(0).getOccupancy()):
            self.redLine.Waysides[0].getTrack(0).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(0).setLight(True)
        #Signal E15
        if(self.redLine.Waysides[0].getTrack(14).getOccupancy()):
            self.redLine.Waysides[0].getTrack(14).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(14).setLight(True)
        #Signal F16
        if(self.redLine.Waysides[0].getTrack(15).getOccupancy()):
            self.redLine.Waysides[0].getTrack(15).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(15).setLight(True)


        #Switch H27 - H28 , H27 - T76
        if(self.redLine.Waysides[0].getTrack(25).getOccupancy() or self.redLine.Waysides[0].getTrack(27).getOccupancy()):
            self.redLine.Waysides[0].getTrack(26).setSwitch(False)
        elif(self.redLine.Waysides[0].getTrack(75).getOccupancy()):
            self.redLine.Waysides[0].getTrack(15).setSwitch(True)
        #Signal H27
        if(self.redLine.Waysides[0].getTrack(26).getOccupancy() and not(self.redLine.Waysides[0].getTrack(27).getOccupancy() or self.redLine.Waysides[0].getTrack(28).getOccupancy())):
            self.redLine.Waysides[0].getTrack(26).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(26).setLight(True)
        #Signal H28
        if(self.redLine.Waysides[0].getTrack(27).getOccupancy() and not(loop1 or self.redLine.Waysides[0].getTrack(76).getOccupancy())):
            self.redLine.Waysides[0].getTrack(27).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(27).setLight(True)
        #Signal T76
        if(self.redLine.Waysides[0].getTrack(75).getOccupancy() and not(loop1 or self.redLine.Waysides[0].getTrack(76).getOccupancy())):
            self.redLine.Waysides[0].getTrack(75).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(75).setLight(True)

        
        #Switch H33 - R72 , H33 - H32
        if(self.redLine.Waysides[0].getTrack(33).getOccupancy() or self.redLine.Waysides[0].getTrack(71).getOccupancy()):
            self.redLine.Waysides[0].getTrack(32).setSwitch(False)
        elif(self.redLine.Waysides[0].getTrack(31).getOccupancy()):
            self.redLine.Waysides[0].getTrack(32).setSwitch(True)
        #Signal H32
        if(self.redLine.Waysides[0].getTrack(31).getOccupancy() and not(leg or self.redLine.Waysides[0].getTrack(70).getOccupancy())):
            self.redLine.Waysides[0].getTrack(31).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(31).setLight(True)
        #Signal H33
        if(self.redLine.Waysides[0].getTrack(32).getOccupancy() and not(self.redLine.Waysides[0].getTrack(71).getOccupancy() or self.redLine.Waysides[0].getTrack(72).getOccupancy())):
            self.redLine.Waysides[0].getTrack(32).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(32).setLight(True)
        #Signal R72
        if(self.redLine.Waysides[0].getTrack(71).getOccupancy() and not(self.redLine.Waysides[0].getTrack(32).getOccupancy() or self.redLine.Waysides[0].getTrack(33).getOccupancy())):
            self.redLine.Waysides[0].getTrack(71).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(71).setLight(True)
        

        #Switch H38 - H39 , H38 - Q71
        if(self.redLine.Waysides[0].getTrack(36).getOccupancy() or self.redLine.Waysides[0].getTrack(38).getOccupancy()):
            self.redLine.Waysides[0].getTrack(37).setSwitch(False)
        elif(self.redLine.Waysides[0].getTrack(70).getOccupancy()):
            self.redLine.Waysides[0].getTrack(37).setSwitch(True)
        #Signal H38
        if(self.redLine.Waysides[0].getTrack(37).getOccupancy() and not(self.redLine.Waysides[0].getTrack(38).getOccupancy() or self.redLine.Waysides[0].getTrack(39).getOccupancy())):
            self.redLine.Waysides[0].getTrack(37).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(37).setLight(True)
        #Signal H39
        if(self.redLine.Waysides[0].getTrack(38).getOccupancy() and not(self.redLine.Waysides[0].getTrack(37).getOccupancy() or self.redLine.Waysides[0].getTrack(36).getOccupancy())):
            self.redLine.Waysides[0].getTrack(38).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(38).setLight(True)
        #Signal Q71
        if(self.redLine.Waysides[0].getTrack(70).getOccupancy() and not(leg)):
            self.redLine.Waysides[0].getTrack(70).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(70).setLight(True)


        #Switch H44 - O67 , H44 - H43
        if(self.redLine.Waysides[0].getTrack(44).getOccupancy() or self.redLine.Waysides[0].getTrack(66).getOccupancy()):
            self.redLine.Waysides[0].getTrack(43).setSwitch(False)
        elif(self.redLine.Waysides[0].getTrack(42).getOccupancy()):
            self.redLine.Waysides[0].getTrack(43).setSwitch(True)
        #Signal H43
        if(self.redLine.Waysides[0].getTrack(42).getOccupancy() and not(loop2)):
            self.redLine.Waysides[0].getTrack(42).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(42).setLight(True)
        #Signal H44
        if(self.redLine.Waysides[0].getTrack(43).getOccupancy() and not(self.redLine.Waysides[0].getTrack(66).getOccupancy() or self.redLine.Waysides[0].getTrack(67).getOccupancy())):
            self.redLine.Waysides[0].getTrack(43).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(43).setLight(True)
        #Signal O67
        if(self.redLine.Waysides[0].getTrack(66).getOccupancy() and not(loop2)):
            self.redLine.Waysides[0].getTrack(66).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(66).setLight(True)


        #Crossroad I47
        if(self.redLine.Waysides[0].getTrack(45).getOccupancy() or self.redLine.Waysides[0].getTrack(46).getOccupancy() or self.redLine.Waysides[0].getTrack(47).getOccupancy()):
            self.redLine.Waysides[0].getTrack(46).setCrossroad(True)
        else:
            self.redLine.Waysides[0].getTrack(46).setCrossroad(False)


        #Switch J52 - J53 , J52 - N66
        if(self.redLine.Waysides[0].getTrack(50).getOccupancy() or self.redLine.Waysides[0].getTrack(51).getOccupancy()):
            self.redLine.Waysides[0].getTrack(51).setSwitch(False)
        if(self.redLine.Waysides[0].getTrack(65).getOccupancy()):
            self.redLine.Waysides[0].getTrack(51).setSwitch(True)
        #Signal J52
        if(self.redLine.Waysides[0].getTrack(51).getOccupancy()):
            self.redLine.Waysides[0].getTrack(51).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(51).setLight(True)
        #Signal J53
        if(self.redLine.Waysides[0].getTrack(52).getOccupancy()):
            self.redLine.Waysides[0].getTrack(52).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(52).setLight(True)
        #Signal N66
        if(self.redLine.Waysides[0].getTrack(65).getOccupancy()):
            self.redLine.Waysides[0].getTrack(65).setLight(False)
        else:
            self.redLine.Waysides[0].getTrack(65).setLight(True)
    def sendStopGreen(self, occu):
        blocksStop = []
        blocks = []
        for i in range (len(self.greenLine.Waysides)):
                for j in range (self.greenLine.Waysides[i].amountOfTracks()):
                    blocks.append(self.greenLine.Waysides[i].tracks[j])
        #Green Line
        #Collision Logic
        for i in range(3, 15):
            if(blocks[i].getOccupancy()):
                if(blocks[i-1].getOccupancy() or blocks[i-2].getOccupancy()):
                    blocksStop.append(blocks[i].getName())
        for i in range(14, 148):
            if(blocks[i].getOccupancy()):
                if(blocks[i+1].getOccupancy() or blocks[i+2].getOccupancy() or blocks[i+3].getOccupancy()):
                    blocksStop.append(blocks[i].getName())

        #Light Stop
        if(self.greenLine.Waysides[1].getTrack(41).getLight()):
            if(occu[150]):
                blocksStop.append("Z151")
        if(self.greenLine.Waysides[1].getTrack(28).getLight()): #Check 3 Out
            if(occu[59]):
                blocksStop.append("J60")
            elif(occu[60]):
                blocksStop.append("J61")
            elif(occu[60]):
                blocksStop.append("J62")
        if(self.greenLine.Waysides[2].getTrack(2).getLight()): #Check 3 out
            if(occu[74]):
                blocksStop.append("M75")
            elif(occu[73]):
                blocksStop.append("M74")
            elif(occu[75]):
                blocksStop.append("M76")
        if(self.greenLine.Waysides[2].getTrack(3).getLight()): #Check 3 out
            if(occu[77]):
                blocksStop.append("N78")
            elif(occu[78]):
                blocksStop.append("N79")
            elif(occu[79]):
                blocksStop.append("N80")
        if(self.greenLine.Waysides[2].getTrack(11).getLight()): #Check 3 out
            if(occu[82]):
                blocksStop.append("N83")
            elif(occu[83]):
                blocksStop.append("N84")
            elif(occu[81]):
                blocksStop.append("N82")
        if(self.greenLine.Waysides[2].getTrack(26).getLight()): #Check 4 out
            if(occu[98]):
                blocksStop.append("Q99")
            elif(occu[99]):
                blocksStop.append("Q100")
            elif(occu[97]):
                blocksStop.append("Q98")
            elif(occu[96]):
                blocksStop.append("P97")
        if(self.greenLine.Waysides[0].getTrack(32).getLight()): #Check 3 out
            if(occu[148]):
                blocksStop.append("Y149")
            elif(occu[149]):
                blocksStop.append("Z150")
            elif(occu[147]):
                blocksStop.append("Y148")
        if(self.greenLine.Waysides[0].getTrack(28).getLight()):
            if(occu[26]):
                blocksStop.append("F27")
            elif(occu[27]):
                blocksStop.append("F28")
        if(self.greenLine.Waysides[0].getTrack(12).getLight()):
            if(occu[13]):
                blocksStop.append("D14")
            elif(occu[14]):
                blocksStop.append("D15")
        if(self.greenLine.Waysides[0].getTrack(0).getLight()):
            if(occu[0]):
                blocksStop.append("A1")
            elif(occu[1]):
                blocksStop.append("A2")
        if(self.greenLine.Waysides[1].getTrack(25).getLight()):
            if(occu[55]):
                blocksStop.append("I56")
            elif(occu[56]):
                blocksStop.append("I57")
        #Send the data out to the Track model here
        self.trackModelStoppedTrains.emit(blocksStop)
    def sendStopRed(self):
        stoppage = []
        loop1 = False
        loop2 = False
        leg = False
        for i in range(0, 16):
            loop1 = loop1 or self.redLine.Waysides[0].getTrack(i).getOccupancy()
        for i in range(43, 67):
            loop2 = loop2 or self.redLine.Waysides[0].getTrack(i).getOccupancy()
        for i in range(32, 38):
            leg = leg or self.redLine.Waysides[0].getTrack(i).getOccupancy()

        #Signal C10
        if(self.redLine.Waysides[0].getTrack(9).getOccupancy() and (self.redLine.Waysides[0].getTrack(10).getOccupancy() or self.redLine.Waysides[0].getTrack(11).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(9).getName())
        #Signal D11
        if(self.redLine.Waysides[0].getTrack(10).getOccupancy() and (self.redLine.Waysides[0].getTrack(9).getOccupancy() or self.redLine.Waysides[0].getTrack(8).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(10).getName())
        #Signal Yard
        if(self.redLine.Waysides[0].getTrack(76).getOccupancy() and loop1):
            stoppage.append(self.redLine.Waysides[0].getTrack(76).getName())
        #Signal A1
        if(self.redLine.Waysides[0].getTrack(0).getOccupancy() and (self.redLine.Waysides[0].getTrack(15).getOccupancy() or self.redLine.Waysides[0].getTrack(16).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(0).getName())
        #Signal E15
        if(self.redLine.Waysides[0].getTrack(14).getOccupancy() and (self.redLine.Waysides[0].getTrack(15).getOccupancy() or self.redLine.Waysides[0].getTrack(16).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(14).getName())
        #Signal F16
        if(self.redLine.Waysides[0].getTrack(15).getOccupancy() and (self.redLine.Waysides[0].getTrack(0).getOccupancy() or self.redLine.Waysides[0].getTrack(1).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(15).getName())
        #Signal H27
        if(self.redLine.Waysides[0].getTrack(26).getOccupancy() and (self.redLine.Waysides[0].getTrack(27).getOccupancy() or self.redLine.Waysides[0].getTrack(28).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(26).getName())
        #Signal H28
        if(self.redLine.Waysides[0].getTrack(27).getOccupancy() and (loop1 or self.redLine.Waysides[0].getTrack(76).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(27).getName())
        #Signal T76
        if(self.redLine.Waysides[0].getTrack(75).getOccupancy() and (loop1 or self.redLine.Waysides[0].getTrack(76).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(76).getName())
        #Signal H32
        if(self.redLine.Waysides[0].getTrack(31).getOccupancy() and (leg or self.redLine.Waysides[0].getTrack(70).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(31).getName())
        #Signal H33
        if(self.redLine.Waysides[0].getTrack(32).getOccupancy() and (self.redLine.Waysides[0].getTrack(71).getOccupancy() or self.redLine.Waysides[0].getTrack(72).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(32).getName())
        #Signal R72
        if(self.redLine.Waysides[0].getTrack(71).getOccupancy() and (self.redLine.Waysides[0].getTrack(32).getOccupancy() or self.redLine.Waysides[0].getTrack(33).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(71).getName())
        #Signal H38
        if(self.redLine.Waysides[0].getTrack(37).getOccupancy() and (self.redLine.Waysides[0].getTrack(38).getOccupancy() or self.redLine.Waysides[0].getTrack(39).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(37).getName())
        #Signal H39
        if(self.redLine.Waysides[0].getTrack(38).getOccupancy() and (self.redLine.Waysides[0].getTrack(37).getOccupancy() or self.redLine.Waysides[0].getTrack(36).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(38).getName())
        #Signal Q71
        if(self.redLine.Waysides[0].getTrack(70).getOccupancy() and (leg)):
            stoppage.append(self.redLine.Waysides[0].getTrack(70).getName())
        #Signal H43
        if(self.redLine.Waysides[0].getTrack(42).getOccupancy() and (loop2)):
            stoppage.append(self.redLine.Waysides[0].getTrack(42).getName())
        #Signal H44
        if(self.redLine.Waysides[0].getTrack(43).getOccupancy() and (self.redLine.Waysides[0].getTrack(66).getOccupancy() or self.redLine.Waysides[0].getTrack(67).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(43).getName())
        #Signal O67
        if(self.redLine.Waysides[0].getTrack(66).getOccupancy() and (loop2)):
            stoppage.append(self.redLine.Waysides[0].getTrack(66).getName())
        #Signal J52
        if(self.redLine.Waysides[0].getTrack(51).getOccupancy() and (self.redLine.Waysides[0].getTrack(52).getOccupancy() or self.redLine.Waysides[0].getTrack(53).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(51).getName())
        #Signal J53
        if(self.redLine.Waysides[0].getTrack(52).getOccupancy() and (self.redLine.Waysides[0].getTrack(51).getOccupancy() or self.redLine.Waysides[0].getTrack(50).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(52).getName())
        #Signal N66
        if(self.redLine.Waysides[0].getTrack(65).getOccupancy() and (self.redLine.Waysides[0].getTrack(51).getOccupancy() or self.redLine.Waysides[0].getTrack(50).getOccupancy())):
            stoppage.append(self.redLine.Waysides[0].getTrack(65).getName())
        #Send the data out to the Track model here
        self.trackModelStoppedTrains.emit(stoppage)





    #Anything below this shouldn't need to be touched or edited
    #Functions used in Whole UI
    def openArduinoFile(self): #Functionality for PLC File Opening
        dialog = QFileDialog()
        dialog.setNameFilter("Arduino File (*.ino)")
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialogSuccessful = dialog.exec()
        if dialogSuccessful:
            fileLocation = dialog.selectedFiles()[0]
            self.label_4.setText(fileLocation)
            arduino = "C:\Program Files (x86)\Arduino\\arduino.exe"
            command = f'"{arduino}" "{fileLocation}"'
            subprocess.run(command, shell=True) 
    
    #Functions used in Automatic Mode
    def checkListAutomatic(self): #Checks if a Line is selected or not to grey out combo boxes and list
        if self.listWidget_3.currentItem() is not None:
            self.comboBox.setEnabled(True)
        self.configureWaysidesAutomaticGreen()
    def checkWaysideSelectionAutomatic(self): #Checks if still selecting crossroad to grey out button
        value = self.comboBox.currentText()
        if value == "Select Wayside":
            for combo_box in [self.comboBox_5, self.comboBox_6, self.comboBox_7, self.listWidget_7, self.listWidget_8]:
                combo_box.setDisabled(True)
        else:
            for combo_box in [self.comboBox_5, self.comboBox_6, self.comboBox_7, self.listWidget_7, self.listWidget_8]:
                combo_box.setEnabled(True)
        self.configureLightsAutomaticGreen(value)
        self.configureCrossroadsAutomaticGreen(value)
        self.configureSwitchAutomaticGreen(value)
    def defaultLight(self):
        text = self.comboBox_5.currentText()
        if text == "Select Light":
            return
        properText = text.replace("Light ", "") #Get Just track Number and letter into a string
        waysideNumber = self.comboBox.currentIndex()-1 #Gets the current wayside selected
        value = self.listWidget_3.currentItem()
        if(value.text() == "Green Line"):
            for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
                if(properText == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            operate.changeLight(self.greenLine.Waysides[waysideNumber].getTrack(i).getLight())
        elif(value.text() == "Red Line"):
            for i in range(self.redLine.Waysides[waysideNumber].amountOfTracks()):
                if(properText == self.redLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            operate.changeLight(self.redLine.Waysides[waysideNumber].getTrack(i).getLight())
    def defaultCrossroad(self):
        text = self.comboBox_6.currentText()
        if text == "Select Crossroad":
            return
        properText = text.replace("Crossroad ", "") #Get Just track Number and letter into a string
        waysideNumber = self.comboBox.currentIndex()-1 #Gets the current wayside selected
        value = self.listWidget_3.currentItem()
        if(value.text() == "Green Line"):
            for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
                if(properText == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            operate.crossroad(self.greenLine.Waysides[waysideNumber].getTrack(i).getCrossroad())
        elif(value.text() == "Red Line"):
            for i in range(self.redLine.Waysides[waysideNumber].amountOfTracks()):
                if(properText == self.redLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            operate.crossroad(self.redLine.Waysides[waysideNumber].getTrack(i).getCrossroad())
    def defaultSwitch(self):
        text = self.comboBox_7.currentText()
        if text == "Select Switch":
            return
        waysideNumber = self.comboBox.currentIndex()-1 #Gets the current wayside selected
        value = self.listWidget_3.currentItem()
        if(value.text() == "Green Line"):
            for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
                if(text == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            trackStatus = self.greenLine.Waysides[waysideNumber].getTrack(i).getSwitch()
            if trackStatus == True: #Right
                operate.switch(self.greenLine.Waysides[waysideNumber].getTrackName(i), self.greenLine.Waysides[waysideNumber].getTrack(i).getRightDest(), trackStatus)
            elif trackStatus == False: #Left
                operate.switch(self.greenLine.Waysides[waysideNumber].getTrackName(i), self.greenLine.Waysides[waysideNumber].getTrack(i).getLeftDest(), trackStatus)
        elif(value.text() == "Red Line"):
            for i in range(self.redLine.Waysides[waysideNumber].amountOfTracks()):
                if(text == self.redLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            trackStatus = self.redLine.Waysides[waysideNumber].getTrack(i).getSwitch()
            if trackStatus == True: #Right
                operate.switch(self.redLine.Waysides[waysideNumber].getTrackName(i), self.redLine.Waysides[waysideNumber].getTrack(i).getRightDest(), trackStatus)
            elif trackStatus == False: #Left
                operate.switch(self.redLine.Waysides[waysideNumber].getTrackName(i), self.redLine.Waysides[waysideNumber].getTrack(i).getLeftDest(), trackStatus)
    def setListsOccupancyAutomatic(self): #Shows occupancy on the lists for displaying
        waysideNumber = self.comboBox.currentIndex()-1 #Gets the current wayside selected
        self.listWidget_7.clear()
        value = self.listWidget_3.currentItem()
        if self.listWidget_3.currentItem() is None:
            return
        if(value.text() == "Green Line"):
            for j in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
                if self.greenLine.Waysides[waysideNumber].getTrack(j).getOccupancy() == True:
                    self.listWidget_7.addItem(self.greenLine.Waysides[waysideNumber].getTrackName(j))
        elif(value.text() == "Red Line"):
            for j in range(self.redLine.Waysides[waysideNumber].amountOfTracks()):
                if self.redLine.Waysides[waysideNumber].getTrack(j).getOccupancy() == True:
                    self.listWidget_7.addItem(self.redLine.Waysides[waysideNumber].getTrackName(j))
    def setListsFailureAutomatic(self): #Shows failures on the list for displaying
        waysideNumber = self.comboBox.currentIndex()-1 #Gets the current wayside selected
        self.listWidget_8.clear()
        value = self.listWidget_3.currentItem()
        if self.listWidget_3.currentItem() is None:
            return
        if(value.text() == "Green Line"):
            for j in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
                if self.greenLine.Waysides[waysideNumber].getTrack(j).getFailure() == True:
                    self.listWidget_8.addItem(self.greenLine.Waysides[waysideNumber].getTrackName(j))
        elif(value.text() == "Red Line"):
            for j in range(self.redLine.Waysides[waysideNumber].amountOfTracks()):
                if self.redLine.Waysides[waysideNumber].getTrack(j).getFailure() == True:
                    self.listWidget_8.addItem(self.redLine.Waysides[waysideNumber].getTrackName(j))

    #Functions used in Manual Mode
    def crossChangeManual(self): #Checks if still selecting crossroad to grey out button
        if self.comboBox_3.currentText() == "Select Crossroad":
            self.pushButton.setDisabled(True)
        else:
            self.pushButton.setDisabled(False)
    def switchChangeManual(self): #Checks if still selecting switch to grey out button
        if self.comboBox_4.currentText() == "Select Switch":
            self.pushButton_2.setDisabled(True)
        else:
            self.pushButton_2.setDisabled(False)
    def lightChangeManual(self): #Checks if still selecting light to grey out list
        if self.comboBox_2.currentText() == "Select Light":
            self.listWidget_2.setDisabled(True)
        else:
            self.listWidget_2.setDisabled(False)
    def checkListManual(self): #Checks if a wayside is selected or not to grey out combo boxes or not
        if self.listWidget.currentItem() is not None:
            self.comboBox_12.setEnabled(True)
        self.configureWaysidesManualGreen()
    def checkWaysideSelectionManual(self): #Checks if still selecting crossroad to grey out button
        value = self.comboBox_12.currentText()
        if value == "Select Wayside":
            for combo_box in [self.comboBox_2, self.comboBox_3, self.comboBox_4, self.listWidget_5, self.listWidget_6]:
                combo_box.setDisabled(True)
        else:
            for combo_box in [self.comboBox_2, self.comboBox_3, self.comboBox_4, self.listWidget_5, self.listWidget_6]:
                combo_box.setEnabled(True)
        self.configureLightsManualGreen(value)
        self.configureCrossroadsManualGreen(value)
        self.configureSwitchManualGreen(value)
    def editLight(self, text): #Edits the light when selection made on UI in manual and updates track
        light = self.comboBox_2.currentText()
        if light == "Select Light":
            return
        properText = light.replace("Light ", "") #Get Just track Number and letter into a string
        waysideNumber = self.comboBox_12.currentIndex()-1 #Gets the current wayside selected
        value = self.listWidget.currentItem()
        if(value.text() == "Green Line"):
            for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
                if(properText == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            if text == "Red":
                color = True
            elif text == "Green":
                color = False
            self.greenLine.Waysides[waysideNumber].getTrack(i).setLight(color)
            operate.changeLight(self.greenLine.Waysides[waysideNumber].getTrack(i).getLight())
        elif(value.text() == "Red Line"):
            for i in range(self.redLine.Waysides[waysideNumber].amountOfTracks()):
                if(properText == self.redLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            if text == "Red":
                color = True
            elif text == "Green":
                color = False
            self.redLine.Waysides[waysideNumber].getTrack(i).setLight(color)
            operate.changeLight(self.redLine.Waysides[waysideNumber].getTrack(i).getLight())
    def editCrossroad(self): #Edits crossroad when toggle switch pressed
        text = self.comboBox_3.currentText()
        if text == "Select Crossroad":
            return
        properText = text.replace("Crossroad ", "") #Get Just track Number and letter into a string
        waysideNumber = self.comboBox_12.currentIndex()-1 #Gets the current wayside selected
        value = self.listWidget.currentItem()
        if(value.text() == "Green Line"):
            for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
                if(properText == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            newVal = not self.greenLine.Waysides[waysideNumber].getTrack(i).getCrossroad() #Toggling the current value
            self.greenLine.Waysides[waysideNumber].getTrack(i).setCrossroad(newVal) #Setting it to the track it is associated with
            operate.crossroad(self.greenLine.Waysides[waysideNumber].getTrack(i).getCrossroad())
        elif(value.text() == "Red Line"):
            for i in range(self.redLine.Waysides[waysideNumber].amountOfTracks()):
                if(properText == self.redLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            newVal = not self.redLine.Waysides[waysideNumber].getTrack(i).getCrossroad() #Toggling the current value
            self.redLine.Waysides[waysideNumber].getTrack(i).setCrossroad(newVal) #Setting it to the track it is associated with
            operate.crossroad(self.redLine.Waysides[waysideNumber].getTrack(i).getCrossroad())
    def editSwitch(self): #Edits switch data when toggle switch is pressed
        text = self.comboBox_4.currentText()
        if text == "Select Crossroad":
            return
        waysideNumber = self.comboBox_12.currentIndex()-1 #Gets the current wayside selected
        value = self.listWidget.currentItem()
        if(value.text() == "Green Line"):
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
        elif(value.text() == "Red Line"):
            for i in range(self.redLine.Waysides[waysideNumber].amountOfTracks()):
                if(text == self.redLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            newVal = not self.redLine.Waysides[waysideNumber].getTrack(i).getSwitch() #Toggling the current value
            self.redLine.Waysides[waysideNumber].getTrack(i).setSwitch(newVal) #Setting it to the track it is associated with
            trackStatus = self.redLine.Waysides[waysideNumber].getTrack(i).getSwitch()
            if trackStatus == True: #Right
                operate.switch(self.redLine.Waysides[waysideNumber].getTrackName(i), self.redLine.Waysides[waysideNumber].getTrack(i).getRightDest(), trackStatus)
            elif trackStatus == False: #Left
                operate.switch(self.redLine.Waysides[waysideNumber].getTrackName(i), self.redLine.Waysides[waysideNumber].getTrack(i).getLeftDest(), trackStatus)
    def defaultLightManual(self): #Displaying default value of light
        text = self.comboBox_2.currentText()
        if text == "Select Light":
            return
        properText = text.replace("Light ", "") #Get Just track Number and letter into a string
        waysideNumber = self.comboBox_12.currentIndex()-1 #Gets the current wayside selected
        value = self.listWidget.currentItem()
        if(value.text() == "Green Line"):
            for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
                if(properText == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            operate.changeLight(self.greenLine.Waysides[waysideNumber].getTrack(i).getLight())
        elif(value.text() == "Red Line"):
            for i in range(self.redLine.Waysides[waysideNumber].amountOfTracks()):
                if(properText == self.redLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            operate.changeLight(self.redLine.Waysides[waysideNumber].getTrack(i).getLight())
    def defaultCrossroadManual(self): #Displaying default value of Crossroad
        text = self.comboBox_3.currentText()
        if text == "Select Crossroad":
            return
        properText = text.replace("Crossroad ", "") #Get Just track Number and letter into a string
        waysideNumber = self.comboBox_12.currentIndex()-1 #Gets the current wayside selected
        value = self.listWidget.currentItem()
        if(value.text() == "Green Line"):
            for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
                if(properText == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            operate.crossroad(self.greenLine.Waysides[waysideNumber].getTrack(i).getCrossroad())
        elif(value.text() == "Red Line"):
            for i in range(self.redLine.Waysides[waysideNumber].amountOfTracks()):
                if(properText == self.redLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            operate.crossroad(self.redLine.Waysides[waysideNumber].getTrack(i).getCrossroad())
    def defaultSwitchManual(self): #Displaying default value of switch
        text = self.comboBox_4.currentText()
        if text == "Select Switch":
            return
        waysideNumber = self.comboBox_12.currentIndex()-1 #Gets the current wayside selected
        value = self.listWidget.currentItem()
        if(value.text() == "Green Line"):
            for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
                if(text == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            trackStatus = self.greenLine.Waysides[waysideNumber].getTrack(i).getSwitch()
            if trackStatus == True: #Right
                operate.switch(self.greenLine.Waysides[waysideNumber].getTrackName(i), self.greenLine.Waysides[waysideNumber].getTrack(i).getRightDest(), trackStatus)
            elif trackStatus == False: #Left
                operate.switch(self.greenLine.Waysides[waysideNumber].getTrackName(i), self.greenLine.Waysides[waysideNumber].getTrack(i).getLeftDest(), trackStatus)
        elif(value.text() == "Red Line"):
            for i in range(self.redLine.Waysides[waysideNumber].amountOfTracks()):
                if(text == self.redLine.Waysides[waysideNumber].getTrackName(i)):
                    break
            trackStatus = self.redLine.Waysides[waysideNumber].getTrack(i).getSwitch()
            if trackStatus == True: #Right
                operate.switch(self.redLine.Waysides[waysideNumber].getTrackName(i), self.redLine.Waysides[waysideNumber].getTrack(i).getRightDest(), trackStatus)
            elif trackStatus == False: #Left
                operate.switch(self.redLine.Waysides[waysideNumber].getTrackName(i), self.redLine.Waysides[waysideNumber].getTrack(i).getLeftDest(), trackStatus)
    def setListsOccupancyManual(self): #Shows occupancy on the lists for displaying
        waysideNumber = self.comboBox_12.currentIndex()-1 #Gets the current wayside selected
        self.listWidget_5.clear()
        value = self.listWidget.currentItem()
        if self.listWidget.currentItem() is None:
            return
        if(value.text() == "Green Line"):
            for j in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
                if self.greenLine.Waysides[waysideNumber].getTrack(j).getOccupancy() == True:
                    self.listWidget_5.addItem(self.greenLine.Waysides[waysideNumber].getTrackName(j))
        elif(value.text() == "Red Line"):
            for j in range(self.redLine.Waysides[waysideNumber].amountOfTracks()):
                if self.redLine.Waysides[waysideNumber].getTrack(j).getOccupancy() == True:
                    self.listWidget_5.addItem(self.redLine.Waysides[waysideNumber].getTrackName(j))
    def setListsFailureManual(self): #Shows failures on the list for displaying
        waysideNumber = self.comboBox_12.currentIndex()-1 #Gets the current wayside selected
        self.listWidget_6.clear()
        value = self.listWidget.currentItem()
        if self.listWidget.currentItem() is None:
            return
        if(value.text() == "Green Line"):
            for j in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
                if self.greenLine.Waysides[waysideNumber].getTrack(j).getFailure() == True:
                    self.listWidget_6.addItem(self.greenLine.Waysides[waysideNumber].getTrackName(j))
        elif(value.text() == "Red Line"):
            for j in range(self.redLine.Waysides[waysideNumber].amountOfTracks()):
                if self.redLine.Waysides[waysideNumber].getTrack(j).getFailure() == True:
                    self.listWidget_6.addItem(self.redLine.Waysides[waysideNumber].getTrackName(j))

    #Functions used in Test Bench - Not updated for red line
    def checkListTest(self): #Checks if a line is selected or not to grey out combo boxes
        if self.listWidget_9.currentItem() is not None:
            self.comboBox_13.setEnabled(True)
        value = self.listWidget_9.currentItem()
        if value.text() == "Green Line":
            self.configureWaysidesTestGreen()
        elif value.text() == "Red Line":
            for i in range(self.comboBox_13.count(), 0, -1):
                self.comboBox_13.removeItem(i)
    def checkWaysideSelectionTest(self): #Checks if still selecting wayside to grey out button
        value = self.comboBox_13.currentText()
        if value == "Select Wayside":
            for combo_box in [self.comboBox_9, self.comboBox_10, self.comboBox_11, self.comboBox_8]:
                combo_box.setDisabled(True)
        else:
            for combo_box in [self.comboBox_9, self.comboBox_10, self.comboBox_11, self.comboBox_8]:
                combo_box.setEnabled(True)
        self.configureLightsTestGreen(value)
        self.configureCrossroadsTestGreen(value)
        self.configureSwitchTestGreen(value)
        self.configureTrackSelectionGreen(value)
    def crossChangeTest(self): #Checks if still selecting crossroad to grey out list
        if self.comboBox_10.currentText() == "Select Crossroad":
            self.listWidget_10.setDisabled(True)
        else:
            self.listWidget_10.setDisabled(False)
    def switchChangeTest(self): #Checks if still selecting switch to grey out list
        if self.comboBox_11.currentText() == "Select Switch":
            self.listWidget_11.setDisabled(True)
        else:
            self.listWidget_11.setDisabled(False)
    def lightChangeTest(self): #Checks if still selecting light to grey out list
        if self.comboBox_9.currentText() == "Select Light":
            self.listWidget_4.setDisabled(True)
        else:
            self.listWidget_4.setDisabled(False)
    def trackChangeTest(self):
        if self.comboBox_8.currentText() == "Track Selection":
            self.pushButton_4.setDisabled(True)
            self.pushButton_5.setDisabled(True)
        else:
            self.pushButton_4.setDisabled(False)
            self.pushButton_5.setDisabled(False)
    def switchSelection(self, item): #Displays proper options for each switch in test bench
        temp = self.listWidget_11.item(0)
        temp.setText("")
        temp = self.listWidget_11.item(1)
        temp.setText("")
        if item == "D13":
            temp = self.listWidget_11.item(0)
            temp.setText("D14->C12")
            temp = self.listWidget_11.item(1)
            temp.setText("A1->D14")
        elif item == "G29":
            temp = self.listWidget_11.item(0)
            temp.setText("F28->G30")
            temp = self.listWidget_11.item(1)
            temp.setText("Z150->F28")
        elif item == "J58":
            temp = self.listWidget_11.item(0)
            temp.setText("I57->YARD")
            temp = self.listWidget_11.item(1)
            temp.setText("I57->J59")
        elif item == "J62":
            temp = self.listWidget_11.item(0)
            temp.setText("J61->K63")
            temp = self.listWidget_11.item(1)
            temp.setText("YARD->K63")
        elif item == "N77":
            temp = self.listWidget_11.item(0)
            temp.setText("N78->R101")
            temp = self.listWidget_11.item(1)
            temp.setText("M76->N78")
        elif item == "N85":
            temp = self.listWidget_11.item(0)
            temp.setText("N84->O86")
            temp = self.listWidget_11.item(1)
            temp.setText("Q100->N84")
    def editLightTest(self, text):
        light = self.comboBox_9.currentText()
        if light == "Select Light":
            return
        properText = light.replace("Light ", "") #Get Just track Number and letter into a string
        waysideNumber = self.comboBox_13.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(properText == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        if text == "Red":
            color = True
        elif text == "Green":
            color = False
        self.greenLine.Waysides[waysideNumber].getTrack(i).setLight(color)
    def editCrossroadTest(self, current):
        text = self.comboBox_10.currentText()
        if text == "Select Crossroad":
            return
        properText = text.replace("Crossroad ", "") #Get Just track Number and letter into a string
        waysideNumber = self.comboBox_13.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(properText == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        if current == "On":
            self.greenLine.Waysides[waysideNumber].getTrack(i).setCrossroad(True)
        elif current == "Off":
            self.greenLine.Waysides[waysideNumber].getTrack(i).setCrossroad(False)
        print(self.greenLine.Waysides[waysideNumber].getTrack(i).getCrossroad())
    def editSwitchTest(self, current_row):
        text = self.comboBox_11.currentText()
        if text == "Select Switch":
            return
        waysideNumber = self.comboBox_13.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(text == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        index = current_row
        if index == 1: #Right
            self.greenLine.Waysides[waysideNumber].getTrack(i).setSwitch(True) #Setting it to the track it is associated with
        elif index == 0: #Left
            self.greenLine.Waysides[waysideNumber].getTrack(i).setSwitch(False) #Setting it to the track it is associated with
    def toggleTrack(self):
        text = self.comboBox_8.currentText()
        if text == "Track Selection":
            return
        waysideNumber = self.comboBox_13.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(text == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        newVal = not self.greenLine.Waysides[waysideNumber].getTrack(i).getOccupancy() #Toggling the current value
        self.greenLine.Waysides[waysideNumber].getTrack(i).setOccupancy(newVal) #Setting it to the track it is associated with
    def toggleFailure(self):
        text = self.comboBox_8.currentText()
        if text == "Track Selection":
            return
        waysideNumber = self.comboBox_13.currentIndex()-1 #Gets the current wayside selected
        for i in range(self.greenLine.Waysides[waysideNumber].amountOfTracks()):
            if(text == self.greenLine.Waysides[waysideNumber].getTrackName(i)):
                break
        newVal = not self.greenLine.Waysides[waysideNumber].getTrack(i).getFailure() #Toggling the current value
        self.greenLine.Waysides[waysideNumber].getTrack(i).setFailure(newVal) #Setting it to the track it is associated with

    #Code for configuration of Green and Red Line Values
    #Automatic Mode
    def configureWaysidesAutomaticGreen(self):
        for i in range(self.comboBox.count(), 0, -1):
            self.comboBox.removeItem(i)
        value = self.listWidget_3.currentItem()
        if(value.text() == "Green Line"):
            self.comboBox.addItem("Wayside 1")
            self.comboBox.addItem("Wayside 2")
            self.comboBox.addItem("Wayside 3")
            self.comboBox.addItem("Wayside 4")
        elif(value.text() == "Red Line"):
            self.comboBox.addItem("Wayside 1")
            self.comboBox.addItem("Wayside 2")      
    def configureLightsAutomaticGreen(self, currentWayside): #Sets proper lights for each wayside selection
        self.comboBox_5.setCurrentIndex(0)
        for i in range(self.comboBox_5.count(), 0, -1):
            self.comboBox_5.removeItem(i)
        value = self.listWidget_3.currentItem()
        if(value.text() == "Green Line"):
            if(currentWayside == "Wayside 1"):
                self.comboBox_5.addItem("Light A1")
                self.comboBox_5.addItem("Light D13")
                self.comboBox_5.addItem("Light G29")
                self.comboBox_5.addItem("Light Z150")
            elif(currentWayside == "Wayside 2"):
                self.comboBox_5.addItem("Light J58")
                self.comboBox_5.addItem("Light J61")
                self.comboBox_5.addItem("Light YARD")
            elif(currentWayside == "Wayside 3"):
                self.comboBox_5.addItem("Light M76")
                self.comboBox_5.addItem("Light N77")
                self.comboBox_5.addItem("Light N85")
                self.comboBox_5.addItem("Light Q100")
        if(value.text() == "Red Line"):
            if(currentWayside == "Wayside 1"):
                self.comboBox_5.addItem("Light A1")
                self.comboBox_5.addItem("Light C10")
                self.comboBox_5.addItem("Light D11")
                self.comboBox_5.addItem("Light E15")
                self.comboBox_5.addItem("Light F16")
                self.comboBox_5.addItem("Light H27")
                self.comboBox_5.addItem("Light H28")
                self.comboBox_5.addItem("Light H32")
                self.comboBox_5.addItem("Light H33")
                self.comboBox_5.addItem("Light R72")
                self.comboBox_5.addItem("Light T76")
                self.comboBox_5.addItem("Light T77")
            elif(currentWayside == "Wayside 2"):
                self.comboBox_5.addItem("Light H38")
                self.comboBox_5.addItem("Light H39")
                self.comboBox_5.addItem("Light H43")
                self.comboBox_5.addItem("Light H44")
                self.comboBox_5.addItem("Light J52")
                self.comboBox_5.addItem("Light J53")
                self.comboBox_5.addItem("Light N66")
                self.comboBox_5.addItem("Light O67")
                self.comboBox_5.addItem("Light Q71")
    def configureCrossroadsAutomaticGreen(self, currentWayside): #Sets proper crossroads for each wayside selection
        self.comboBox_6.setCurrentIndex(0)
        for i in range(self.comboBox_6.count(), 0, -1):
            self.comboBox_6.removeItem(i)
        value = self.listWidget_3.currentItem()
        if(value.text() == "Green Line"):
            if(currentWayside == "Wayside 1"):
                self.comboBox_6.addItem("Crossroad E19")
        elif(value.text() == "Red Line"):
            if(currentWayside == "Wayside 2"):
                self.comboBox_6.addItem("Crossroad I47")
    def configureSwitchAutomaticGreen(self, currentWayside): #Sets proper switches for each wayside selection
        self.comboBox_7.setCurrentIndex(0)
        for i in range(self.comboBox_7.count(), 0, -1):
            self.comboBox_7.removeItem(i)
        value = self.listWidget_3.currentItem()
        if(value.text() == "Green Line"):
            if(currentWayside == "Wayside 1"):
                self.comboBox_7.addItem("D13")
                self.comboBox_7.addItem("G29")
            elif(currentWayside == "Wayside 2"):
                self.comboBox_7.addItem("J58")
                self.comboBox_7.addItem("J62")
            elif(currentWayside == "Wayside 3"):
                self.comboBox_7.addItem("N77")
                self.comboBox_7.addItem("N85")
        elif(value.text() == "Red Line"):
            if(currentWayside == "Wayside 1"):
                self.comboBox_7.addItem("C9")
                self.comboBox_7.addItem("E15")
                self.comboBox_7.addItem("H27")
                self.comboBox_7.addItem("H32")
            elif(currentWayside == "Wayside 2"):
                self.comboBox_7.addItem("H38")
                self.comboBox_7.addItem("H43")
                self.comboBox_7.addItem("J52")
        
    #Manual Mode
    def configureWaysidesManualGreen(self):
        for i in range(self.comboBox_12.count(), 0, -1):
            self.comboBox_12.removeItem(i)
        value = self.listWidget.currentItem()
        if(value.text() == "Green Line"):
            self.comboBox_12.addItem("Wayside 1")
            self.comboBox_12.addItem("Wayside 2")
            self.comboBox_12.addItem("Wayside 3")
            self.comboBox_12.addItem("Wayside 4")
        elif(value.text() == "Red Line"):
            self.comboBox_12.addItem("Wayside 1")
            self.comboBox_12.addItem("Wayside 2")  
    def configureLightsManualGreen(self, currentWayside): #Sets proper lights for each wayside selection
        self.comboBox_2.setCurrentIndex(0)
        for i in range(self.comboBox_2.count(), 0, -1):
            self.comboBox_2.removeItem(i)
        value = self.listWidget.currentItem()
        if(value.text() == "Green Line"):
            if(currentWayside == "Wayside 1"):
                self.comboBox_2.addItem("Light A1")
                self.comboBox_2.addItem("Light D13")
                self.comboBox_2.addItem("Light G29")
                self.comboBox_2.addItem("Light Z150")
            elif(currentWayside == "Wayside 2"):
                self.comboBox_2.addItem("Light J58")
                self.comboBox_2.addItem("Light J61")
                self.comboBox_2.addItem("Light YARD")
            elif(currentWayside == "Wayside 3"):
                self.comboBox_2.addItem("Light M76")
                self.comboBox_2.addItem("Light N77")
                self.comboBox_2.addItem("Light N85")
                self.comboBox_2.addItem("Light Q100")
        if(value.text() == "Red Line"):
            if(currentWayside == "Wayside 1"):
                self.comboBox_2.addItem("Light A1")
                self.comboBox_2.addItem("Light C10")
                self.comboBox_2.addItem("Light D11")
                self.comboBox_2.addItem("Light E15")
                self.comboBox_2.addItem("Light F16")
                self.comboBox_2.addItem("Light H27")
                self.comboBox_2.addItem("Light H28")
                self.comboBox_2.addItem("Light H32")
                self.comboBox_2.addItem("Light H33")
                self.comboBox_2.addItem("Light R72")
                self.comboBox_2.addItem("Light T76")
                self.comboBox_2.addItem("Light T77")
            elif(currentWayside == "Wayside 2"):
                self.comboBox_2.addItem("Light H38")
                self.comboBox_2.addItem("Light H39")
                self.comboBox_2.addItem("Light H43")
                self.comboBox_2.addItem("Light H44")
                self.comboBox_2.addItem("Light J52")
                self.comboBox_2.addItem("Light J53")
                self.comboBox_2.addItem("Light N66")
                self.comboBox_2.addItem("Light O67")
                self.comboBox_2.addItem("Light Q71")
    def configureCrossroadsManualGreen(self, currentWayside): #Sets proper crossroads for each wayside selection
        self.comboBox_3.setCurrentIndex(0)
        for i in range(self.comboBox_3.count(), 0, -1):
            self.comboBox_3.removeItem(i)
        value = self.listWidget.currentItem()
        if(value.text() == "Green Line"):
            if(currentWayside == "Wayside 1"):
                self.comboBox_3.addItem("Crossroad E19")
        elif(value.text() == "Red Line"):
            if(currentWayside == "Wayside 2"):
                self.comboBox_3.addItem("Crossroad I47")
    def configureSwitchManualGreen(self, currentWayside): #Sets proper switches for each wayside selection
        self.comboBox_4.setCurrentIndex(0)
        for i in range(self.comboBox_4.count(), 0, -1):
            self.comboBox_4.removeItem(i)
        value = self.listWidget.currentItem()
        if(value.text() == "Green Line"):
            if(currentWayside == "Wayside 1"):
                self.comboBox_4.addItem("D13")
                self.comboBox_4.addItem("G29")
            elif(currentWayside == "Wayside 2"):
                self.comboBox_4.addItem("J58")
                self.comboBox_4.addItem("J62")
            elif(currentWayside == "Wayside 3"):
                self.comboBox_4.addItem("N77")
                self.comboBox_4.addItem("N85")
        elif(value.text() == "Red Line"):
            if(currentWayside == "Wayside 1"):
                self.comboBox_4.addItem("C9")
                self.comboBox_4.addItem("E15")
                self.comboBox_4.addItem("H27")
                self.comboBox_4.addItem("H32")
            elif(currentWayside == "Wayside 2"):
                self.comboBox_4.addItem("H38")
                self.comboBox_4.addItem("H43")
                self.comboBox_4.addItem("J52")
        
    #Test Bench - Not updated with red line stuff
    def configureWaysidesTestGreen(self):
        for i in range(self.comboBox_13.count(), 0, -1):
            self.comboBox_13.removeItem(i)
        self.comboBox_13.addItem("Wayside 1")
        self.comboBox_13.addItem("Wayside 2")
        self.comboBox_13.addItem("Wayside 3")
        self.comboBox_13.addItem("Wayside 4")
    def configureLightsTestGreen(self, currentWayside): #Sets proper lights for each wayside selection
        self.comboBox_9.setCurrentIndex(0)
        for i in range(self.comboBox_9.count(), 0, -1):
            self.comboBox_9.removeItem(i)
        if(currentWayside == "Wayside 1"):
            self.comboBox_9.addItem("Light A1")
            self.comboBox_9.addItem("Light D13")
            self.comboBox_9.addItem("Light G29")
            self.comboBox_9.addItem("Light Z150")
        elif(currentWayside == "Wayside 2"):
            self.comboBox_9.addItem("Light J58")
            self.comboBox_9.addItem("Light J61")
            self.comboBox_9.addItem("Light YARD")
        elif(currentWayside == "Wayside 3"):
            self.comboBox_9.addItem("Light M76")
            self.comboBox_9.addItem("Light N77")
            self.comboBox_9.addItem("Light N85")
            self.comboBox_9.addItem("Light Q100")
    def configureCrossroadsTestGreen(self, currentWayside): #Sets proper crossroads for each wayside selection
        self.comboBox_10.setCurrentIndex(0)
        for i in range(self.comboBox_10.count(), 0, -1):
            self.comboBox_10.removeItem(i)
        if(currentWayside == "Wayside 1"):
            self.comboBox_10.addItem("Crossroad E19")
    def configureSwitchTestGreen(self, currentWayside): #Sets proper switches for each wayside selection
        self.comboBox_11.setCurrentIndex(0)
        for i in range(self.comboBox_11.count(), 0, -1):
            self.comboBox_11.removeItem(i)
        if(currentWayside == "Wayside 1"):
            self.comboBox_11.addItem("D13")
            self.comboBox_11.addItem("G29")
        elif(currentWayside == "Wayside 2"):
            self.comboBox_11.addItem("J58")
            self.comboBox_11.addItem("J62")
        elif(currentWayside == "Wayside 3"):
            self.comboBox_11.addItem("N77")
            self.comboBox_11.addItem("N85")
    def configureTrackSelectionGreen(self, currentWayside):
        self.comboBox_8.setCurrentIndex(0)
        for i in range(self.comboBox_8.count(), 0, -1):
            self.comboBox_8.removeItem(i)
        if(currentWayside == "Wayside 1"):
            for i in range(self.greenLine.Waysides[0].amountOfTracks()):
                self.comboBox_8.addItem(self.greenLine.Waysides[0].getTrackName(i))
        elif(currentWayside == "Wayside 2"):
            for i in range(self.greenLine.Waysides[1].amountOfTracks()):
                self.comboBox_8.addItem(self.greenLine.Waysides[1].getTrackName(i))
        elif(currentWayside == "Wayside 3"):
            for i in range(self.greenLine.Waysides[2].amountOfTracks()):
                self.comboBox_8.addItem(self.greenLine.Waysides[2].getTrackName(i))
        elif(currentWayside == "Wayside 4"):
            for i in range(self.greenLine.Waysides[3].amountOfTracks()):
                self.comboBox_8.addItem(self.greenLine.Waysides[3].getTrackName(i))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HWTrackControllerGUI()
    widget = QWidget()
    window.setupUi(widget)
    window.connectFunctions()
    widget.show()
    sys.exit(app.exec())
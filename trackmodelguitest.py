from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow, QFileDialog
from PyQt6 import QtCore, QtGui, QtWidgets
import pandas as pd
from customUI import Ui_MainWindow
import os;
import random;

## TO CONVERT UI TO PY
# open terminal at folder with ui
# pyuic6 -x -o test.py mainwindow.ui
#profit
#################

#comboBox_4 = Block box
# comboBox_3 = Line Box


metersToFeet = 3.28084
kmhrTomihr = 0.621371

class Line():
    def __init__(self,name):
        self.name = name
        self.blocks = []

    def addBlock(self,blk):
        self.blocks.append(blk)

    def getBlockNames(self):
        if len(self.blocks) == 0:
            return []
        block_list = [blk.name for blk in self.blocks]
        return block_list
    
    def getOccupiedBlockNames(self):
        if(len(self.blocks) == 0):
            return []

        occupied_list = [blk.name for blk in self.blocks if blk.occupied]
        return occupied_list
    
    def getBlockFromName(self,blockName):
        return self.blocks[self.blocks.index(blockName)]
  
    def getBlockOccupancyList(self):
        occupancyMask = [blk.occupied for blk in self.blocks]
        return occupancyMask
    
    def updateLineStatus(self, controlSignals):
        for i in range(len(controlSignals)):
            if(self.blocks[i].switch[0] or self.blocks[i].crossroad[0] or self.blocks[i].signal[0]):
                #Switch Updating
                if(self.blocks[i].switch[3] != controlSignals[i][0]):
                    self.blocks[i].toggleSwitch()
                
                #Crossroad Updating
                if(self.blocks[i].crossroad[1] != controlSignals[i][1]):
                    self.blocks[i].toggleCrossroad()
                
                #Signal Updating
                if(self.blocks[i].signal[1] != controlSignals[i][2]):
                    self.blocks[i].toggleSignal()

#implement beacon locations, implement beacon data, Track---> Train function(which is in the beacons), Set up authoirty variable
class Block():
    def __init__(self,attributes):
        name, occupied, length, grade, limit, elevation = attributes

        # underground, station, switch, crossroad, signal

        self.name = name #string with name ex: "A2"
        self.occupied = occupied #bool with occupancy
        self.length = length #double with block length
        self.grade = grade #double with block grade
        self.limit = limit # double with speed limit
        self.elevation = elevation # double with elevation
        self.underground = False # bool with underground status
        self.station = [False, "", -1, ""] # list with if the station exists, station name, tickets sold, and station side ex
                                # [True, "SHADYSIDE", 86, "Left/Right"]
        self.switch = [False, "", "",False] # list with if the switch exists, block name pointing towards, block name pointing away
                            # [True, "16", "1"]
        self.crossroad = [False, True]
        self.signal = [False, True] #need to implement red or green

    def setOccupied(self):
        self.occupied = True

    def clearOccupied(self):
        self.occupied = False

    def toggleSwitch(self):
        if self.switch[0]:
            temp = self.switch[1]
            self.switch[1] = self.switch[2]
            self.switch[2] = temp
            self.switch[3] = not self.switch[3]

    def toggleCrossroad(self):
        if self.crossroad[0]:
            self.crossroad[1] = not self.crossroad[1]
    
    def toggleSignal(self):
        if self.signal[0]:
            self.signal[1] = not self.signal[1]
    
    def addUnderground(self):
        self.underground = True

    def addStation(self, infrastructure, stationSide):
        split = infrastructure.split(";")
        split = [x.lstrip() for x in split]

        stationName = split[split.index("STATION")+1]               
        ticketsSold = random.randint(0,100) #Change this to a random tickets sold

        self.station = [True, stationName, ticketsSold, stationSide]

    def addSwitch(self,infrastructure):
        split = infrastructure.split()

        nextWord = split[split.index("SWITCH")+1]

        if nextWord[0] == "(":
            #normal switch between blocks
            nextWord += split[split.index("SWITCH")+2]
            switch_blocks = nextWord.replace('(','').replace(')','').replace(';','-').split("-")

            connectedBlocks = [blk for blk in switch_blocks if switch_blocks.count(blk) == 1]

            #All switches are initialized to the left postiion active, AKA, False -> Left active; True -> Right Active,second to last bool shows this
            # Final bool for signal status
            switch = [True, connectedBlocks[0], connectedBlocks[1], False]

        elif nextWord == "TO/FROM":
            switch = [True, "YARD", ""]
            #switch to and from the yard

        elif nextWord == "TO":
            switch = [True, "YARD", ""]
            #switch to yard

        elif nextWord == "FROM":
            switch = [True, "YARD", ""]
            #switch from yard
            
        else:
            print("ERROR: Switch processing error")

    def addCrossroad(self):
        self.crossroad = [True, True]

    def addSignal(self):
        self.signal = [True, True]

class TrackModel():
    def __init__(self):
        self.lines = []

    def addLine(self, path):
        if not os.path.exists(path):
            print("File not selected!")
            return
        
        db = pd.read_csv(path)
        numOfRows = len(db.index)

        #instantiate line:
        newLine = Line(db.at[0,"Line"] + " Line")


        #Instantiate Blocks
        for i in range(numOfRows):
            if(not (db.isna().at[i,"Line"])):

                name = (str(db.at[i,"Section"])+str(db.at[i, "Block Number"])).lstrip('nan')
                length = db.at[i,"Block Length (m)"]
                grade = db.at[i,"Block Grade (%)"]
                limit = db.at[i,"Speed Limit (Km/Hr)"]
                elevation = db.at[i,"ELEVATION (M)"]

                attributes = (name,length,grade,limit,elevation)
                blk = Block(attributes)

            
                if(db.isna().at[i,"Infrastructure"]):
                    newLine.addBlock(blk)
                    continue

                infrastructure = str(db.at[i,"Infrastructure"]).replace(":",";")

                isUnderground = "UNDERGROUND" in infrastructure
                isStation = "STATION" in infrastructure
                isSwitch = "SWITCH" in infrastructure
                isCrossroad = "RAILWAY CROSSING" in infrastructure
                isSignal = "SIGNAL" in infrastructure
                isSWBeacon = "SW_BEACON" in infrastructure
                isSTBeacon = "ST_BEACON" in infrastructure


                if isUnderground:
                    blk.addUnderground()

                if isStation:
                    stationSide = str(db.at[i, "Station Side"])
                    blk.addStation(infrastructure, stationSide)

                if isSwitch:
                    blk.addSwitch(infrastructure)

                #True -> Closed, False -> Open
                if isCrossroad:
                    blk.addCrossroad()

                #Signal Status; True -> Red, False -> Green
                if isSignal:
                    blk.addSignal()

                newLine.addBlock(blk)

        self.lines.append(newLine)

    def getLineNames(self):
        names_list = [l.name for l in self.lines]
        return names_list
    
    def getLineFromName(self, lineName):
        for l in self.lines:
            if (l.name == lineName):
                return l
        
        print("ERROR: Line not found")
        return 0

    def updateOccupancy(self,occupancyList):
        #Clear occupancy
        for line in self.lines:
            for block in self.blocks:
                block.clearOccupied()

        for i in range(len(occupancyList)):
            blk_name, line_name = occupancyList
            self.lines[self.lines.index(line_name)].getBlockFromNames(blk_name).setOccupied()


class functionalUI(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.trackModel = TrackModel()

        self.occupied_debug = []

    def connect(self):
        self.comboBox_3.currentIndexChanged.connect(self.lineChange)
        self.comboBox_4.currentIndexChanged.connect(self.blockChange)
        self.pushButton_2.clicked.connect(self.buttonPress)
        self.lineEdit.returnPressed.connect(self.tbChange)

    def tbChange(self):
        tbInfo = self.lineEdit.displayText().split(',')
    
        for l in self.trackModel.lines:
            if(l.name == tbInfo[0]):
                break

        tbInfo.pop(0)

        self.occupied_debug += tbInfo

    def lineChange(self):
        #Clear the Blocks
        self.comboBox_4.clear()
        #Clear the Occupancy
        self.listWidget_2.clear()

        # Add the blocks associated with that line
        currentLineName = self.comboBox_3.currentText()

        l = self.trackModel.getLineFromName(currentLineName)
        self.comboBox_4.addItems(l.getBlockNames())
        self.listWidget_2.addItems(l.getOccupiedBlockNames())

    def blockChange(self):
        currentBlockName = self.comboBox_4.currentText()
        currentLineName = self.comboBox_3.currentText()

        l = self.trackModel.getLineFromName(currentLineName)
        b = l.getBlockFromName(currentBlockName)

        #name
        self.tableWidget_3.item(0,0).setText(b.name)

        #occupancy
        if(b.occupied):
            self.tableWidget_3.item(1,0).setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.tableWidget_3.item(1,0).setCheckState(QtCore.Qt.CheckState.Unchecked)

        #length
        self.tableWidget_3.item(2,0).setText(str(round(b.length * metersToFeet,3)) +" feet")

        #grade
        self.tableWidget_3.item(3,0).setText(str(b.grade) + "%")

        #elevation
        self.tableWidget_3.item(4,0).setText(str(round(b.elevation*metersToFeet,3)) + " feet")

        #limit
        self.tableWidget_3.item(5,0).setText(str(round(b.limit*kmhrTomihr,3)) + " mi/hr")

        #station
        if(b.station[0]):
            self.tableWidget_3.item(6,0).setCheckState(QtCore.Qt.CheckState.Checked)
            self.tableWidget_7.item(0,0).setText(b.station[1])
            self.tableWidget_7.item(1,0).setText(str(b.station[2]))
            self.tableWidget_7.item(2,0).setText(b.station[3])
            self.tableWidget_7.resizeColumnsToContents()
        else:
            self.tableWidget_3.item(6,0).setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.tableWidget_7.item(0,0).setText("")
            self.tableWidget_7.item(1,0).setText("")
            self.tableWidget_7.item(2,0).setText("")

        #Switch
        if(b.switch[0]):
            self.tableWidget_3.item(7,0).setCheckState(QtCore.Qt.CheckState.Checked)
            self.tableWidget_8.item(0,0).setText(b.name)
            self.tableWidget_8.item(1,0).setText(b.switch[1])
            self.tableWidget_8.item(2,0).setText(b.switch[2])
        else:
            self.tableWidget_3.item(7,0).setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.tableWidget_8.item(0,0).setText("")
            self.tableWidget_8.item(1,0).setText("")
            self.tableWidget_8.item(2,0).setText("")

        #Underground
        if(b.underground):
            self.tableWidget_3.item(8,0).setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.tableWidget_3.item(8,0).setCheckState(QtCore.Qt.CheckState.Unchecked)

        #Crossroad
        if(b.crossroad[0]):
            self.tableWidget_3.item(9,0).setCheckState(QtCore.Qt.CheckState.Checked)
            self.tableWidget_6.item(0,0).setText(b.name)
            self.tableWidget_6.item(1,0).setText("No" if b.crossroad[1] else "Yes")
        else:
            self.tableWidget_3.item(9,0).setCheckState(QtCore.Qt.CheckState.Unchecked)
            self.tableWidget_6.item(0,0).setText("")
            self.tableWidget_6.item(1,0).setText("")

    def buttonPress(self):
        fd = QFileDialog()
        path, _ = fd.getOpenFileName(None, 'Select a file:')
        self.trackModel.addLine(path)
        self.comboBox_3.clear()
        self.comboBox_3.addItems(self.trackModel.getLineNames())
      

app = QApplication([])
MainWindow = QMainWindow()
ui = functionalUI()
ui.setupUi(MainWindow)
ui.connect()
MainWindow.show()
# # Start the event loop.
app.exec()
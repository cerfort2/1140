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
        for b in self.blocks:
            if (b.name == blockName):
                return b
        
        print("ERROR: Line not found")
        return 0
    
    def getBlockOccupancyList(self):
        occupancyMask = [blk.occupied for blk in self.blocks]
        return occupancyMask
    
    def updateLine(self, signals):
        for i in range(len(signals)):
            if(self.blocks[i].switch[0] or self.blocks[i].crossroad[0]):
                #Switch Updating
                if(self.blocks[i].switch[3] != signals[i][0]):
                    self.blocks[i].toggleSwitch()
                
                #Crossroad Updating
                if(self.blocks[i].crossroad[1] != signals[i][1]):
                    self.blocks[i].toggleCrossroad()
                
                #Signal Updating
                if(self.blocks[i].switch[4] != signals[i][2]):
                    self.blocks[i].toggleSignal()


class Block():
    def __init__(self,attributes):
        name, occupied, length, grade, limit, elevation, underground, station, switch, crossroad = attributes

        self.name = name #string with name ex: "A2"
        self.occupied = occupied #bool with occupancy
        self.length = length #double with block length
        self.grade = grade #double with block grade
        self.limit = limit # double with speed limit
        self.elevation = elevation # double with elevation
        self.underground = underground # bool with underground status
        self.station = station # list with if the station exists, station name, tickets sold, and station side ex
                                # [True, "SHADYSIDE", 86, "Left/Right"]
        self.switch = switch # list with if the switch exists, block name pointing towards, block name pointing away
                            # [True, "16", "1"]
        self.crossroad = crossroad

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
        if self.switch[0]:
            self.switch[4] = not self.switch[4]
            
    def isSwitch(self):
        return self.switch[0]
    

class TrackModel():
    def __init__(self):
        self.lines = []

    def addLine(self, path):
        if os.path.exists(path):
            db = pd.read_csv(path)
            numOfRows = len(db.index)

            #instantiate line:
            newLine = Line(db.at[0,"Line"] + " Line")

            #Instantiate Blocks
            for i in range(numOfRows):
                if(not (db.isna().at[i,"Section"])):

                    name = db.at[i,"Section"]+str(int(db.at[i, "Block Number"]))
                    length = db.at[i,"Block Length (m)"]
                    grade = db.at[i,"Block Grade (%)"]
                    limit = db.at[i,"Speed Limit (Km/Hr)"]
                    elevation = db.at[i,"ELEVATION (M)"]
                    
                    if(not db.isna().at[i,"Infrastructure"]):
                        infrastructure = str(db.at[i,"Infrastructure"])
                        infrastructure = infrastructure.replace(":",";")

                        stationSide = str(db.at[i, "Station Side"])

                        underground = "UNDERGROUND" in infrastructure
                        isStation = "STATION" in infrastructure
                        isSwitch = "SWITCH" in infrastructure
                        isCrossing = "RAILWAY CROSSING" in infrastructure


                        #Station Processing
                        #################################################
                        if isStation:
                            split = infrastructure.split(";")

                            for i in range(len(split)):
                                if(split[i]== "STATION"):
                                    stationName = split[i+1]
                                    break
                            
                            ticketsSold = random.randint(0,100) #Change this to a random tickets sold

                            station = [isStation, stationName, ticketsSold, stationSide]

                        else:
                            station = [False, "", -1, ""]
                        #################################################


                        #Switch Processing
                        #################################################
                        if isSwitch:
                            split = infrastructure.split()

                            for i in range(len(split)):
                                if(split[i]== "SWITCH"):
                                    nextWord = split[i+1]
                                    break
                            
                            if nextWord[0] == "(":
                                #normal switch between blocks

                                nextWord += split[i+2]
                                nextWord = nextWord.replace('(','')
                                nextWord = nextWord.replace(')','')
                                nextWord = nextWord.replace(';','-')

                                switch_blocks = nextWord.split("-")

                                erasedDupes = [blk for blk in switch_blocks if switch_blocks.count(blk) == 1]

                                #All switches are initialized to the left postiion active, AKA, False -> Left active; True -> Right Active,second to last bool shows this
                                # Final bool for signal status
                                #Signal Status; True -> Red, False -> Green
                                switch = [isSwitch, erasedDupes[0], erasedDupes[1], False, True]


                            elif nextWord == "TO/FROM":
                                switch = [isSwitch, "YARD", ""]
                                #switch to and from the yard

                            elif nextWord == "TO":
                                switch = [isSwitch, "YARD", ""]
                                #switch to yard
                            elif nextWord == "FROM":
                                switch = [isSwitch, "YARD", ""]
                                #switch from yard
                            else:
                                print("ERROR: Switch processing error")
                        else:
                            switch = [False, "", "",False, True]
                        #################################################

                        #Crossroad Processing
                        #################################################
                        #True -> Closed, False -> Open
                        crossroad = [isCrossing, True]

                        #################################################


                    else:
                        underground = False
                        station = [False, "", -1, ""]
                        switch = [False, "", "", False, True]
                        crossroad = [False, True]
                        
                    

                    attributes = (name,False,length,grade,limit,elevation,underground,station,switch,crossroad)
                    blk = Block(attributes)
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


class functionalUI(Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.trackModel = TrackModel()

        self.occupied_debug = []

    def update(self):
        self.comboBox_3.activated.connect(self.lineChange)
        self.comboBox_4.activated.connect(self.blockChange)
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
ui.update()
MainWindow.show()
# # Start the event loop.
app.exec()
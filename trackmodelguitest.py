from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow, QFileDialog, QWidget
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QObject, pyqtSignal
import pandas as pd
from customUI import Ui_Form
import os
import random
import networkx as nx
import matplotlib.pyplot as plt

## TO CONVERT UI TO PY
# open terminal at folder with ui
# pyuic6 -x -o customUI.py mainwindow.ui
#profit
#################

#comboBox_4 = Block box
# comboBox_3 = Line Box


#polarity, #switch beacons, #updating map, #updating authority 
metersToFeet = 3.28084
kmhrTomihr = 0.621371

      
class Line():

    def __init__(self,df):
        numOfRows = len(df.index)
        self.name = df.at[0,"Line"] + " Line"
        self.blocks = []

        #Instantiate Blocks
        for i in range(numOfRows):
            if(not (df.isna().at[i,"Line"])):

                name = (str(df.at[i,"Section"])+str(df.at[i, "Block Number"])).lstrip('nan')
                length = df.at[i,"Block Length (m)"]
                grade = df.at[i,"Block Grade (%)"]
                limit = df.at[i,"Speed Limit (Km/Hr)"]
                elevation = df.at[i,"ELEVATION (M)"]

                attributes = (name,False,length,grade,limit,elevation)
                blk = Block(attributes)

            
                if(df.isna().at[i,"Infrastructure"]):
                    self.blocks.append(blk)
                    continue

                infrastructure = str(df.at[i,"Infrastructure"]).replace(":",";")

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
                    stationSide = str(df.at[i, "Station Side"])
                    blk.addStation(infrastructure, stationSide)

                if isSwitch:
                    blk.addSwitch(infrastructure)

                #True -> Closed, False -> Open
                if isCrossroad:
                    blk.addCrossroad()

                #Signal Status; True -> Red, False -> Green
                if isSignal:
                    blk.addSignal()

                if isSWBeacon:
                    blk.addBeaconAtSwitch()

                if isSTBeacon:
                    if isStation:
                        blk.addBeaconAtStation()
                    else:
                        blk.addBeaconBeforeStation()

                self.blocks.append(blk)
        
        self.loadBeacons()
        self.loadBlockConnections()
        self.loadPolarity()
          
    def designMap(self,blockSelected):
        
        plt.clf()

        pos = nx.kamada_kawai_layout(self.network)

        colors = []
        labels ={}

        for i in range(len(self.blocks)):
            if(self.blocks[i].occupied) or (self.blocks[i].name == blockSelected):
                labels[self.blocks[i]] = self.blocks[i].name
            else:
                labels[self.blocks[i]] = ""

            if self.blocks[i].occupied:
                colors.append('blue')
            elif self.blocks[i].crossroad[0]:
                colors.append('#FFA500') # Orange
            elif self.blocks[i].underground:
                colors.append('#964B00') #brown
            else:
                colors.append('green')


        nx.draw_networkx(self.network, pos,node_size = 50,
                    labels = labels, with_labels=True,
                    font_size = 12, node_color = colors, node_shape = 's')# so^>v<dph8.

        plt.draw()
        plt.show()

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
    
    def getOccupiedBlocks(self):
        if(len(self.blocks) == 0):
            return []

        occupied_list = [blk for blk in self.blocks if blk.occupied]
        return occupied_list

    def getBlock(self,blockName):
        return self.blocks[self.getBlockNames().index(blockName)]
  
    def loadBeacons(self):
        for i in range(len(self.blocks)):
            if self.blocks[i].approachingBeacon[0]:
                self.blocks[i].approachingBeacon[1] = str(self.blocks[i+1].station[1]) + "/" + str(self.blocks[i+1].station[3])
                # print(self.blocks[i].approachingBeacon[1])
            elif self.blocks[i].stationBeacon[0] or self.blocks[i].switchBeacon[0]: #This will only work for green line
                self.blocks[i].stationBeacon[1] += self.blocks[i].name
                self.blocks[i].stationBeacon[1] += "/"
                self.blocks[i].stationBeacon[1] += str(self.blocks[i].length)
                self.blocks[i].stationBeacon[1] += "/"
                self.blocks[i].stationBeacon[1] += str(self.blocks[i].underground)
                self.blocks[i].stationBeacon[1] += "/"
                self.blocks[i].stationBeacon[1] += str(self.blocks[i].limit)
                self.blocks[i].stationBeacon[1] += "; "
                for j in range(i+1,len(self.blocks)):
                    if self.blocks[j].stationBeacon[0] or self.blocks[j].switchBeacon[0]:
                        break
                    self.blocks[i].stationBeacon[1] += self.blocks[j].name
                    self.blocks[i].stationBeacon[1] += "/"
                    self.blocks[i].stationBeacon[1] += str(self.blocks[j].length)
                    self.blocks[i].stationBeacon[1] += "/"
                    self.blocks[i].stationBeacon[1] += str(self.blocks[j].underground)
                    self.blocks[i].stationBeacon[1] += "/"
                    self.blocks[i].stationBeacon[1] += str(self.blocks[j].limit)
                    self.blocks[i].stationBeacon[1] += "; "
                # print(self.blocks[i].stationBeacon[1])
  
    def loadPolarity(self):
        for blk in list(self.network.nodes):
            for neighbor in self.network.adj[blk]:
                if((blk.polarity == neighbor.polarity) and (not neighbor.polaritySetted)):
                    neighbor.polarity = not blk.polarity
                    neighbor.polaritySetted = True

        test = [blk.polarity for blk in self.blocks]
        print(test)

    def loadBlockConnections(self):
        self.network = nx.Graph()
        self.network.add_nodes_from(self.blocks)

        for i in range(len(self.blocks)-2):
            self.network.add_edge(self.blocks[i], self.blocks[i+1])
            if (self.blocks[i].switch[0]):
                self.network.add_edge(self.blocks[i], self.getBlock(self.blocks[i].switch[1]))
                self.network.add_edge(self.blocks[i], self.getBlock(self.blocks[i].switch[2]))
        
        if (self.name == "Green Line"):
            self.network.remove_edge(self.getBlock("Q100"), self.getBlock("R101"))
        #debug
        # nodeList = [node.name for node in list(self.network.nodes)]
        # print(nodeList)
        # for (e1, e2) in self.network.edges:
        #     print((e1.name,e2.name))

    #Track Model --> Track Controller
    def getBlockOccupancyList(self):
        occupancyMask = [blk.occupied for blk in self.blocks]
        return occupancyMask
    
    #Track Controller --> Track Model
    def updateLineStatus(self, controlSignals):
        for i in range(len(controlSignals[0])):
            if(self.blocks[i].switch[0] or self.blocks[i].crossroad[0] or self.blocks[i].signal[0]):
                #Switch Updating
                if(self.blocks[i].switch[3] != controlSignals[0][i]):
                    self.blocks[i].toggleSwitch()
                
                #Crossroad Updating
                if(self.blocks[i].crossroad[1] != controlSignals[1][i]):
                    self.blocks[i].toggleCrossroad()
                
                #Signal Updating
                if(self.blocks[i].signal[1] != controlSignals[2][i]):
                    self.blocks[i].toggleSignal()


    def initializeTrackControllerData(self):
        hasSwitch = [blk.switch[0] for blk in self.blocks]
        hasCrossroad = [blk.crossroad[0] for blk in self.blocks]
        hasSignal = [blk.signal[0] for blk in self.blocks]
        name = [blk.name for blk in self.blocks]
        leftBlock = []
        rightBlock = []
        for blk in self.blocks:
            if(blk.switch[0]):
                leftBlock.append(blk.switch[1])
                rightBlock.append(blk.switch[2])
            else:
                leftBlock.append("")
                rightBlock.append("")
        
        return [hasSwitch,hasCrossroad,hasSignal,name,leftBlock,rightBlock]
            

#implement beacon locations, implement beacon data
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
        self.switchBeacon = [False, ""]
        self.approachingBeacon = [False, ""]
        self.stationBeacon = [False, ""]
        self.polarity = True
        self.polaritySetted = False

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
            self.switch = [True, connectedBlocks[0], connectedBlocks[1], False]

        elif nextWord == "TO/FROM":
            self.switch = [True, "YARD", ""]
            #switch to and from the yard

        elif nextWord == "TO":
            self.switch = [True, "YARD", ""]
            #switch to yard

        elif nextWord == "FROM":
            self.switch = [True, "YARD", ""]
            #switch from yard
            
        else:
            print("ERROR: Switch processing error")

    def addCrossroad(self):
        self.crossroad = [True, True]

    def addSignal(self):
        self.signal = [True, True]

    def addBeaconBeforeStation(self):
        self.approachingBeacon = [True,""]

    def addBeaconAtStation(self):
        self.stationBeacon = [True, ""]

    def addBeaconAtSwitch(self):
        self.switchBeacon = [True,""]


class TrackModel(QObject):

    trackControllerOccupancy = pyqtSignal(list)
    trackControllerInitializeLine = pyqtSignal(list)

    trainModelSuggestedSpeed = pyqtSignal(list)
    trainModelAuthority = pyqtSignal(int)
    trainModelSwitchBeacon = pyqtSignal(str)
    trainModelApproachingBeacon = pyqtSignal(str)
    trainModelStationBeacon = pyqtSignal(str)
    trainModelGrade = pyqtSignal(list)
    trainModelCreation = pyqtSignal()
    trainModelPolarity = pyqtSignal(list)

    CTCticketSales = pyqtSignal(int)


    def __init__(self):
        super().__init__()
        self.lines = []
        authority = 0

    def addLine(self, path):
        if not os.path.exists(path):
            print("File not selected!")
            return
        
        df = pd.read_csv(path)

        #instantiate line:
        newLine = Line(df)
        self.lines.append(newLine)

    def getLineNames(self):
        names_list = [l.name for l in self.lines]
        return names_list
    
    def getLine(self, lineName):
        return self.lines[self.getLineNames().index(lineName)]
    
    #Emit track occupancy
    def emitOccupancy(self):
        for line in self.lines:
            self.trackControllerOccupancy.emit(line.getBlockOccupancyList())

    def emitStationBeacon(self):
        for line in self.lines:
            occupiedList = line.getOccupiedBlocks()
            for blk in occupiedList:
                if blk.stationBeacon[0]:
                    self.trainModelBeacon.emit(blk.stationBeacon[1])

    def emitSwitchBeacon(self):
        for line in self.lines:
            occupiedList = line.getOccupiedBlocks()
            for blk in occupiedList:
                if blk.switchBeacon[0]:
                    self.trainModelBeacon.emit(blk.switchBeacon[1])

    def emitApproachingBeacon(self):
        for line in self.lines:
            occupiedList = line.getOccupiedBlocks()
            for blk in occupiedList:
                if blk.approachingBeacon[0]:
                    self.trainModelBeacon.emit(blk.approachingBeacon[1])

    def grade(self):
        for line in self.lines:
            gradeList = [blk.grade for blk in line.blocks if blk.occupied]
            self.trainModelGrade.emit(gradeList)

    def polarity(self):
        for line in self.lines:
            polarityList = [blk.polarity for blk in line.blocks if blk.occupied]
            self.trainModelPolarity.emit(polarityList)

    def controlModel(self,controlSignals):
        for line in self.lines:
            line.updateLineStatus(controlSignals)

    #Train Model --> Track Model
    def updateOccupancy(self,occupancyList):
        #Clear occupancy
        for line in self.lines:
            for block in line.blocks:
                block.clearOccupied()

        if len(self.lines) == 0:
            return
        
        for blk_name in range(len(occupancyList)):
            self.lines[self.lines.index(self.lines[0])].getBlock(blk_name).setOccupied()

    #Track Model --> Train Model
    def routeToBlockLengths(self, route):

        for line in self.lines:
            blocksAndLengths = []

            for i in range(1, len(route)):
                blocksAndLengths.append((route[i], line.getBlock(route[i]).length))

        return blocksAndLengths

    #pass through track model
    def suggestedSpeed(self, SS):
        #create a train
        self.trainModelCreation.emit()

        self.trainModelSuggestedSpeed.emit(SS)

    def route(self, r):
        self.trainRoute = r

    #convert block authority to feet authority
    def authority(self, authorityInBlocks):
        for line in self.lines:
            occupiedList = line.getOccupiedBlockNames()
            for blkname in occupiedList:
                authorityInM = 0
                for i in range(self.trainRoute.index(blkname)+1,self.trainRoute.index(blkname)+1+authorityInBlocks):
                    if (i == self.trainRoute.index(blkname)+authorityInBlocks):
                        authorityInM += line.getBlock(self.trainRoute[i].length/2)
                    else:
                        authorityInM += line.getBlock(self.trainRoute[i]).length
                
        
        self.trainModelAuthority.emit(authorityInM)
          
    def initTrack(self):
        for line in self.lines:
            self.trackControllerInitializeLine.emit(line.initializeTrackControllerData())

    def getTicketsSales(self):
        for line in self.lines:
            tickets = [blk.station[2] for blk in line.getOccupiedBlocks() if blk.station[0]]

        if len(tickets) != 0:
            self.CTCticketSales.emit(tickets[0])
        
class functionalUI(Ui_Form):
    def __init__(self) -> None:
        super().__init__()
        self.trackModel = TrackModel()

    def connect(self):
        self.comboBox_3.currentIndexChanged.connect(self.lineChange)
        self.comboBox_4.currentIndexChanged.connect(self.blockChange)
        self.comboBox_4.currentIndexChanged.connect(self.updateMap)
        self.pushButton_2.clicked.connect(self.buttonPress)
        self.lineEdit.returnPressed.connect(self.tbChange)
        self.lineEdit.returnPressed.connect(self.updateMap)
        self.listWidget_2.itemActivated.connect(self.updateMap)

    def tbChange(self):
        
        self.listWidget_2.clear()
        tbInfo = self.lineEdit.displayText().split(',')

        line = self.trackModel.getLine(tbInfo[0])
        tbInfo.pop(0)

        for blk in line.blocks:
            blk.occupied = False

        for blk in tbInfo:
            line.getBlock(blk).occupied = True

        test = [blk.name for blk in line.blocks if blk.occupied]
        self.listWidget_2.addItems(test)

    def lineChange(self):
        #Clear the Blocks
        self.comboBox_4.clear()
        #Clear the Occupancy
        self.listWidget_2.clear()


        # Add the blocks associated with that line
        currentLineName = self.comboBox_3.currentText()

        line = self.trackModel.getLine(currentLineName)
        self.comboBox_4.addItems(line.getBlockNames())
        self.listWidget_2.addItems(line.getOccupiedBlockNames())

    def blockChange(self):
        currentBlockName = self.comboBox_4.currentText()
        currentLineName = self.comboBox_3.currentText()

        l = self.trackModel.getLine(currentLineName)
        b = l.getBlock(currentBlockName)

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
        self.trackModel.initTrack()
        self.updateMap()
      
    def updateMap(self):
        for line in self.trackModel.lines:
            line.designMap(self.comboBox_4.currentText())

    def update_time(self):
        self.trackModel.emitOccupancy()
        self.updateMap()
        self.trackModel.emitStationBeacon()
        self.trackModel.emitSwitchBeacon()
        self.trackModel.emitApproachingBeacon()
        self.trackModel.authority()
        self.trackModel.getTicketsSales()
        self.trackModel.polarity()
        self.trackModel.grade()







if __name__ == '__main__':
    app = QApplication([])
    MainWindow = QWidget()
    ui = functionalUI()
    ui.setupUi(MainWindow)
    ui.connect()
    MainWindow.show()
   
# # Start the event loop.
    app.exec()
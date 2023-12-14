from PyQt6.QtWidgets import QApplication, QComboBox, QMainWindow, QFileDialog, QWidget
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QObject, pyqtSignal
import pandas as pd
from Track_Model.customUI import Ui_Form
import os
import random
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
import mplcursors 

## TO CONVERT UI TO PY
# open terminal at folder with ui
# pyuic6 -x -o customUI.py trackModelWidget.ui
#profit
#################

#comboBox_4 = Block box
# comboBox_3 = Line Box


#polarity, #switch beacons, #updating map, #updating authority 
metersToFeet = 3.28084
kmhrTomihr = 0.621371

#UI changes
#Label the first block of each section (A1,B4,C12,D17)
#displaying signals on track

#Functional Changes
#Split the trouble blocks for polarity purposes (might need to hard code this)


class Line():

    def __init__(self,df):
        numOfRows = len(df.index)
        self.name = df.at[0,"Line"] + " Line"
        self.blocks = []

        #Instantiate Blocks
        for i in range(numOfRows):
            if(not (df.isna().at[i,"Line"])):

                name = (str(df.at[i,"Section"])+str(int(df.at[i, "Block Number"]))).lstrip('nan')
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
        
        self.loadBlockConnections()
        self.loadBeacons()
        self.loadPolarity()
        # self.testBeacons()
          
    def designMap(self, blockSelected, figureNumber):
        
        plt.figure(figureNumber)
        plt.clf()

        plt.margins(0)
        pos = nx.kamada_kawai_layout(self.network)

        colors = []
        labels = {}
        annotations = []
        edgesToBeDrawn = []
        signalXPos = []
        signalYPos = []
        signalColor = []
        nodeSize = []

        for i in range(len(self.blocks)):
            if(self.blocks[i].occupied) or (self.blocks[i].name == blockSelected):
                labels[self.blocks[i]] = self.blocks[i].name
            else:
                labels[self.blocks[i]] = ""

            # if(self.blocks[i].switchBeacon[0] or self.blocks[i].stationBeacon[0] or self.blocks[i].approachingBeacon[0]) or (self.blocks[i].name == blockSelected):
            #     labels[self.blocks[i]] = self.blocks[i].name
            # else:
            #     labels[self.blocks[i]] = ""

            # labels[self.blocks[i]] = self.blocks[i].polarity

            dataToAnnotate = self.blocks[i].name

            if self.blocks[i].station[0]:
                dataToAnnotate += "\n" + str(self.blocks[i].station[1]) + "\n" + "Tickets Sold:" + str(self.blocks[i].station[2])
            annotations.append(dataToAnnotate)

            if self.blocks[i].occupied:
                colors.append('#FFA500') #Orange
            elif self.blocks[i].station[0]:
                colors.append("#40E0D0")
            elif self.blocks[i].crossroad[0]:
                colors.append('blue') 
            elif self.blocks[i].underground:
                colors.append('#964B00') #brown
            else:
                colors.append(self.name.split()[0])
                # colors.append("black")

            if self.blocks[i].signal[0]:
                signalXPos.append(pos[self.blocks[i]][0] + 0.03)
                signalYPos.append(pos[self.blocks[i]][1])
                if self.blocks[i].signal[1]:
                    signalColor.append('red')
                else:
                    signalColor.append('green')


            if(self.blocks[i].occupied):
                nodeSize.append(25)
            else:
                nodeSize.append(5)

            


        
        for edge in self.network.edges:
            blk1, blk2 = edge
            if (not ((blk1.switch[0] and blk1.switch[2] == blk2.name) or (blk2.switch[0] and blk2.switch[2] == blk1.name))):
                edgesToBeDrawn.append(edge)







        nx.draw_networkx(self.network, pos,node_size = nodeSize,
                    labels = labels, with_labels=True,
                    font_size = 8, node_color = colors, node_shape = 's', 
                    edgelist = edgesToBeDrawn)# so^>v<dph8.
        # nx.draw_networkx_labels(self.network,pos,labels, horizontalalignment='right',verticalalignment='top')
        # nx.draw_networkx_edges(self.network,pos, edgelist=edgesToBeDrawn)

        plt.scatter(signalXPos,signalYPos, c=signalColor, s = 12)

        # plt.scatter(signalXPos,[yPos - 0.001 for yPos in signalYPos], marker= 3, c = 'black')




        mplcursors.cursor(hover = 2).connect(
            "add", lambda sel: sel.annotation.set_text(annotations[sel.index]))
        
        plt.draw()
        # plt.show()

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
  
    def loadPolarity(self):
        for blk in list(self.network.nodes):
            for neighbor in self.network.adj[blk]:
                if((blk.polarity == neighbor.polarity) and (not neighbor.polaritySetted)):
                    neighbor.polarity = not blk.polarity
                    neighbor.polaritySetted = True

        # test = [blk.polarity for blk in self.blocks]
        # print(test)

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

        if (self.name == "Red Line"):
            self.network.remove_edge(self.getBlock("Q71"),self.getBlock("R72"))
            self.network.remove_edge(self.getBlock("N66"),self.getBlock("O67"))

        if(self.name == "Blue Line"):
            self.network.remove_edge(self.getBlock("B10"), self.getBlock("C11"))
            self.network.add_edge(self.getBlock("C14"), self.getBlock("C15"))

    #Check beacons in an order: approaching, station, switch

    #if train going in block order: 
    # (switch or station) beacon  --> (switch or station) beacon 
    #basically, ignore approaching beacons,(you should still read in the station name and side from them)

    # if train going in opposite block order: 
    # (switch or approaching) beacon --> (switch or approaching) beacon
    #basically ignore station beacons

    # note that your order can change through the route
    def loadBeacons(self):
        #create a working copy of the network
        workingGraph = self.network.copy()

        #Create splits in the graph to seperate sections that are capped on both ends by beacons
        for edge in list(workingGraph.edges):
            blkOne,blkTwo = edge

            adjacentSwitchBeaconBlocks = blkOne.switchBeacon[0] and blkTwo.switchBeacon[0]
            stationThenApproaching = blkOne.stationBeacon[0] and blkTwo.approachingBeacon[0]
            approachingThenStation = blkOne.approachingBeacon[0] and blkTwo.stationBeacon[0]

            if adjacentSwitchBeaconBlocks or stationThenApproaching or approachingThenStation:
                workingGraph.remove_edge(blkOne,blkTwo)

        #Add station name and side to the approachingBeacons
        for i in range(len(self.blocks)):
            if self.blocks[i].approachingBeacon[0]:
                self.blocks[i].approachingBeacon[1] = str(self.blocks[i+1].station[1]) + "/" + str(self.blocks[i+1].station[3]) + "; "
            if self.blocks[i].stationBeacon[0]:
                self.blocks[i].stationBeacon[1] = str(self.blocks[i].station[1]) + "/" + str(self.blocks[i].station[3]) + "; "

        #Iterate through each connected segment of the track
        for connectedSet in nx.connected_components(workingGraph):
            sortedBlocks = list(sorted(connectedSet, key=self.sortBlocks))
            test = [blk.name for blk in sortedBlocks]

            #Iterate from the top of the segment and add data to the head beacon
            if sortedBlocks[0].approachingBeacon[0]:
                for blk in sortedBlocks:
                    sortedBlocks[0].approachingBeacon[1] += str(blk.name) + "/" + str(blk.length)+ "/" + str(blk.underground) + "/" + str(blk.limit) + "; "
            elif sortedBlocks[0].stationBeacon[0]:
                for blk in sortedBlocks:
                    pass
                    # sortedBlocks[0].stationBeacon[1] += str(blk.name) + "/" + str(blk.length)+ "/" + str(blk.underground) + "/" + str(blk.limit) + "; "
            elif sortedBlocks[0].switchBeacon[0]:
                for blk in sortedBlocks:
                    sortedBlocks[0].switchBeacon[1] += str(blk.name) + "/" + str(blk.length)+ "/" + str(blk.underground) + "/" + str(blk.limit) + "; "

            #check for singletons in connected sets and don't double add
            if len(sortedBlocks) == 1:
                continue

            #Iterate from the bottom of the segment and add the data to the tail beacon
            if sortedBlocks[-1].approachingBeacon[0]:
                for blk in reversed(sortedBlocks):
                    sortedBlocks[-1].approachingBeacon[1] += str(blk.name) + "/" + str(blk.length) + "/" + str(blk.underground) + "/" + str(blk.limit) + "; "
            elif sortedBlocks[-1].stationBeacon[0]:
                for blk in reversed(sortedBlocks):
                    pass
                    # sortedBlocks[-1].stationBeacon[1] += str(blk.name) + "/" + str(blk.length) + "/" + str(blk.underground) + "/" + str(blk.limit) + "; "
            elif sortedBlocks[-1].switchBeacon[0]:
                for blk in reversed(sortedBlocks):
                    sortedBlocks[-1].switchBeacon[1] += str(blk.name) + "/" + str(blk.length)+ "/" + str(blk.underground) + "/" + str(blk.limit) + "; "
            
    #sorting function only    
    def sortBlocks(self,element):
        return int(element.name[1:])
    
    def testBeacons(self):
        for blk in self.blocks:
            if(blk.approachingBeacon[0]):
                print(blk.name + ":Approaching:" + blk.approachingBeacon[1])
            elif(blk.stationBeacon[0]):
                print(blk.name + ":Station:" + blk.stationBeacon[1])
            elif(blk.switchBeacon[0]):
                print(blk.name + ":Switch:" + blk.switchBeacon[1])
            else:
                print(blk.name)

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

        #Basic Attributes
        self.name = name #string with name ex: "A2"
        self.occupied = occupied #bool with occupancy
        self.length = length #double with block length
        self.grade = grade #double with block grade
        self.limit = limit # double with speed limit
        self.elevation = elevation # double with elevation
        self.underground = False # bool with underground status
        
        #Infrastructure Attributes
        self.station = [False, "", -1, ""] # list with if the station exists, station name, tickets sold, and station side ex
                                # [True, "SHADYSIDE", 86, "Left/Right"]
        self.switch = [False, "", "",False] # list with if the switch exists, block name pointing towards, block name pointing away
                            # [True, "16", "1"]
        self.crossroad = [False, True]
        self.signal = [False, True] 
        self.switchBeacon = [False, ""]
        self.approachingBeacon = [False, ""]
        self.stationBeacon = [False, ""]
        self.trackHeater = False

        #Polarity Attributes
        self.polarity = True
        self.polaritySetted = False

        #Failure Attributes
        self.brokenRail = False
        self.trackCircuitFailure = False
        self.powerFailure = False

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

    def __init__(self):
        super().__init__()
        self.controlSignalsHolder = [[],[],[]]
        self.lines = []
        self.occupancyList = []
        self.occupancyListStrings = []
        self.route_passthrough = []
        self.suggestedSpeed_passthrough= []
        self.authority_passthrough = []
        self.temperature = 50

    #--------------------
    #Internal Functions
    #--------------------
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
    
    #--------------------
    #Transmitting Signal Functions
    #--------------------
    
    #Emit track occupancy
    trackControllerOccupancy = pyqtSignal(list)
    def emitOccupancy(self):
        for line in self.lines:
            self.trackControllerOccupancy.emit(line.getBlockOccupancyList())

    #Initialize the track to the other modules
    trackControllerInitializeLine = pyqtSignal(list)
    def initTrack(self):
        for line in self.lines:
            self.trackControllerInitializeLine.emit(line.initializeTrackControllerData())

    #Emit Station Beacon
    trainModelStationBeacon = pyqtSignal(list)
    def emitStationBeacon(self):
        stationInfo = []
        for blk in self.occupancyList:
            if blk.stationBeacon[0]:
                stationInfo.append(blk.stationBeacon[1])
            else:
                stationInfo.append("")

        self.trainModelStationBeacon.emit(stationInfo)

    #Emit Switch Beacons
    trainModelSwitchBeacon = pyqtSignal(str)
    def emitSwitchBeacon(self):
        for blk in self.occupancyList:
            if blk.switchBeacon[0]:
                self.trainModelSwitchBeacon.emit(blk.switchBeacon[1])

    #Emit Approaching Beacons
    trainModelApproachingBeacon = pyqtSignal(str)
    def emitApproachingBeacon(self):
        for blk in self.occupancyList:
            if blk.approachingBeacon[0]:
                self.trainModelApproachingBeacon.emit(blk.approachingBeacon[1])

    #Emit polarity of occupied blocks
    trainModelPolarity = pyqtSignal()
    def polarity(self):
        # polarityList = [blk.polarity for blk in self.occupancyList if blk.occupied]
        self.trainModelPolarity.emit()

    #Send ticket sales of occupied stations
    CTCticketSales = pyqtSignal(list)
    def getTicketsSales(self):
        for line in self.lines:
            tickets = [blk.station[2] for blk in line.getOccupiedBlocks() if blk.station[0]]

        if len(tickets) != 0:
            self.CTCticketSales.emit(tickets)
     
    trainModelBlockInfo = pyqtSignal(list)
    def getOccupiedBlockInfo(self):
        blkInfoList = []
        for blk in self.occupancyList:
            blkInfo = [blk.limit,blk.grade,blk.underground]
            blkInfoList.append(blkInfo)

        
        self.trainModelBlockInfo.emit(blkInfoList)

    trackControllerFailureBlocks = pyqtSignal(list)
    def sendFailureBlocks(self):
        for line in self.lines:
            failedBlocks = [(blk.brokenRail or blk.trackCircuitFailure or blk.powerFailure) for blk in line.blocks]
            self.trackControllerFailureBlocks.emit(failedBlocks)


    trackModelUpdates = pyqtSignal() # Signal for if the map should update along with all other UI
    #------------------
    #Receiving Signals
    #------------------
    
    def controlModel(self,controlSignals):
        if self.controlSignalsHolder != controlSignals:
            for line in self.lines:
                line.updateLineStatus(controlSignals)

            self.controlSignalsHolder = controlSignals

            self.trackModelUpdates.emit()

    #Train Model --> Track Model
    def updateOccupancy(self,occupancyList):
        if len(self.lines) == 0:
            return
        
        if (self.occupancyListStrings == occupancyList):
            return
        
        self.occupancyListStrings = occupancyList #List of strings
        self.occupancyList = [self.lines[0].getBlock(name) for name in occupancyList] #List of Blocks in the correct order

        #Clear occupancy
        for line in self.lines:
            for block in line.blocks:
                if not (block.brokenRail or block.trackCircuitFailure or block.powerFailure):
                    block.clearOccupied()

        for blk_name in occupancyList:
            self.lines[self.lines.index(self.lines[0])].getBlock(blk_name).setOccupied()

        self.trackModelUpdates.emit()
        self.emitApproachingBeacon()
        self.emitSwitchBeacon()
        self.emitStationBeacon()

    #Track Model --> Track Controller
    def fixFailures(self, blockToFix):
        for line in self.lines:

            blk = line.getBlock(blockToFix)

            if blk.brokenRail:
                blk.brokenRail = not blk.brokenRail
            elif blk.trackCircuitFailure:
                blk.trackCircuitFailure = not blk.trackCircuitFailure
            elif blk.powerFailure:
                blk.powerFailure = not blk.powerFailure

            blk.clearOccupied()
        
        self.trackModelUpdates.emit()

    #Track Controller --> Track Model
    def closeBlock(self, blockToClose):
        for line in self.lines:
            line.getBlock(blockToClose).setOccupied()

    #Track Controller --> Track Model
    def openBlock(self, blockToOpen):
        for line in self.lines:
            line.getBlock(blockToOpen).clearOccupied()
                

    def updateTemp(self,temp):
        self.temperature = temp
        for line in self.lines:
            for block in line.blocks:
                if self.temperature > 32:
                    block.trackHeater = True
                else:
                    block.trackHeater = False



    #----------------
    #Pass through Signals
    #----------------
    trainModelCreation = pyqtSignal()
    def createTrain(self):
        self.trainModelCreation.emit()

    trainModelRouteNames = pyqtSignal(list)
    def route(self, r):
        self.route_passthrough = [r, self.suggestedSpeed_passthrough, self.authority_passthrough]
        self.trainModelRouteNames.emit(self.route_passthrough)

    trainModelAuthority = pyqtSignal(list)
    def authority(self, authority):
        # print(authority)
        self.authority_passthrough = authority
        # self.trainModelBlockLengths.emit(authority)

    trainModelSuggestedSpeed = pyqtSignal(list)
    def suggestedSpeed(self,suggestedSpeed):
        self.suggestedSpeed_passthrough = suggestedSpeed
        # self.trainModelStationStops.emit(suggestedSpeed)
        # self.trainModelAuthority.emit(authorityInM

    trainModelStopAtBlocks = pyqtSignal(list)
    def stopAtBlocks(self,stopBlocks):
        self.trainModelStopAtBlocks.emit(stopBlocks)
        


class functionalUI(Ui_Form):
    def __init__(self) -> None:
        super().__init__()
        self.trackModel = TrackModel()

    def connect(self):
        self.comboBox_3.textActivated.connect(self.lineChange)
        self.comboBox_4.textActivated.connect(self.blockChange)
        self.comboBox_4.textActivated.connect(self.updateModel)

        self.pushButton.clicked.connect(self.toggleBrokenRail)
        self.pushButton_2.clicked.connect(self.uploadTrack)
        self.pushButton_3.clicked.connect(self.toggleTrackCircuitFailure)
        self.pushButton_4.clicked.connect(self.togglePowerFailure)

        self.lineEdit.returnPressed.connect(self.tbChange)
        self.lineEdit.returnPressed.connect(self.updateMap)

        self.trackModel.trackModelUpdates.connect(self.updateModel)

    def updateModel(self):
        self.updateMap()
        self.listWidgetChange()
        if self.comboBox_4.count() != 0:
            self.blockChange()

    def tbChange(self):
        tbInfo = self.lineEdit.displayText().split(',')

        line = self.trackModel.getLine(tbInfo[0])
        tbInfo.pop(0)

        for blk in line.blocks:
            blk.occupied = False

        for blk in tbInfo:
            line.getBlock(blk).occupied = True

        self.updateModel()

    def listWidgetChange(self):
        self.listWidget_2.clear()
        currentLineName = self.comboBox_3.currentText()

        if (currentLineName != ''):
            line = self.trackModel.getLine(currentLineName)
            self.listWidget_2.addItems(line.getOccupiedBlockNames())

    def lineChange(self):
        #Clear the Blocks
        self.comboBox_4.clear()


        # Add the blocks associated with that line
        currentLineName = self.comboBox_3.currentText()
        line = self.trackModel.getLine(currentLineName)
        self.comboBox_4.addItems(line.getBlockNames())

        self.listWidgetChange()

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

        #Signal
        if(b.signal[0]):
            self.tableWidget_3.item(10,0).setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.tableWidget_3.item(10,0).setCheckState(QtCore.Qt.CheckState.Unchecked)

        #Track Heater
        if(b.trackHeater):
            self.tableWidget_3.item(11,0).setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.tableWidget_3.item(11,0).setCheckState(QtCore.Qt.CheckState.Unchecked)

        #Broken Rail
        if(b.brokenRail):
            self.tableWidget_3.item(12,0).setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.tableWidget_3.item(12,0).setCheckState(QtCore.Qt.CheckState.Unchecked)

        #Track Circuit Failure
        if(b.trackCircuitFailure):
            self.tableWidget_3.item(13,0).setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.tableWidget_3.item(13,0).setCheckState(QtCore.Qt.CheckState.Unchecked)

        #Power Failure
        if(b.powerFailure):
            self.tableWidget_3.item(14,0).setCheckState(QtCore.Qt.CheckState.Checked)
        else:
            self.tableWidget_3.item(14,0).setCheckState(QtCore.Qt.CheckState.Unchecked)

    def uploadTrack(self):
        fd = QFileDialog()
        path, _ = fd.getOpenFileName(None, 'Select a file:')
        self.trackModel.addLine(path)

        self.comboBox_3.clear()
        self.comboBox_3.addItems(self.trackModel.getLineNames())

        self.trackModel.initTrack()
        self.updateMap()
        plt.show()
      
    def toggleBrokenRail(self):
        currentBlockName = self.comboBox_4.currentText()
        currentLineName = self.comboBox_3.currentText()

        if (currentBlockName == '') or (currentLineName == ''):
            return

        blk = self.trackModel.getLine(currentLineName).getBlock(currentBlockName)

        if(blk.trackCircuitFailure or blk.powerFailure):
            return
        
        if(blk.brokenRail):
            blk.clearOccupied()
        else:
            blk.setOccupied()

        blk.brokenRail = not blk.brokenRail

        self.updateModel()

    def toggleTrackCircuitFailure(self):
        currentBlockName = self.comboBox_4.currentText()
        currentLineName = self.comboBox_3.currentText()

        if(currentBlockName == '') or (currentLineName == ''):
            return

        blk = self.trackModel.getLine(currentLineName).getBlock(currentBlockName)

        if(blk.brokenRail or blk.powerFailure):
            return
        
        if(blk.trackCircuitFailure):
            blk.clearOccupied()
        else:
            blk.setOccupied()
            
        blk.trackCircuitFailure = not blk.trackCircuitFailure

        self.updateModel()

    def togglePowerFailure(self):
        currentBlockName = self.comboBox_4.currentText()
        currentLineName = self.comboBox_3.currentText()

        if(currentBlockName == '') or (currentLineName == ''):
            return

        blk = self.trackModel.getLine(currentLineName).getBlock(currentBlockName)

        if(blk.brokenRail or blk.trackCircuitFailure):
            return
        
        if(blk.powerFailure):
            blk.clearOccupied()
        else:
            blk.setOccupied()
            
        blk.powerFailure = not blk.powerFailure

        self.updateModel()
    
    def updateMap(self):
        for i in range(len(self.trackModel.lines)):
            self.trackModel.lines[i].designMap(self.comboBox_4.currentText(), i+1)

    def update_time(self):
        self.trackModel.emitOccupancy()
        # self.trackModel.emitStationBeacon()
        # self.trackModel.emitSwitchBeacon()
        # self.trackModel.emitApproachingBeacon()
        # self.trackModel.authority()
        # self.trackModel.getTicketsSales()
        self.trackModel.polarity()
        self.trackModel.grade()







if __name__ == '__main__':
    app = QApplication([])
    MainWindow = QWidget()
    ui = functionalUI()
    ui.setupUi(MainWindow)
    ui.connect()
    MainWindow.show()

    # Start the event loop.
    app.exec()
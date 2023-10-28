import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QTableWidgetItem
from TrackController import Ui_MainWindow

import Track
from Track import *
import Wayside
from Wayside import *
import Block
from Block import *

class SoftwareTrackControllerGUI(QMainWindow):


    def __init__(self):
        super().__init__()
        self.init_ui()

        #Set default pixmaps
        self.ui.switchDirection.setPixmap(left)
        self.ui.crossroadStatus.setPixmap(open)
        #Set default text
        self.ui.wayside.addItem("Green 1")
        self.ui.wayside.addItem("Green 2")
        self.ui.wayside.addItem("Green 3")
        self.ui.wayside.addItem("Green 4")
        self.ui.waysideTB.addItem("Green 1")
        self.ui.waysideTB.addItem("Green 2")
        self.ui.waysideTB.addItem("Green 3")
        self.ui.waysideTB.addItem("Green 4")
        for i in range(len(side[0].blocks)):
            self.ui.block.addItem(side[0].blocks[i].name)
        for i in range(len(side[0].blocks)):
            self.ui.blockTB.addItem(side[0].blocks[i].name)
        self.ui.waysideData.setText("Green 1")
        self.ui.blockData.setText("A1")
        self.ui.failureData.setText("No failure")
        self.ui.stationData.setText("No")
        self.ui.switchFrame.hide()
        self.ui.crossroadFrame.hide()
        self.setOccupied()
        #Switch Toggle Signal
        self.ui.toggleDirection.clicked.connect(self.toggle_direction_handler)
        #Crossroad Toggle Signal
        self.ui.toggleCrossroad.clicked.connect(self.toggle_crossroad_handler)
        #Green button
        self.ui.greenButton.clicked.connect(self.green_handler)
        #Red button
        self.ui.redButton.clicked.connect(self.red_handler)
        #Change Wayside
        self.ui.wayside.currentIndexChanged.connect(self.new_wayside)
        #Change Block
        self.ui.block.currentIndexChanged.connect(self.new_block)
        #Set occupied
        self.ui.tab.currentChanged.connect(self.setOccupied)
        #Mode
        self.ui.modeButton.toggled.connect(self.mode_handler)
        #TB
        self.ui.occupationTB.stateChanged.connect(self.TB_o_handler)
        self.ui.waysideTB.currentIndexChanged.connect(self.TB_w_handler)
        self.ui.blockTB.currentIndexChanged.connect(self.TB_b_handler)

    def TB_o_handler(self):
        way = self.ui.waysideTB.currentIndex()
        blo = self.ui.blockTB.currentIndex()
        side[way].blocks[blo].setOccupancy(self.ui.occupationTB.isChecked())

    def TB_w_handler(self):
        way = self.ui.waysideTB.currentIndex()
        blo = 0
        self.ui.blockTB.clear()
        for i in range(len(side[way].blocks)):
            self.ui.blockTB.addItem(side[way].blocks[i].name)
        self.ui.occupationTB.setChecked(side[way].blocks[blo].getOccupancy())
    
    def TB_b_handler(self):
        way = self.ui.waysideTB.currentIndex()
        blo = self.ui.blockTB.currentIndex()
        self.ui.occupationTB.setChecked(side[way].blocks[blo].getOccupancy())

    

    def toggle_direction_handler(self):
        #Get current block and wayside
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        #If left turn right if right turn left
        if(side[way].blocks[blo].getSwitch()):
            side[way].blocks[blo].setSwitch(False)
            self.ui.switchDirection.setPixmap(left)
        else:
            side[way].blocks[blo].setSwitch(True)
            self.ui.switchDirection.setPixmap(right)
    
    def toggle_crossroad_handler(self):
        #Get current block and wayside
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        #If open close if closed open
        if(side[way].blocks[blo].getCrossroad()):
            side[way].blocks[blo].setCrossroad(False)
            self.ui.crossroadStatus.setPixmap(open)
        else:
            side[way].blocks[blo].setCrossroad(True)
            self.ui.crossroadStatus.setPixmap(closed)
        

    def green_handler(self):
        #Get current block and wayside
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        #If red change green
        if(side[way].blocks[blo].getSignal()):
            side[way].blocks[blo].setSignal(False)
            self.ui.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")

    def red_handler(self):
        #Get current block and wayside
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        #If Green change red
        if(not side[way].blocks[blo].getSignal()):
            side[way].blocks[blo].setSignal(True)
            self.ui.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")

    def new_wayside(self):
        #Get current wayside and block index is zero
        way = self.ui.wayside.currentIndex()
        blo = 0
        #Create new block list
        self.ui.block.clear()
        for i in range(len(side[way].blocks)):
            self.ui.block.addItem(side[way].blocks[i].name)
        #Set the lables of block wayside and occupation
        self.ui.waysideData.setText(side[way].name)
        self.ui.blockData.setText(side[way].blocks[blo].name)
        if(side[way].blocks[blo].getHasStation()):
            self.ui.stationData.setText("Yes")
        else:
            self.ui.stationData.setText("No")
        #Switch Update
        if(side[way].blocks[blo].getHasSwitch()):
            #If there is a switch set data and show frame
            if(side[way].blocks[blo].getSwitch()):
                self.ui.switchDirection.setPixmap(right)
            else:
                self.ui.switchDirection.setPixmap(left)
            self.ui.leftBlock.setText(side[way].blocks[blo].getLeft())
            self.ui.rightBlock.setText(side[way].blocks[blo].getRight())
            self.ui.switchFrame.show()
        else:
            self.ui.switchFrame.hide()
        #Crossroad Update
        if(side[way].blocks[blo].getHasCrossroad()):
            #If there is a crossroad set image and show frame
            if(side[way].blocks[blo].getCrossroad()):
                self.ui.crossroadStatus.setPixmap(closed)
            else:
                self.ui.crossroadStatus.setPixmap(open)
            self.ui.crossroadFrame.show()
        else:
            self.ui.crossroadFrame.hide()
        if(side[way].blocks[blo].getHasSignal()):
            #If there is a signal set color and show frame
            if(side[way].blocks[blo].getSignal()):
                self.ui.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")
            else:
                self.ui.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.ui.signalFrame.show()
        else:
            self.ui.signalFrame.hide()



    def new_block(self):
        #Get current wayside and block index
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        #Set data lables
        self.ui.waysideData.setText(side[way].name)
        self.ui.blockData.setText(side[way].blocks[blo].name)
        if(side[way].blocks[blo].getHasStation()):
            self.ui.stationData.setText("Yes")
        else:
            self.ui.stationData.setText("No")
        #Switch Update
        if(side[way].blocks[blo].getHasSwitch()):
            #If there is a switch set data and show frame
            if(side[way].blocks[blo].getSwitch()):
                self.ui.switchDirection.setPixmap(right)
            else:
                self.ui.switchDirection.setPixmap(left)
            self.ui.leftBlock.setText(side[way].blocks[blo].getLeft())
            self.ui.rightBlock.setText(side[way].blocks[blo].getRight())
            self.ui.switchFrame.show()
        else:
            self.ui.switchFrame.hide()
        #Crossroad Update
        if(side[way].blocks[blo].getHasCrossroad()):
            #If there is a crossroad set image and show frame
            if(side[way].blocks[blo].getCrossroad()):
                self.ui.crossroadStatus.setPixmap(closed)
            else:
                self.ui.crossroadStatus.setPixmap(open)
            self.ui.crossroadFrame.show()
        else:
            self.ui.crossroadFrame.hide()
        if(side[way].blocks[blo].getHasSignal()):
            #If there is a signal set color and show frame
            if(side[way].blocks[blo].getSignal()):
                self.ui.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")
            else:
                self.ui.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.ui.signalFrame.show()
        else:
            self.ui.signalFrame.hide()

    def mode_handler(self):
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        self.ui.switchDirection.setPixmap(left)

    def setOccupied(self):
        self.ui.occupationData.clear()
        names = whole.getOccupancy()
        for i in range (len(names)):
            self.ui.occupationData.addItem(names[i])

    def init_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #Required pixmaps created after application
    left = QPixmap("left.jpg")
    right = QPixmap("light.jpg")
    open = QPixmap("crosso.jpg")
    closed = QPixmap("crossc.jpg")
    #Creating Track Map
    side:Wayside = [Wayside(), Wayside(), Wayside(), Wayside()]
    side[0].name = "Green 1"
    side[1].name = "Green 2"
    side[2].name = "Green 3"
    side[3].name = "Green 4"
    side[0].addBlock(False, False, True, False, "A1") #Signal
    side[0].addBlock(False, False, False, True, "A2") #Station
    side[0].addBlock(False, False, False, False, "A3")
    side[0].addBlock(False, False, False, False, "B4") 
    side[0].addBlock(False, False, False, False, "B5")
    side[0].addBlock(False, False, False, False, "B6")
    side[0].addBlock(False, False, False, False, "B7")
    side[0].addBlock(False, False, False, False, "B8")
    side[0].addBlock(False, False, False, True, "C9") #Station
    side[0].addBlock(False, False, False, False, "C10")
    side[0].addBlock(False, False, False, False, "C11")
    side[0].addBlock(False, False, False, False, "C12") 
    side[0].addBlock(True, False, True, False, "D13", "C12", "A1") #Switch, Signal
    side[0].addBlock(False, False, False, False, "D14")
    side[0].addBlock(False, False, False, False, "D15")
    side[0].addBlock(False, False, False, True, "D16") #Station
    side[0].addBlock(False, False, False, False, "E17")
    side[0].addBlock(False, False, False, False, "E18")
    side[0].addBlock(False, True, False, False, "E19") #Crossroad
    side[0].addBlock(False, False, False, False, "E20") 
    side[0].addBlock(False, False, False, False, "F21") 
    side[0].addBlock(False, False, False, True, "F22") #Station
    side[0].addBlock(False, False, False, False, "F23") 
    side[0].addBlock(False, False, False, False, "F24")
    side[0].addBlock(False, False, False, False, "F25") 
    side[0].addBlock(False, False, False, False, "F26")
    side[0].addBlock(False, False, False, False, "F27")
    side[0].addBlock(False, False, False, False, "F28")
    side[0].addBlock(True, False, True, False, "G29", "G30", "Z150") #Switch, Signal
    side[0].addBlock(False, False, False, False, "G30")
    side[0].addBlock(False, False, False, True, "G31") #Station
    side[0].addBlock(False, False, False, False, "G32")
    side[1].addBlock(False, False, False, False, "H33")
    side[1].addBlock(False, False, False, False, "H34")
    side[1].addBlock(False, False, False, False, "H35")
    side[1].addBlock(False, False, False, False, "I36")
    side[1].addBlock(False, False, False, False, "I37")
    side[1].addBlock(False, False, False, False, "I38")
    side[1].addBlock(False, False, False, True, "I39") #Station
    side[1].addBlock(False, False, False, False, "I40")
    side[1].addBlock(False, False, False, False, "I41") 
    side[1].addBlock(False, False, False, False, "I42")
    side[1].addBlock(False, False, False, False, "I43")
    side[1].addBlock(False, False, False, False, "I44")
    side[1].addBlock(False, False, False, False, "I45")
    side[1].addBlock(False, False, False, False, "I46")
    side[1].addBlock(False, False, False, False, "I47")
    side[1].addBlock(False, False, False, True, "I48") #Station
    side[1].addBlock(False, False, False, False, "I49")
    side[1].addBlock(False, False, False, False, "I50")
    side[1].addBlock(False, False, False, False, "I51")
    side[1].addBlock(False, False, False, False, "I52")
    side[1].addBlock(False, False, False, False, "I53")
    side[1].addBlock(False, False, False, False, "I54") 
    side[1].addBlock(False, False, False, False, "I55")
    side[1].addBlock(False, False, False, False, "I56")
    side[1].addBlock(False, False, False, True, "I57") #Station
    side[1].addBlock(True, False, True, False, "J58", "YARD", "J59") #Switch, Signal
    side[1].addBlock(False, False, False, False, "J59")
    side[1].addBlock(False, False, False, False, "J60")
    side[1].addBlock(False, False, True, False, "J61") #Signal
    side[1].addBlock(True, False, False, False, "J62", "J61", "YARD") #switch
    side[1].addBlock(False, False, False, False, "K63")
    side[1].addBlock(False, False, False, False, "K64")
    side[1].addBlock(False, False, False, True, "K65") #Station
    side[1].addBlock(False, False, False, False, "K66")
    side[1].addBlock(False, False, False, False, "K67")
    side[1].addBlock(False, False, False, False, "K68")
    side[1].addBlock(False, False, False, False, "L69")
    side[1].addBlock(False, False, False, False, "L70")
    side[1].addBlock(False, False, False, False, "L71")
    side[1].addBlock(False, False, False, False, "L72")
    side[1].addBlock(False, False, False, True, "L73") #Station
    side[2].addBlock(False, False, False, False, "M74")
    side[2].addBlock(False, False, False, False, "M75")
    side[2].addBlock(False, False, True, False, "M76") #Signal
    side[2].addBlock(True, False, True, True, "N77", "R101", "M76") #Switch, Signal, Station
    side[2].addBlock(False, False, False, False, "N78")
    side[2].addBlock(False, False, False, False, "N79")
    side[2].addBlock(False, False, False, False, "N80")
    side[2].addBlock(False, False, False, False, "N81")
    side[2].addBlock(False, False, False, False, "N82")
    side[2].addBlock(False, False, False, False, "N83")
    side[2].addBlock(False, False, False, False, "N84")
    side[2].addBlock(True, False, True, False, "N85", "O86", "Q100") #Switch, Signal
    side[2].addBlock(False, False, False, False, "O86")
    side[2].addBlock(False, False, False, False, "O87")
    side[2].addBlock(False, False, False, True, "O88") #Station
    side[2].addBlock(False, False, False, False, "P89")
    side[2].addBlock(False, False, False, False, "P90")
    side[2].addBlock(False, False, False, False, "P91")
    side[2].addBlock(False, False, False, False, "P92")
    side[2].addBlock(False, False, False, False, "P93")
    side[2].addBlock(False, False, False, False, "P94")
    side[2].addBlock(False, False, False, False, "P95")
    side[2].addBlock(False, False, False, True, "P96") #Station
    side[2].addBlock(False, False, False, False, "P97")
    side[2].addBlock(False, False, False, False, "Q98")
    side[2].addBlock(False, False, False, False, "Q99")
    side[2].addBlock(False, False, True, False, "Q100") #Signal
    side[2].addBlock(False, False, False, False, "R101")
    side[3].addBlock(False, False, False, False, "S102")
    side[3].addBlock(False, False, False, False, "S103")
    side[3].addBlock(False, False, False, False, "S104")
    side[3].addBlock(False, False, False, True, "T105") #Station
    side[3].addBlock(False, False, False, False, "T106")
    side[3].addBlock(False, False, False, False, "T107")
    side[3].addBlock(False, False, False, False, "T108")
    side[3].addBlock(False, False, False, False, "T109")
    side[3].addBlock(False, False, False, False, "U110")
    side[3].addBlock(False, False, False, False, "U111")
    side[3].addBlock(False, False, False, False, "U112")
    side[3].addBlock(False, False, False, False, "U113")
    side[3].addBlock(False, False, False, True, "U114") #Station
    side[3].addBlock(False, False, False, False, "U115")
    side[3].addBlock(False, False, False, False, "U116")
    side[3].addBlock(False, False, False, False, "V117")
    side[3].addBlock(False, False, False, False, "V118")
    side[3].addBlock(False, False, False, False, "V119")
    side[3].addBlock(False, False, False, False, "V120")
    side[3].addBlock(False, False, False, False, "V121")
    side[3].addBlock(False, False, False, False, "W122")
    side[3].addBlock(False, False, False, True, "W123") #Station
    side[3].addBlock(False, False, False, False, "W124")
    side[3].addBlock(False, False, False, False, "W125")
    side[3].addBlock(False, False, False, False, "W126")
    side[3].addBlock(False, False, False, False, "W127")
    side[3].addBlock(False, False, False, False, "W128")
    side[3].addBlock(False, False, False, False, "W129")
    side[3].addBlock(False, False, False, False, "W130")
    side[3].addBlock(False, False, False, False, "W131")
    side[3].addBlock(False, False, False, True, "W132") #Station
    side[3].addBlock(False, False, False, False, "W133")
    side[3].addBlock(False, False, False, False, "W134")
    side[3].addBlock(False, False, False, False, "W135")
    side[3].addBlock(False, False, False, False, "W136")
    side[3].addBlock(False, False, False, False, "W137")
    side[3].addBlock(False, False, False, False, "W138")
    side[3].addBlock(False, False, False, False, "W139")
    side[3].addBlock(False, False, False, False, "W140")
    side[3].addBlock(False, False, False, True, "W141") #Station
    side[3].addBlock(False, False, False, False, "W142")
    side[3].addBlock(False, False, False, False, "W143")
    side[3].addBlock(False, False, False, False, "X144")
    side[3].addBlock(False, False, False, False, "X145")
    side[3].addBlock(False, False, False, False, "X146")
    side[3].addBlock(False, False, False, False, "Y147")
    side[3].addBlock(False, False, False, False, "Y148")
    side[3].addBlock(False, False, False, False, "Y149")
    side[0].addBlock(False, False, True, False, "Z150") #Signal
    side[1].addBlock(False, False, True, False, "YARD") #Signal
    side[0].blocks[0].setOccupancy(True)
    whole = Track(side)
    data = whole.getData()
    x = []
    for i in range(151):
        x.append(False)
    x[150] = True
    whole.setOccupancy(x)
    ###########################################
    MainWindow = SoftwareTrackControllerGUI()
    MainWindow.show()
    sys.exit(app.exec())
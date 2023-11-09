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
        for i in range(len(side)):
            self.ui.wayside.addItem(side[i].getName())
            self.ui.waysideTB.addItem(side[i].getName())
        for i in range(len(side[0].blocks)):
            self.ui.block.addItem(side[0].getBlock(i).name)
        for i in range(len(side[0].blocks)):
            self.ui.blockTB.addItem(side[0].getBlock(i).name)
        self.ui.waysideData.setText(side[0].getName())
        self.ui.blockData.setText(side[0].getBlock(0).getName())
        self.ui.failureData.setText("No failure")
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
        side[way].getBlock(blo).setOccupancy(self.ui.occupationTB.isChecked())

    def TB_w_handler(self):
        way = self.ui.waysideTB.currentIndex()
        blo = 0
        self.ui.blockTB.clear()
        for i in range(len(side[way].blocks)):
            self.ui.blockTB.addItem(side[way].getBlock(i).name)
        self.ui.occupationTB.setChecked(side[way].getBlock(blo).getOccupancy())
    
    def TB_b_handler(self):
        way = self.ui.waysideTB.currentIndex()
        blo = self.ui.blockTB.currentIndex()
        self.ui.occupationTB.setChecked(side[way].getBlock(blo).getOccupancy())

    

    def toggle_direction_handler(self):
        #Get current block and wayside
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        #If left turn right if right turn left
        if(side[way].getBlock(blo).getSwitch()):
            side[way].getBlock(blo).setSwitch(False)
            self.ui.switchDirection.setPixmap(left)
        else:
            side[way].getBlock(blo).setSwitch(True)
            self.ui.switchDirection.setPixmap(right)
    
    def toggle_crossroad_handler(self):
        #Get current block and wayside
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        #If open close if closed open
        if(side[way].getBlock(blo).getCrossroad()):
            side[way].getBlock(blo).setCrossroad(False)
            self.ui.crossroadStatus.setPixmap(open)
        else:
            side[way].getBlock(blo).setCrossroad(True)
            self.ui.crossroadStatus.setPixmap(closed)
        

    def green_handler(self):
        #Get current block and wayside
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        #If red change green
        if(not side[way].getBlock(blo).getSignal()):
            side[way].getBlock(blo).setSignal(True)
            self.ui.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")

    def red_handler(self):
        #Get current block and wayside
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        #If Green change red
        if(side[way].getBlock(blo).getSignal()):
            side[way].getBlock(blo).setSignal(False)
            self.ui.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")

    def new_wayside(self):
        #Get current wayside and block index is zero
        way = self.ui.wayside.currentIndex()
        blo = 0
        #Create new block list
        self.ui.block.clear()
        for i in range(len(side[way].blocks)):
            self.ui.block.addItem(side[way].getBlock(i).name)
        #Set the lables of block wayside and occupation
        self.ui.waysideData.setText(side[way].name)
        self.ui.blockData.setText(side[way].getBlock(blo).name)
        #Switch Update
        if(side[way].getBlock(blo).getHasSwitch()):
            #If there is a switch set data and show frame
            if(side[way].getBlock(blo).getSwitch()):
                self.ui.switchDirection.setPixmap(right)
            else:
                self.ui.switchDirection.setPixmap(left)
            self.ui.leftBlock.setText(side[way].getBlock(blo).getLeft())
            self.ui.rightBlock.setText(side[way].getBlock(blo).getRight())
            self.ui.switchFrame.show()
        else:
            self.ui.switchFrame.hide()
        #Crossroad Update
        if(side[way].getBlock(blo).getHasCrossroad()):
            #If there is a crossroad set image and show frame
            if(side[way].getBlock(blo).getCrossroad()):
                self.ui.crossroadStatus.setPixmap(closed)
            else:
                self.ui.crossroadStatus.setPixmap(open)
            self.ui.crossroadFrame.show()
        else:
            self.ui.crossroadFrame.hide()
        if(side[way].getBlock(blo).getHasSignal()):
            #If there is a signal set color and show frame
            if(side[way].getBlock(blo).getSignal()):
                self.ui.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")
            else:
                self.ui.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.ui.signalFrame.show()
        else:
            self.ui.signalFrame.hide()



    def new_block(self):
        #Get current wayside and block index
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        #Set data lables
        self.ui.waysideData.setText(side[way].name)
        self.ui.blockData.setText(side[way].getBlock(blo).name)
        #Switch Update
        if(side[way].getBlock(blo).getHasSwitch()):
            #If there is a switch set data and show frame
            if(side[way].getBlock(blo).getSwitch()):
                self.ui.switchDirection.setPixmap(right)
            else:
                self.ui.switchDirection.setPixmap(left)
            self.ui.leftBlock.setText(side[way].getBlock(blo).getLeft())
            self.ui.rightBlock.setText(side[way].getBlock(blo).getRight())
            self.ui.switchFrame.show()
        else:
            self.ui.switchFrame.hide()
        #Crossroad Update
        if(side[way].getBlock(blo).getHasCrossroad()):
            #If there is a crossroad set image and show frame
            if(side[way].getBlock(blo).getCrossroad()):
                self.ui.crossroadStatus.setPixmap(closed)
            else:
                self.ui.crossroadStatus.setPixmap(open)
            self.ui.crossroadFrame.show()
        else:
            self.ui.crossroadFrame.hide()
        if(side[way].getBlock(blo).getHasSignal()):
            #If there is a signal set color and show frame
            if(side[way].getBlock(blo).getSignal()):
                self.ui.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")
            else:
                self.ui.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.ui.signalFrame.show()
        else:
            self.ui.signalFrame.hide()

    def mode_handler(self):
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        self.ui.switchDirection.setPixmap(left)

    def setOccupied(self):
        self.ui.occupationData.clear()
        #names = whole.getOccupancy()
        #for i in range (len(names)):
        #    self.ui.occupationData.addItem(names[i])

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
    side:Wayside = [Wayside("Green 1"), Wayside("Green 2"), Wayside("Green 3"), Wayside("Green 4")]

    side[0].addBlock(False, False, True, "A1") #Signal
    side[0].addBlock(False, False, False, "A2")
    side[0].addBlock(False, False, False, "A3")
    side[0].addBlock(False, False, False, "B4") 
    side[0].addBlock(False, False, False, "B5")
    side[0].addBlock(False, False, False, "B6")
    side[0].addBlock(False, False, False, "B7")
    side[0].addBlock(False, False, False, "B8")
    side[0].addBlock(False, False, False, "C9")
    side[0].addBlock(False, False, False, "C10")
    side[0].addBlock(False, False, False, "C11")
    side[0].addBlock(False, False, False, "C12") 
    side[0].addBlock(True, False, True, "D13", "C12", "A1") #Switch, Signal
    side[0].addBlock(False, False, False, "D14")
    side[0].addBlock(False, False, False, "D15")
    side[0].addBlock(False, False, False, "D16")
    side[0].addBlock(False, False, False, "E17")
    side[0].addBlock(False, False, False, "E18")
    side[0].addBlock(False, True, False, "E19") #Crossroad
    side[0].addBlock(False, False, False, "E20") 
    side[0].addBlock(False, False, False, "F21") 
    side[0].addBlock(False, False, False, "F22")
    side[0].addBlock(False, False, False, "F23") 
    side[0].addBlock(False, False, False, "F24")
    side[0].addBlock(False, False, False, "F25") 
    side[0].addBlock(False, False, False, "F26")
    side[0].addBlock(False, False, False, "F27")
    side[0].addBlock(False, False, False, "F28")
    side[0].addBlock(True, False, True, "G29", "G30", "Z150") #Switch, Signal
    side[0].addBlock(False, False, False, "G30")
    side[0].addBlock(False, False, False, "G31")
    side[0].addBlock(False, False, False, "G32")
    side[1].addBlock(False, False, False, "H33")
    side[1].addBlock(False, False, False, "H34")
    side[1].addBlock(False, False, False, "H35")
    side[1].addBlock(False, False, False, "I36")
    side[1].addBlock(False, False, False, "I37")
    side[1].addBlock(False, False, False, "I38")
    side[1].addBlock(False, False, False, "I39")
    side[1].addBlock(False, False, False, "I40")
    side[1].addBlock(False, False, False, "I41") 
    side[1].addBlock(False, False, False, "I42")
    side[1].addBlock(False, False, False, "I43")
    side[1].addBlock(False, False, False, "I44")
    side[1].addBlock(False, False, False, "I45")
    side[1].addBlock(False, False, False, "I46")
    side[1].addBlock(False, False, False, "I47")
    side[1].addBlock(False, False, False, "I48") #Station
    side[1].addBlock(False, False, False, "I49")
    side[1].addBlock(False, False, False, "I50")
    side[1].addBlock(False, False, False, "I51")
    side[1].addBlock(False, False, False, "I52")
    side[1].addBlock(False, False, False, "I53")
    side[1].addBlock(False, False, False, "I54") 
    side[1].addBlock(False, False, False, "I55")
    side[1].addBlock(False, False, False, "I56")
    side[1].addBlock(False, False, False, "I57")
    side[1].addBlock(True, False, True, "J58", "YARD", "J59") #Switch, Signal
    side[1].addBlock(False, False, False, "J59")
    side[1].addBlock(False, False, False, "J60")
    side[1].addBlock(False, False, True, "J61") #Signal
    side[1].addBlock(True, False, False, "J62", "J61", "YARD") #switch
    side[1].addBlock(False, False, False, "K63")
    side[1].addBlock(False, False, False, "K64")
    side[1].addBlock(False, False, False, "K65")
    side[1].addBlock(False, False, False, "K66")
    side[1].addBlock(False, False, False, "K67")
    side[1].addBlock(False, False, False, "K68")
    side[1].addBlock(False, False, False, "L69")
    side[1].addBlock(False, False, False, "L70")
    side[1].addBlock(False, False, False, "L71")
    side[1].addBlock(False, False, False, "L72")
    side[1].addBlock(False, False, False, "L73")
    side[2].addBlock(False, False, False, "M74")
    side[2].addBlock(False, False, False, "M75")
    side[2].addBlock(False, False, True, "M76") #Signal
    side[2].addBlock(True, False, True, "N77", "R101", "M76") #Switch, Signal
    side[2].addBlock(False, False, False,"N78")
    side[2].addBlock(False, False, False,"N79")
    side[2].addBlock(False, False, False,"N80")
    side[2].addBlock(False, False, False,"N81")
    side[2].addBlock(False, False, False, "N82")
    side[2].addBlock(False, False, False, "N83")
    side[2].addBlock(False, False, False, "N84")
    side[2].addBlock(True, False, True, "N85", "O86", "Q100") #Switch, Signal
    side[2].addBlock(False, False, False, "O86")
    side[2].addBlock(False, False, False, "O87")
    side[2].addBlock(False, False, False, "O88") #Station
    side[2].addBlock(False, False, False, "P89")
    side[2].addBlock(False, False, False, "P90")
    side[2].addBlock(False, False, False, "P91")
    side[2].addBlock(False, False, False, "P92")
    side[2].addBlock(False, False, False, "P93")
    side[2].addBlock(False, False, False, "P94")
    side[2].addBlock(False, False, False, "P95")
    side[2].addBlock(False, False, False, "P96")
    side[2].addBlock(False, False, False, "P97")
    side[2].addBlock(False, False, False, "Q98")
    side[2].addBlock(False, False, False, "Q99")
    side[2].addBlock(False, False, True, "Q100") #Signal
    side[2].addBlock(False, False, False, "R101")
    side[3].addBlock(False, False, False, "S102")
    side[3].addBlock(False, False, False, "S103")
    side[3].addBlock(False, False, False, "S104")
    side[3].addBlock(False, False, False, "T105")
    side[3].addBlock(False, False, False, "T106")
    side[3].addBlock(False, False, False, "T107")
    side[3].addBlock(False, False, False, "T108")
    side[3].addBlock(False, False, False, "T109")
    side[3].addBlock(False, False, False, "U110")
    side[3].addBlock(False, False, False, "U111")
    side[3].addBlock(False, False, False, "U112")
    side[3].addBlock(False, False, False, "U113")
    side[3].addBlock(False, False, False, "U114")
    side[3].addBlock(False, False, False, "U115")
    side[3].addBlock(False, False, False, "U116")
    side[3].addBlock(False, False, False, "V117")
    side[3].addBlock(False, False, False, "V118")
    side[3].addBlock(False, False, False, "V119")
    side[3].addBlock(False, False, False, "V120")
    side[3].addBlock(False, False, False, "V121")
    side[3].addBlock(False, False, False, "W122")
    side[3].addBlock(False, False, False, "W123")
    side[3].addBlock(False, False, False, "W124")
    side[3].addBlock(False, False, False, "W125")
    side[3].addBlock(False, False, False, "W126")
    side[3].addBlock(False, False, False, "W127")
    side[3].addBlock(False, False, False, "W128")
    side[3].addBlock(False, False, False, "W129")
    side[3].addBlock(False, False, False, "W130")
    side[3].addBlock(False, False, False, "W131")
    side[3].addBlock(False, False, False, "W132")
    side[3].addBlock(False, False, False, "W133")
    side[3].addBlock(False, False, False, "W134")
    side[3].addBlock(False, False, False, "W135")
    side[3].addBlock(False, False, False, "W136")
    side[3].addBlock(False, False, False, "W137")
    side[3].addBlock(False, False, False, "W138")
    side[3].addBlock(False, False, False, "W139")
    side[3].addBlock(False, False, False, "W140")
    side[3].addBlock(False, False, False, "W141")
    side[3].addBlock(False, False, False, "W142")
    side[3].addBlock(False, False, False, "W143")
    side[3].addBlock(False, False, False, "X144")
    side[3].addBlock(False, False, False, "X145")
    side[3].addBlock(False, False, False, "X146")
    side[3].addBlock(False, False, False, "Y147")
    side[3].addBlock(False, False, False, "Y148")
    side[3].addBlock(False, False, False, "Y149")
    side[0].addBlock(False, False, True, "Z150") #Signal
    side[1].addBlock(False, False, False, "Z151")

    #whole = Track(side)
    #data = whole.getData()
    ###########################################
    MainWindow = SoftwareTrackControllerGUI()
    MainWindow.show()
    sys.exit(app.exec())
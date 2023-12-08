import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow
from PyQt6.QtCore import QTimer, pyqtSignal, QObject
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QTableWidgetItem
from Software_Track_Controller.TrackController import Ui_Form

import Software_Track_Controller.Track
from Software_Track_Controller.Track import *
import Software_Track_Controller.Wayside
from Software_Track_Controller.Wayside import *
import Software_Track_Controller.Block
from Software_Track_Controller.Block import *
import Software_Track_Controller.PLC
from Software_Track_Controller.PLC import *


class SoftwareTrackControllerGUI(Ui_Form, QObject):

    trackModelTrackDataHW = pyqtSignal(list)
    trackModelSendRouteHW = pyqtSignal(list)
    trackModelSuggestedSpeedHW = pyqtSignal(list)
    trackModelAuthorityHW = pyqtSignal(list)

    CTCOccupancyHW = pyqtSignal(list)
    CTCTrackFailuresHW = pyqtSignal(list)



    def __init__(self):
        super().__init__()
        #Creates Track On initilization
        self.line:Track = Track()

    def sendFailures(self): #Sends failures to CTC
        #Senses failures using PLC and
        fail:str = []
        self.CTCTrackFailuresHW.emit(fail)
        

    def getOccupancy(self, data): #Receives occupancy from Track Model
        #Gets occupancy and sets occupancy
        self.line.setOccupancy(data)
        #Sets new states in automatic
        self.mode_handler()
        #Sets occupied list
        self.setOccupied()
        #sends occupancy to ctc
        self.CTCOccupancyHW.emit(self.line.getOccupancy())

    def createNewTrainData(self, route, auth, speed): 
        #Receives train dispatch data from CTC and sends to Track Model
        self.trackModelAuthorityHW.emit(auth)
        self.trackModelSuggestedSpeedHW.emit(speed)
        self.trackModelSendRouteHW.emit(route)

    # def getAuth(self): 
    #     #Sends only auth to track model
    #     self.trackModelAuthority.emit(self.trainAuth.getAuth(0))

    def sendData(self): 
        #Sends track states to track Model
        self.trackModelTrackDataHW.emit(self.line.getData())
        
    def setDisplay(self, data): 
        #Inililizes waysides from Track Model
        self.side:Wayside = self.line.create(data)
        #Create logic class
        self.create = PLC(self.line.getBlocks())
        #Clears lists
        self.block.clear()
        self.wayside.clear()
        #Sets the list of waysides
        for i in range(len(self.side)):
            self.wayside.addItem(self.side[i].getName())
            # self.waysideTB.addItem(self.side[i].getName())
        #Sets the lists of block for the first wayside
        for i in range(len(self.side[0].getBlocks())):
            self.block.addItem(self.side[0].getBlock(i).getName())
            # self.blockTB.addItem(self.side[0].getBlock(i).getName())
        


    def connectFunctions(self):
        #Required pixmaps created after application
        self.left = QPixmap("left.jpg")
        self.right = QPixmap("light.jpg")
        self.open = QPixmap("crosso.jpg")
        self.closed = QPixmap("crossc.jpg")
        #Hide frames by default
        # self.switchFrame.hide()
        # self.crossroadFrame.hide()
        # self.signalFrame.hide()
        #Switch Toggle Signal
        self.toggleDirection.clicked.connect(self.toggle_direction_handler)
        #Crossroad Toggle Signal
        self.toggleCrossroad.clicked.connect(self.toggle_crossroad_handler)
        #Green button
        self.greenButton.clicked.connect(self.green_handler)
        #Red button
        self.redButton.clicked.connect(self.red_handler)
        #Change Wayside
        self.wayside.currentIndexChanged.connect(self.new_wayside)
        #Change Block
        self.block.currentIndexChanged.connect(self.new_block)
        #Mode
        self.modeButton.toggled.connect(self.mode_handler)
        #TB
        # self.occupationTB.stateChanged.connect(self.TB_o_handler)
        # self.waysideTB.currentIndexChanged.connect(self.TB_w_handler)
        # self.blockTB.currentIndexChanged.connect(self.TB_b_handler)

    # def TB_o_handler(self):
    #     way = self.waysideTB.currentIndex()
    #     blo = self.blockTB.currentIndex()
    #     self.side[way].getBlock(blo).setOccupancy(self.occupationTB.isChecked())

    # def TB_w_handler(self):
    #     way = self.waysideTB.currentIndex()
    #     blo = 0
    #     self.blockTB.clear()
    #     for i in range(len(self.side[way].getBlocks())):
    #         self.blockTB.addItem(self.side[way].getBlock(i).name)
    #     self.occupationTB.setChecked(self.side[way].getBlock(blo).getOccupied())
    
    # def TB_b_handler(self):
    #     way = self.waysideTB.currentIndex()
    #     blo = self.blockTB.currentIndex()
    #     self.occupationTB.setChecked(self.side[way].getBlock(blo).getOccupied())

    

    def toggle_direction_handler(self):
        #Get current block and wayside
        way = self.wayside.currentIndex()
        blo = self.block.currentIndex()
        #If left turn right if right turn left
        if(self.side[way].getBlock(blo).getSwitch()):
            self.side[way].getBlock(blo).setSwitch(False)
            self.switchDirection.setPixmap(self.left)
        else:
            self.side[way].getBlock(blo).setSwitch(True)
            self.switchDirection.setPixmap(self.right)
    
    def toggle_crossroad_handler(self):
        #Get current block and wayside
        way = self.wayside.currentIndex()
        blo = self.block.currentIndex()
        #If open close if closed open
        if(self.side[way].getBlock(blo).getCrossroad()):
            self.side[way].getBlock(blo).setCrossroad(False)
            self.crossroadStatus.setPixmap(self.open)
        else:
            self.side[way].getBlock(blo).setCrossroad(True)
            self.crossroadStatus.setPixmap(self.closed)
        

    def green_handler(self):
        #Get current block and wayside
        way = self.wayside.currentIndex()
        blo = self.block.currentIndex()
        #If red change green
        if(self.side[way].getBlock(blo).getSignal()):
            self.side[way].getBlock(blo).setSignal(False)
            self.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")

    def red_handler(self):
        #Get current block and wayside
        way = self.wayside.currentIndex()
        blo = self.block.currentIndex()
        #If Green change red
        if(not self.side[way].getBlock(blo).getSignal()):
            self.side[way].getBlock(blo).setSignal(True)
            self.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")

    def new_wayside(self):
        #Get current wayside and set block index zero
        way = self.wayside.currentIndex()
        blo = 0
        #Create new block list
        self.block.clear()
        for i in range(len(self.side[way].getBlocks())):
            self.block.addItem(self.side[way].getBlock(i).name)
        #Switch Update
        if(self.side[way].getBlock(blo).getHasSwitch()):
            #If there is a switch set data and show frame
            if(self.side[way].getBlock(blo).getSwitch()):
                self.switchDirection.setPixmap(self.right)
            else:
                self.switchDirection.setPixmap(self.left)
            self.leftBlock.setText(self.side[way].getBlock(blo).getLeft())
            self.rightBlock.setText(self.side[way].getBlock(blo).getRight())
            self.switchFrame.show()
        else:
            self.switchFrame.hide()
        #Crossroad Update
        if(self.side[way].getBlock(blo).getHasCrossroad()):
            #If there is a crossroad set image and show frame
            if(self.side[way].getBlock(blo).getCrossroad()):
                self.crossroadStatus.setPixmap(self.closed)
            else:
                self.crossroadStatus.setPixmap(self.open)
            self.crossroadFrame.show()
        else:
            self.crossroadFrame.hide()
        #Signal Update
        if(self.side[way].getBlock(blo).getHasSignal()):
            #If there is a signal set color and show frame
            if(not self.side[way].getBlock(blo).getSignal()):
                self.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")
            else:
                self.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.signalFrame.show()
        else:
            self.signalFrame.hide()



    def new_block(self):
        #Get current wayside and block index
        way = self.wayside.currentIndex()
        blo = self.block.currentIndex()
        #Switch Update
        if(self.side[way].getBlock(blo).getHasSwitch()):
            #If there is a switch set data and show frame
            if(self.side[way].getBlock(blo).getSwitch()):
                self.switchDirection.setPixmap(self.right)
            else:
                self.switchDirection.setPixmap(self.left)
            self.leftBlock.setText(self.side[way].getBlock(blo).getLeft())
            self.rightBlock.setText(self.side[way].getBlock(blo).getRight())
            self.switchFrame.show()
        else:
            self.switchFrame.hide()
        #Crossroad Update
        if(self.side[way].getBlock(blo).getHasCrossroad()):
            #If there is a crossroad set image and show frame
            if(self.side[way].getBlock(blo).getCrossroad()):
                self.crossroadStatus.setPixmap(self.closed)
            else:
                self.crossroadStatus.setPixmap(self.open)
            self.crossroadFrame.show()
        else:
            self.crossroadFrame.hide()
        #Signal Update
        if(self.side[way].getBlock(blo).getHasSignal()):
            #If there is a signal set color and show frame
            if(not self.side[way].getBlock(blo).getSignal()):
                self.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")
            else:
                self.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.signalFrame.show()
        else:
            self.signalFrame.hide()

    def mode_handler(self):
        way = self.wayside.currentIndex()
        blo = self.block.currentIndex()
        colides = self.create.collision()
        if(self.modeButton.isChecked()):
            self.toggleDirection.hide()
            self.toggleCrossroad.hide()
            self.redButton.hide()
            self.greenButton.hide()
            self.create.logic()
            if(self.side[way].getBlock(blo).getHasSwitch()):
                #If there is a switch set data and show frame
                if(self.side[way].getBlock(blo).getSwitch()):
                    self.switchDirection.setPixmap(self.right)
                else:
                    self.switchDirection.setPixmap(self.left)
                self.leftBlock.setText(self.side[way].getBlock(blo).getLeft())
                self.rightBlock.setText(self.side[way].getBlock(blo).getRight())
                self.switchFrame.show()
            else:
                self.switchFrame.hide()
            #Crossroad Update
            if(self.side[way].getBlock(blo).getHasCrossroad()):
                #If there is a crossroad set image and show frame
                if(self.side[way].getBlock(blo).getCrossroad()):
                    self.crossroadStatus.setPixmap(self.closed)
                else:
                    self.crossroadStatus.setPixmap(self.open)
                self.crossroadFrame.show()
            else:
                self.crossroadFrame.hide()
            if(self.side[way].getBlock(blo).getHasSignal()):
                #If there is a signal set color and show frame
                if(not self.side[way].getBlock(blo).getSignal()):
                    self.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")
                else:
                    self.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")
                self.signalFrame.show()
            else:
                self.signalFrame.hide()
        else:
            self.toggleDirection.show()
            self.toggleCrossroad.show()
            self.redButton.show()
            self.greenButton.show()

    def setOccupied(self):
        self.occupationData.clear()
        names = self.line.getOccupied()
        for i in names:
            self.occupationData.addItem(i)

    def init_ui(self):
        self = Ui_Form()
        self.setupUi(self)

        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = SoftwareTrackControllerGUI()
    MainWindow.show()
    sys.exit(app.exec())



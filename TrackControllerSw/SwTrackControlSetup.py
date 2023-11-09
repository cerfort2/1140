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

        #Required pixmaps created after application
        self.left = QPixmap("left.jpg")
        self.right = QPixmap("light.jpg")
        self.open = QPixmap("crosso.jpg")
        self.closed = QPixmap("crossc.jpg")
        self.line:Track = Track()
        self.side:Wayside = self.line.create([[0],[0],[0],[0],[0]])
        #Creating Track Map
        ###########################################

        #Set default text
        for i in range(len(self.side)):
            self.ui.wayside.addItem(self.side[i].getName())
            self.ui.waysideTB.addItem(self.side[i].getName())
        for i in range(len(self.side[0].blocks)):
            self.ui.block.addItem(self.side[0].getBlock(i).name)
        for i in range(len(self.side[0].blocks)):
            self.ui.blockTB.addItem(self.side[0].getBlock(i).name)
        self.ui.waysideData.setText(self.side[0].getName())
        self.ui.blockData.setText(self.side[0].getBlock(0).getName())
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
        self.side[way].getBlock(blo).setOccupancy(self.ui.occupationTB.isChecked())

    def TB_w_handler(self):
        way = self.ui.waysideTB.currentIndex()
        blo = 0
        self.ui.blockTB.clear()
        for i in range(len(self.side[way].blocks)):
            self.ui.blockTB.addItem(self.side[way].getBlock(i).name)
        self.ui.occupationTB.setChecked(self.side[way].getBlock(blo).getOccupancy())
    
    def TB_b_handler(self):
        way = self.ui.waysideTB.currentIndex()
        blo = self.ui.blockTB.currentIndex()
        self.ui.occupationTB.setChecked(self.side[way].getBlock(blo).getOccupancy())

    

    def toggle_direction_handler(self):
        #Get current block and wayside
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        #If left turn right if right turn left
        if(self.side[way].getBlock(blo).getSwitch()):
            self.side[way].getBlock(blo).setSwitch(False)
            self.ui.switchDirection.setPixmap(self.left)
        else:
            self.side[way].getBlock(blo).setSwitch(True)
            self.ui.switchDirection.setPixmap(self.right)
    
    def toggle_crossroad_handler(self):
        #Get current block and wayside
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        #If open close if closed open
        if(self.side[way].getBlock(blo).getCrossroad()):
            self.side[way].getBlock(blo).setCrossroad(False)
            self.ui.crossroadStatus.setPixmap(self.open)
        else:
            side[way].getBlock(blo).setCrossroad(True)
            self.ui.crossroadStatus.setPixmap(self.closed)
        

    def green_handler(self):
        #Get current block and wayside
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        #If red change green
        if(not self.side[way].getBlock(blo).getSignal()):
            self.side[way].getBlock(blo).setSignal(True)
            self.ui.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")

    def red_handler(self):
        #Get current block and wayside
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        #If Green change red
        if(self.side[way].getBlock(blo).getSignal()):
            self.side[way].getBlock(blo).setSignal(False)
            self.ui.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")

    def new_wayside(self):
        #Get current wayside and block index is zero
        way = self.ui.wayside.currentIndex()
        blo = 0
        #Create new block list
        self.ui.block.clear()
        for i in range(len(self.side[way].blocks)):
            self.ui.block.addItem(self.side[way].getBlock(i).name)
        #Set the lables of block wayside and occupation
        self.ui.waysideData.setText(self.side[way].name)
        self.ui.blockData.setText(self.side[way].getBlock(blo).name)
        #Switch Update
        if(self.side[way].getBlock(blo).getHasSwitch()):
            #If there is a switch set data and show frame
            if(self.side[way].getBlock(blo).getSwitch()):
                self.ui.switchDirection.setPixmap(self.right)
            else:
                self.ui.switchDirection.setPixmap(self.left)
            self.ui.leftBlock.setText(self.side[way].getBlock(blo).getLeft())
            self.ui.rightBlock.setText(self.side[way].getBlock(blo).getRight())
            self.ui.switchFrame.show()
        else:
            self.ui.switchFrame.hide()
        #Crossroad Update
        if(self.side[way].getBlock(blo).getHasCrossroad()):
            #If there is a crossroad set image and show frame
            if(self.side[way].getBlock(blo).getCrossroad()):
                self.ui.crossroadStatus.setPixmap(self.closed)
            else:
                self.ui.crossroadStatus.setPixmap(self.open)
            self.ui.crossroadFrame.show()
        else:
            self.ui.crossroadFrame.hide()
        if(self.side[way].getBlock(blo).getHasSignal()):
            #If there is a signal set color and show frame
            if(self.side[way].getBlock(blo).getSignal()):
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
        self.ui.waysideData.setText(self.side[way].name)
        self.ui.blockData.setText(self.side[way].getBlock(blo).name)
        #Switch Update
        if(self.side[way].getBlock(blo).getHasSwitch()):
            #If there is a switch set data and show frame
            if(self.side[way].getBlock(blo).getSwitch()):
                self.ui.switchDirection.setPixmap(self.right)
            else:
                self.ui.switchDirection.setPixmap(self.left)
            self.ui.leftBlock.setText(self.side[way].getBlock(blo).getLeft())
            self.ui.rightBlock.setText(self.side[way].getBlock(blo).getRight())
            self.ui.switchFrame.show()
        else:
            self.ui.switchFrame.hide()
        #Crossroad Update
        if(self.side[way].getBlock(blo).getHasCrossroad()):
            #If there is a crossroad set image and show frame
            if(self.side[way].getBlock(blo).getCrossroad()):
                self.ui.crossroadStatus.setPixmap(self.closed)
            else:
                self.ui.crossroadStatus.setPixmap(self.open)
            self.ui.crossroadFrame.show()
        else:
            self.ui.crossroadFrame.hide()
        if(self.side[way].getBlock(blo).getHasSignal()):
            #If there is a signal set color and show frame
            if(self.side[way].getBlock(blo).getSignal()):
                self.ui.signalState.setStyleSheet("background-color: rgb(0, 255, 0);")
            else:
                self.ui.signalState.setStyleSheet("background-color: rgb(255, 0, 0);")
            self.ui.signalFrame.show()
        else:
            self.ui.signalFrame.hide()

    def mode_handler(self):
        way = self.ui.wayside.currentIndex()
        blo = self.ui.block.currentIndex()
        self.ui.switchDirection.setPixmap(self.left)

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
    MainWindow = SoftwareTrackControllerGUI()
    MainWindow.show()
    sys.exit(app.exec())
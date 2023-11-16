import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
import math
from swtrainUI import Ui_Form


class SoftwareTrainControllerGUI(Ui_Form):
  
    #meters/sec
    #variables in metric
    
    
    # beacon message:
    # name/length/speedlimit/underground;
    # how do we know if at station or switch
    

    def __init__(self):
        self.ebrakeval=False
        
        super().__init__()
        # self.init_ui()

        
       # self.tbapply.clicked.connect(self.tbreceiveVals)
        
    
    def connect(self):
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.update_time)
        # self.timer.start(50)
        self.serviceBrake.setStyleSheet('background-color: orange')
        self.ebrake.setStyleSheet('background-color: #FF7F7F')
        self.mode.currentTextChanged.connect(self.modeVals)
        #self.ebrake.clicked.connect(self.eBrakePressed)      #check for if ebrake is pushed in manual or automatic
        #self.serviceBrake.clicked.connect(self.swtrain.serviceBrakePressed)
        self.internallight.setChecked(True)
        self.ki.setMaximum(999)
        self.kp.setMaximum(999)
        self.ki.setValue(20)
        self.kp.setValue(400)
        self.modeVals()

    def eBrakePressed(self):
        self.ebrakeval=not self.ebrakeval
        
        
        #cannot edit doors or light statuses in automatic mode
    def modeVals(self):
        if self.mode.currentText()=='Automatic':
            self.rightdoor.setDisabled(True)
            self.leftdoor.setDisabled(True)
            self.externallight.setDisabled(True)
            self.internallight.setDisabled(True)
            self.temp.setDisabled(True)
            self.announcement.setDisabled(True)
            self.serviceBrake.setDisabled(True)
            self.manualcommandedspeed.setDisabled(True)
        else:
            self.rightdoor.setDisabled(False)
            self.leftdoor.setDisabled(False)
            self.externallight.setDisabled(False)
            self.internallight.setDisabled(False)
            self.temp.setDisabled(False)
            self.announcement.setDisabled(False)
            self.serviceBrake.setDisabled(False)
            self.manualcommandedspeed.setDisabled(False)      


    # def receiveVals(self):
    #     #self.swtrain.controller.setBeaconInfo()f
    #     self.modeVals()
    #     self.swtrain.setManualCommandedSpeed(self.manualcommandedspeed.value())
    #     self.swtrain.setTemperature(self.temp.value())
    #     self.swtrain.setKi(self.ki.value())
    #     self.swtrain.setKp(self.kp.value())
    #     self.swtrain.setExLights(self.externallight.isChecked())
    #     self.swtrain.setIntLights(self.internallight.isChecked())
    #     if self.swtrain.getManualMode():
    #         self.swtrain.setLeftDoor(self.leftdoor.isChecked())
    #         self.swtrain.setRightDoor(self.rightdoor.isChecked())
    #     self.computeVals()
    
    # def computeVals(self):
    #     #self.swtrain.controller.decodeBeaconInfo()
    #     #self.swtrain.computeAuthority()
    #     self.swtrain.computeManualSpeed()
    #     self.swtrain.computeServiceBrake()
    #     #self.swtrain.computeAutoSpeed()
    #     self.swtrain.computeDwellTime()    
    #     self.swtrain.computePower()      
    #     self.updateVals()

    
    # def updateVals(self):
    #     self.power.display(self.swtrain.getPower())
    #     self.currentspeed.display(self.swtrain.getCurrentSpeed()*2.2369362921)
    #     self.nextstop.setPlainText(self.swtrain.getNextStop())
    #     self.autocommandedspeed.display(2.23693629*self.swtrain.getAutoCommandedSpeed())
    #     self.manualcommandedspeed.setValue(int(self.swtrain.getManualCommandedSpeed()))
    #     self.leftdoor.setChecked(self.swtrain.getLeftDoor())
    #     self.rightdoor.setChecked(self.swtrain.getRightDoor())

        
    #     self.externallight.setChecked(self.swtrain.computeExtLights())
    #     self.announcement.setCurrentText(self.computeAnnouncement())

    #     self.speedlimit.display(int(self.swtrain.getSpeedLimit()))
    #     self.authority.display(int(self.swtrain.getAuthority()*2.23693629))
        
    # def tbreceiveVals(self):
    #     self.setCommandedSpeed(int(self.tbcommandespeed.toPlainText()))
    #     self.setCurrentSpeed(int(self.tbcurrentspeed.toPlainText()))
    #     self.setAuthority(int(self.tbauthority.toPlainText()))
    #     self.computeVals()

    # def manualannouncementchange(self):
    #     self.swtrain.setAnnouncement(self.announcement.currentText())
        
    # def computeAnnouncement(self):
    #             #do not allow duplicate announcements to overpopulate the announcement box
    #     if self.swtrain.getAnnouncement()!=self.announcement.currentText():
    #         if not any(self.swtrain.getAnnouncement()== self.announcement.itemText(i) for i in range(self.announcement.count())):
    #             if self.swtrain.getManualMode():
    #                 self.announcement.addItem(self.swtrain.getAnnouncement()) 
    #                 return self.announcement.currentText() 
    #             else:
    #                 return self.swtrain.getAnnouncement()
    #     else: 
    #         return self.swtrain.getAnnouncement()
        
    def init_ui(self):
        self = Ui_Form()           #setup ui
        self.setupUi(self)

       # self.tbcurrentspeed.textChanged.connect(lambda: self.updateVals) 



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SoftwareTrainControllerGUI()
    window.show()
    sys.exit(app.exec())
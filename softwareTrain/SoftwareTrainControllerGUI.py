import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
import math
from swtrainUI import Ui_Form
from SoftwareTrainController import SoftwareTrainController

class SoftwareTrainControllerGUI(QWidget):
  
    #meters/sec
    #variables in metric

    
    # beacon message:
    # name/length/speedlimit/underground;
    # how do we know if at station or switch
    

    def __init__(self):

        self.swtrain=SoftwareTrainController()

        super().__init__()
        self.init_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(50)
        
       # self.ui.tbapply.clicked.connect(self.tbreceiveVals)
        self.ui.mode.currentTextChanged.connect(self.modeVals)
        self.ui.ebrake.clicked.connect(self.swtrain.eBrakePressed)      #check for if ebrake is pushed in manual or automatic
        self.ui.serviceBrake.clicked.connect(self.swtrain.serviceBrakePressed)
        self.ui.announcement.currentTextChanged.connect(self.manualannouncementchange)
    
    def update_time(self):
         self.ui.time.setDateTime(datetime.now())
         self.receiveVals()
        
        
        #cannot edit doors or light statuses in automatic mode
    def modeVals(self):
        if self.ui.mode.currentText()=='Automatic':
            self.swtrain.setMode(False)
            self.ui.rightdoor.setDisabled(True)
            self.ui.leftdoor.setDisabled(True)
            self.ui.externallight.setDisabled(True)
            self.ui.internallight.setDisabled(True)
            self.ui.temp.setDisabled(True)
            self.ui.announcement.setDisabled(True)
            self.ui.serviceBrake.setDisabled(True)
            self.ui.manualcommandedspeed.setDisabled(True)
        else:
            self.swtrain.setMode(True)
            self.ui.rightdoor.setDisabled(False)
            self.ui.leftdoor.setDisabled(False)
            self.ui.externallight.setDisabled(False)
            self.ui.internallight.setDisabled(False)
            self.ui.temp.setDisabled(False)
            self.ui.announcement.setDisabled(False)
            self.ui.serviceBrake.setDisabled(False)
            self.ui.manualcommandedspeed.setDisabled(False)      


    def receiveVals(self):
        #self.swtrain.controller.setBeaconInfo()
        self.swtrain.setManualCommandedSpeed(self.ui.manualcommandedspeed.value())
        self.swtrain.setTemperature(self.ui.temp.value())
        self.swtrain.setKi(self.ui.ki.value())
        self.swtrain.setKp(self.ui.kp.value())
        self.swtrain.setExLights(self.ui.externallight.isChecked())
        self.swtrain.setIntLights(self.ui.internallight.isChecked())
        if self.swtrain.getManualMode():
            self.swtrain.setLeftDoor(self.ui.leftdoor.isChecked())
            self.swtrain.setRightDoor(self.ui.rightdoor.isChecked())
        self.computeVals()
    
    def computeVals(self):
        #self.swtrain.controller.decodeBeaconInfo()
        #self.swtrain.computeAuthority()
        self.swtrain.computeManualSpeed()
        self.swtrain.computeServiceBrake()
        #self.swtrain.computeAutoSpeed()
        self.swtrain.computeDwellTime()    
        self.swtrain.computePower()      
        self.updateVals()

    
    def updateVals(self):
        self.ui.power.display(self.swtrain.getPower())
        self.ui.currentspeed.display(self.swtrain.getCurrentSpeed()*2.2369362921)
        self.ui.nextstop.setPlainText(self.swtrain.getNextStop())
        self.ui.autocommandedspeed.display(2.23693629*self.swtrain.getAutoCommandedSpeed())
        self.ui.manualcommandedspeed.setValue(int(self.swtrain.getManualCommandedSpeed()))
        self.ui.leftdoor.setChecked(self.swtrain.getLeftDoor())
        self.ui.rightdoor.setChecked(self.swtrain.getRightDoor())

        
        self.ui.externallight.setChecked(self.swtrain.computeExtLights())
        self.ui.announcement.setCurrentText(self.computeAnnouncement())

        self.ui.speedlimit.display(int(self.swtrain.getSpeedLimit()))
        self.ui.authority.display(int(self.swtrain.getAuthority()*2.23693629))
        
    # def tbreceiveVals(self):
    #     self.setCommandedSpeed(int(self.ui.tbcommandespeed.toPlainText()))
    #     self.setCurrentSpeed(int(self.ui.tbcurrentspeed.toPlainText()))
    #     self.setAuthority(int(self.ui.tbauthority.toPlainText()))
    #     self.computeVals()

    def manualannouncementchange(self):
        self.swtrain.setAnnouncement(self.ui.announcement.currentText())
        
    def computeAnnouncement(self):
                #do not allow duplicate announcements to overpopulate the announcement box
        if self.swtrain.getAnnouncement()!=self.ui.announcement.currentText():
            if not any(self.swtrain.getAnnouncement()== self.ui.announcement.itemText(i) for i in range(self.ui.announcement.count())):
                if self.swtrain.getManualMode():
                    self.ui.announcement.addItem(self.swtrain.getAnnouncement()) 
                    return self.ui.announcement.currentText() 
                else:
                    return self.swtrain.getAnnouncement()
        else: 
            return self.swtrain.getAnnouncement()
        
    def init_ui(self):
        self.ui = Ui_Form()           #setup ui
        self.ui.setupUi(self)
        self.modeVals()
        self.ui.ki.setMaximum(999)
        self.ui.kp.setMaximum(999)
        self.ui.ki.setValue(20)
        self.ui.kp.setValue(400)
       # self.ui.tbcurrentspeed.textChanged.connect(lambda: self.updateVals) 

        self.ui.serviceBrake.setStyleSheet('background-color: orange')
        self.ui.ebrake.setStyleSheet('background-color: #FF7F7F')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SoftwareTrainControllerGUI()
    window.show()
    sys.exit(app.exec())

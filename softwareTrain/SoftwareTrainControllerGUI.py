import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
import math
from swtrainUI import Ui_MainWindow
from trainmodel import train_model_software

class SoftwareTrainControllerGUI(QMainWindow):
  
    #meters/sec
    #variables
    

        #calculation of kp and ki values?
        #decode beacon messages?
        #inputs in metric
        #announcement?

    def __init__(self):

        self.swtrain=train_model_software()

        super().__init__()
        self.init_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(50)
        
       # self.ui.tbapply.clicked.connect(self.tbreceiveVals)
        
        self.ui.ebrake.clicked.connect(self.swtrain.controller.eBrakePressed)      #check for if ebrake is pushed in manual or automatic

        self.ui.announcement.currentTextChanged.connect(self.manualannouncementchange)
    
    def update_time(self):
         self.ui.time.setDateTime(datetime.now())
         self.receiveVals()
        
        
        #cannot edit doors or light statuses in automatic mode
    def modeVals(self):
        if self.ui.mode.currentText()=='Automatic':
            self.swtrain.controller.setMode(False)
            self.ui.rightdoor.setDisabled(True)
            self.ui.leftdoor.setDisabled(True)
            self.ui.externallight.setDisabled(True)
            self.ui.internallight.setDisabled(True)
            self.ui.temp.setDisabled(True)
            self.ui.announcement.setDisabled(True)
            self.ui.servicebrake.setDisabled(True)
            self.ui.manualcommandedspeed.setDisabled(True)
        else:
            self.swtrain.controller.setMode(True)
            self.ui.rightdoor.setDisabled(False)
            self.ui.leftdoor.setDisabled(False)
            self.ui.externallight.setDisabled(False)
            self.ui.internallight.setDisabled(False)
            self.ui.temp.setDisabled(False)
            self.ui.announcement.setDisabled(False)
            self.ui.servicebrake.setDisabled(False)
            self.ui.manualcommandedspeed.setDisabled(False)      


    def receiveVals(self):
        self.modeVals()
        self.swtrain.controller.setManualCommandedSpeed(self.ui.manualcommandedspeed.value())
        self.swtrain.controller.setServiceBrakeSlide(self.ui.servicebrake.value())
        self.swtrain.controller.setTemperature(self.ui.temp.value())
        self.swtrain.controller.setKi(self.ui.ki.value())
        self.swtrain.controller.setKp(self.ui.kp.value())
        self.swtrain.controller.setExLights(self.ui.externallight.isChecked())
        self.swtrain.controller.setIntLights(self.ui.internallight.isChecked())
        if self.swtrain.controller.getManualMode():
            self.swtrain.controller.setLeftDoor(self.ui.leftdoor.isChecked())
            self.swtrain.controller.setRightDoor(self.ui.rightdoor.isChecked())
        self.computeVals()
    
    def computeVals(self):
        self.swtrain.controller.computeAuthority()
        self.swtrain.controller.computeManualSpeed()
        self.swtrain.controller.computeAutoSpeed()
        self.swtrain.controller.computeDwellTime() 
        self.swtrain.controller.computeServiceBrake()    
        self.swtrain.controller.computePower()      
        self.swtrain.controller.decodeBeaconInfo()
        self.swtrain.update_train()
        self.updateVals()

    
    def updateVals(self):
        self.ui.power.display(self.swtrain.controller.getPower())
        self.ui.currentspeed.display(self.swtrain.controller.getCurrentSpeed()*2.2369362921)
        self.ui.nextstop.setPlainText(self.swtrain.controller.getNextStop())
        self.ui.autocommandedspeed.display(2.23693629*self.swtrain.controller.getAutoCommandedSpeed())
        self.ui.manualcommandedspeed.setValue(int(self.swtrain.controller.getManualCommandedSpeed()))
        self.ui.leftdoor.setChecked(self.swtrain.controller.getLeftDoor())
        self.ui.rightdoor.setChecked(self.swtrain.controller.getRightDoor())

        
        self.ui.externallight.setChecked(self.swtrain.controller.computeExtLights())
        self.ui.announcement.setCurrentText(self.computeAnnouncement())

        self.ui.speedlimit.display(int(self.swtrain.controller.getSpeedLimit()))
        self.ui.authority.display(int(self.swtrain.controller.getAuthority()*2.23693629))
        
    # def tbreceiveVals(self):
    #     self.setCommandedSpeed(int(self.ui.tbcommandespeed.toPlainText()))
    #     self.setCurrentSpeed(int(self.ui.tbcurrentspeed.toPlainText()))
    #     self.setAuthority(int(self.ui.tbauthority.toPlainText()))
    #     self.computeVals()

    def manualannouncementchange(self):
        self.swtrain.controller.setAnnouncement(self.ui.announcement.currentText())
        
    def computeAnnouncement(self):
                #do not allow duplicate announcements to overpopulate the announcement box
        if self.swtrain.controller.getAnnouncement()!=self.ui.announcement.currentText():
            if not any(self.swtrain.controller.getAnnouncement()== self.ui.announcement.itemText(i) for i in range(self.ui.announcement.count())):
                self.ui.announcement.addItem(self.swtrain.controller.getAnnouncement())    
        
    def init_ui(self):
        self.ui = Ui_MainWindow()           #setup ui
        self.ui.setupUi(self)
        self.modeVals()
        self.ui.ki.setValue(20)
        self.ui.kp.setValue(99)
       # self.ui.tbcurrentspeed.textChanged.connect(lambda: self.updateVals) 

        self.ui.textEdit_12.setStyleSheet('background-color: orange')
        self.ui.ebrake.setStyleSheet('background-color: #FF7F7F')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SoftwareTrainControllerGUI()
    window.show()
    sys.exit(app.exec())

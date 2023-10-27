import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
import math
from swtc import Ui_MainWindow


class SoftwareTrainControllerGUI(QMainWindow):
  
    #variables
    manualmode=False
    ctcSpeed=0
    automaticcommandedspeed=15
    manualcommandedspeed=0
    nextstop="A Stop"
    currentSpeed=0      #current speed in manual or auto (max speed is 70km/hr)
    previousSpeed=0
    commandedSpeed=0    #commanded speed in automatic mode
    desiredSpeed=0      #desired speed that the train controller wants the train to be at (either in manual mode or auto eg stopping at a station)
    speedLimit=43
    authority=15         #authority in automatic mode
    temperature=70       #temp in degrees fahrenheit
    exlights=False     #true=on
    intlights=True      #true=on
    leftDoor=False       #true=open
    rightDoor=False      #true=open
    announcement=""
    manualMode=False    #true =manual mode on
    eBrake=False        #false=not pressed
    tunnel=False
    stationOnLeft=False #where to let the passengers out. if stationOnLeft is true, that means the left doors open when the station is reached
    serviceBrakeSlide=0
    manualSpeedSlide=0
    ek=0
    ekprev=0
    uk=0
    kp=0    #proportional gain
    ki=0    #integral gain
    brakeFailure=False  # false is no failure
    engineFailure=False
    signalFailure=False
    power=0     
    interval=.05
    dwelling=True
        

        #need to implement logic to slow down as coming to a station  (auto)  
        #calculation of kp and ki values?
        #decode beacon messages?
        #inputs in metric
        #need to add in dwell time
        

    def __init__(self):
        super().__init__()
        self.init_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.ui.tbapply.clicked.connect(self.tbreceiveVals)

        self.ui.commandedspeed.setMaximumHeight(43) #set maximum speed limit of the train
        
        self.ui.manualspeed.setTickInterval(1) 

        self.ui.mode.currentTextChanged.connect(self.modeVals)  #check for change in mode
        self.ui.ebrake.clicked.connect(self.eBrakePressed)      #check for if ebrake is pushed in manual or automatic
   
        self.ui.announcement.currentTextChanged.connect(self.manualannouncementchange)
    
    def update_time(self):
        self.ui.time.setDateTime(datetime.now())
        self.receiveVals()
        
        
        #cannot edit doors or light statuses in automatic mode
    def modeVals(self):
        if self.ui.mode.currentText()=='Automatic':
            self.manualMode=False
            self.ui.rightdoor.setDisabled(True)
            self.ui.leftdoor.setDisabled(True)
            self.ui.externallight.setDisabled(True)
            self.ui.internallight.setDisabled(True)
            self.ui.commandedspeed.setDisabled(True)
            self.ui.temp.setDisabled(True)
            self.ui.announcement.setDisabled(True)
            self.ui.servicebrake.setDisabled(True)
            self.ui.manualspeed.setDisabled(True)
        else:
            self.manualMode=True
            self.ui.rightdoor.setDisabled(False)
            self.ui.leftdoor.setDisabled(False)
            self.ui.externallight.setDisabled(False)
            self.ui.internallight.setDisabled(False)
            self.ui.commandedspeed.setDisabled(False)
            self.ui.temp.setDisabled(False)
            self.ui.announcement.setDisabled(False)
            self.ui.servicebrake.setDisabled(False)
            self.ui.manualspeed.setDisabled(False)
        

    def eBrakePressed(self):  
        if self.currentSpeed==0 and self.eBrake==True:    #ebrake already pressed
            print('Ebrake released')
            self.eBrake=False
            self.computeVals()
        else:
            print('Ebrake pressed')
            self.eBrake=True
            self.computeVals()

    def receiveVals(self):
        self.manualSpeedSlide=self.ui.manualspeed.value()
        self.serviceBrakeSlide=self.ui.servicebrake.value()
        self.previousSpeed=self.currentSpeed
        self.temperature=int(self.ui.temp.value())
        self.ki=self.ui.ki.value()
        self.kp=self.ui.kp.value()
        self.exlights=self.ui.externallight.isChecked()
        self.intlights=self.ui.internallight.isChecked()
        self.leftDoor=self.ui.leftdoor.isChecked()
        self.rightDoor=self.ui.rightdoor.isChecked()
        self.computeVals()
    
    def computeVals(self):
        #add in logic for being at station? dwelling? getting out of dwelling? dwell time?
        if self.authority>0:
            self.authority-=self.currentSpeed*1

        #might need to correct
        if self.authority<=30:            
            if self.authority<=30 and self.authority>20:
                self.automaticcommandedspeed=15
            if self.authority<=20 and self.authority>10:
                self.automaticcommandedspeed=10
            if self.authority<=10 and self.authority>5:
                self.automaticcommandedspeed=5
            if self.authority<=5 and self.authority>1:
                self.automaticcommandedspeed=3
            if self.authority<=1:
                self.automaticcommandedspeed=0
        else:
            self.automaticcommandedspeed=self.ctcSpeed
            
        

        self.ekprev=self.ek
        self.ek=self.commandedSpeed-self.currentSpeed
        self.uk+=(self.interval/2)*(self.ek+self.ekprev)
        self.power=(self.ek*self.kp+self.ki*self.uk)          
        
        if self.serviceBrakeSlide>0:
            self.manualSpeedSlide=0
            self.ui.manualspeed.setValue(0)
            self.manualcommandedspeed=self.currentSpeed #make sure this is good
        else:
            if self.manualcommandedspeed+self.ui.manualspeed.value()>=self.speedLimit:
                self.manualcommandedspeed=self.speedLimit
            else:
                self.manualcommandedspeed+=self.ui.manualspeed.value()
            

        if self.manualMode==True:
            self.commandedSpeed=self.manualcommandedspeed
        else:
            self.commandedSpeed=self.automaticcommandedspeed
            self.manualcommandedspeed=self.automaticcommandedspeed
            if self.stationOnLeft and self.authority==0 and self.currentSpeed==0:   #compute values for the doors when at a station
                self.ui.leftdoor.setChecked(True)
                self.ui.rightdoor.setChecked(False)
                self.leftDoor=True
                self.rightDoor=False
            if self.stationOnLeft==False and self.authority==0 and self.currentSpeed==0:
                self.ui.rightdoor.setChecked(True)
                self.ui.leftdoor.setChecked(False)
                self.rightDoor=True
                self.leftDoor=False
            else:
                self.rightDoor=False
                self.leftDoor=False


        if self.eBrake:
            self.commandedSpeed=0
            self.manualcommandedspeed=0
            self.automaticcommandedspeed=0

        self.updateVals()

    def updateVals(self):
        self.ui.power.display(self.power)
        self.ui.currentspeed.display(2.23693629*self.currentSpeed)
        self.ui.nextstop.setPlainText(self.nextstop)
        self.ui.commandedspeed.display(2.23693629*self.commandedSpeed)
        
        if not self.manualMode:
            self.ui.externallight.setChecked(self.computeExtLights())

        #do not allow duplicate announcements to overpopulate the announcement box
        if self.announcement!=self.ui.announcement.currentText():
            if not any(self.announcement == self.ui.announcement.itemText(i) for i in range(self.ui.announcement.count())):
                print('here')
                self.ui.announcement.addItem(self.announcement)
        self.ui.announcement.setCurrentText(self.announcement)

        self.ui.speedlimit.setPlainText(str(self.speedLimit*2.23693629))
        self.ui.authority.setPlainText(str(self.authority*2.23693629))
        
    def tbreceiveVals(self):
        self.automaticcommandedspeed=(int(self.ui.tbcommandespeed.toPlainText()))
        self.currentSpeed=(int(self.ui.tbcurrentspeed.toPlainText()))
        self.authority=(int(self.ui.tbauthority.toPlainText()))
        self.announcement=(self.ui.tbannouncement.currentText())
        self.computeVals()

    def computeExtLights(self):
        if self.tunnel:
            return True
        else:
            return False

    def manualannouncementchange(self):
        self.announcement=self.ui.announcement.currentText()
        
    def setCommandedSpeed(self,s):
        self.ctcSpeed=s
    def setCurrentSpeed(self,s):
        self.currentSpeed=s
    def setSpeedLimit(self,s):
        self.speedLimit=s
        
    def setNextStop(self,stop):
        self.nextstop=stop
        
    def setAnnouncement(self,a):
        self.announcement=a
        print(self.announcement)

    def setAuthority(self,a):
        self.authority=a

    def getMode(self):
        return self.manualmode 
    def getEbrake(self):
        return self.eBrake
        
    def setBrakeFailure(self,a):
        self.brakeFailure=a
    def setSignalFailure(self,a):
        self.signalFailure=a
    def setEngineFailure(self,a):
        self.engineFailure=a

    def getRightDoor(self):
        return self.rightDoor
    def getLeftDoor(self):
            return self.leftDoor
    def getExteriorLights(self):
            return self.exlights
    def getIntLights(self):
        return self.intlights

        #set time function?

    def getDesiredSpeed(self):
        return self.desiredSpeed

    def setTunnel(self,t):
        self.tunnel=t

    def setStationOnLeft(self, s):
        self.stationOnLeft=s

    def getServiceBrake(self):
        return self.serviceBrakeSlide

    def init_ui(self):
        self.ui = Ui_MainWindow()           #setup ui
        self.ui.setupUi(self)
        self.modeVals()
        self.ui.temp.setValue(70)
        self.ui.internallight.setChecked(True)
       # self.ui.tbcurrentspeed.textChanged.connect(lambda: self.updateVals) 

        self.ui.textEdit_12.setStyleSheet('background-color: orange')
        self.ui.ebrake.setStyleSheet('background-color: #FF7F7F')

        
        
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.announce)
        self.timer.start(1000) 
    def announce(self):
        self.setCurrentSpeed(1)
        self.setCommandedSpeed(10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SoftwareTrainControllerGUI()
    window.show()
    sys.exit(app.exec())

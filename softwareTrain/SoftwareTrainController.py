import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
import math
from swtrainUI import Ui_MainWindow


class SoftwareTrainControllerGUI(QMainWindow):
  
    #meters/sec
    #variables
    manualmode=False
    ctcSpeed=0                #speed to go in automatic mode when in the middle of a route in m/s
    automaticcommandedspeed=0   #desired speed in automatic mode. i edit this as the train is stopping at a station
    manualcommandedspeed=0      #the value of the slide bar. commandedspeed=manualcommandedspeed if manualMode=True 
    nextstop="A Stop"
    currentSpeed=0      #current speed in manual or auto (max speed is 70km/hr)
    speedLimit=43
    authority=0         #authority in automatic mode
    temperature=70       #temp in degrees fahrenheit
    exlights=False     #true=on
    intlights=True      #true=on
    leftDoor=False       #true=open
    rightDoor=False      #true=open
    announcement=""
    manualMode=False    #true =manual mode on
    eBrake=False        #false=not pressed
    tunnel=False
    stationOnLeft=True #where to let the passengers out. if stationOnLeft is true, that means the left doors open when the station is reached
    serviceBrakeSlide=0
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
    dwelling=False
    dwellTime=60
         
        #calculation of kp and ki values?
        #decode beacon messages?
        #inputs in metric
        #if i have a failure does the ebrake get pressed? how do failures get computed? what to do after track failure?

    def __init__(self):
        super().__init__()
        self.init_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(50)
        
       # self.ui.tbapply.clicked.connect(self.tbreceiveVals)
        
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
            self.ui.temp.setDisabled(True)
            self.ui.announcement.setDisabled(True)
            self.ui.servicebrake.setDisabled(True)
            self.ui.manualcommandedspeed.setDisabled(True)
        else:
            self.manualMode=True
            self.ui.rightdoor.setDisabled(False)
            self.ui.leftdoor.setDisabled(False)
            self.ui.externallight.setDisabled(False)
            self.ui.internallight.setDisabled(False)
            self.ui.temp.setDisabled(False)
            self.ui.announcement.setDisabled(False)
            self.ui.servicebrake.setDisabled(False)
            self.ui.manualcommandedspeed.setDisabled(False)
        


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
        self.manualcommandedspeed=self.ui.manualcommandedspeed.value()
        self.serviceBrakeSlide=self.ui.servicebrake.value()
        self.temperature=int(self.ui.temp.value())
        self.ki=self.ui.ki.value()
        self.kp=self.ui.kp.value()
        self.exlights=self.ui.externallight.isChecked()
        self.intlights=self.ui.internallight.isChecked()
        self.leftDoor=self.ui.leftdoor.isChecked()
        self.rightDoor=self.ui.rightdoor.isChecked()
        self.computeVals()
    
    def computeVals(self):
        self.computeManualSpeed()
        self.computeAutoSpeed()
        self.computeAuthority()
        self.computeDwellTime()
        self.modeVals()
        self.computeDoors()
        self.computePower()                   
        self.updateVals()

    def computePower(self):
        if self.manualMode==True:
            self.ekprev=self.ek
            self.ek=self.manualcommandedspeed-self.currentSpeed
            self.uk=(self.interval/2)*(self.ek+self.ekprev)
            self.power=(self.ek*self.kp+self.ki*self.uk)
        else:
            self.ekprev=self.ek
            self.ek=self.automaticcommandedspeed-self.currentSpeed
            self.uk+=(self.interval/2)*(self.ek+self.ekprev)
            self.power=(self.ek*self.kp+self.ki*self.uk)

    def computeDoors(self):
        if self.authority==0 and self.currentSpeed==0:
            if self.stationOnLeft:
                self.ui.leftdoor.setChecked(True)
            else:
                self.ui.rightdoor.setChecked(True)
        else:
                self.ui.leftdoor.setChecked(False)
                self.ui.rightdoor.setChecked(False)
    def computeDwellTime(self):
        if self.dwelling and not self.manualMode:
            print(self.dwellTime)
            if self.dwellTime-self.interval>0:   #subtract the time that it takes the timer to time out
                self.dwellTime-=self.interval
            else:
                self.dwelling=False
                self.dwellTime=60        
    def computeAuthority(self):
        if self.authority>0:
            self.authority-=self.currentSpeed*self.interval
        else:
            if not self.manualMode:
                self.dwelling=True
    def computeAutoSpeed(self):
        if self.automaticcommandedspeed*2.2369362921>=self.speedLimit:
            self.ctcSpeed=self.speedLimit
            self.setCommandedSpeed(self.speedLimit*.44704)

                #might need to correct
        #slowing the train down as authority decreases
        if self.authority<=18 and not self.manualMode: 
            if self.authority<=18 and self.authority>15:
                if self.automaticcommandedspeed>12:
                    self.automaticcommandedspeed=12           
            if self.authority<=15 and self.authority>10:
                if self.automaticcommandedspeed>9:
                    self.automaticcommandedspeed=9
            if self.authority<=10 and self.authority>7:
                if self.automaticcommandedspeed>7:
                    self.automaticcommandedspeed=7
            if self.authority<=7 and self.authority>5:
                if self.automaticcommandedspeed>5:
                    self.automaticcommandedspeed=5
            if self.authority<=5 and self.authority>3:
                if self.automaticcommandedspeed>2.5:
                    self.automaticcommandedspeed=2.5
            if self.authority<=3 and self.authority>1:
                if self.automaticcommandedspeed>1:
                    self.automaticcommandedspeed=1
            if self.authority<=.112:
                self.authority=0
                self.automaticcommandedspeed=0
        else:
            self.automaticcommandedspeed=self.ctcSpeed

    def computeManualSpeed(self):
        if not self.manualMode:
            self.ui.manualcommandedspeed.setValue(round(self.automaticcommandedspeed*2.2369362921))

        if self.manualcommandedspeed>=self.speedLimit:
            self.ui.manualcommandedspeed.setValue(self.speedLimit)
            self.manualcommandedspeed=self.speedLimit*.44704        #convert to m/s
        else:
            self.manualcommandedspeed=self.ui.manualcommandedspeed.value()*.44704   

        if self.serviceBrakeSlide>0:
            self.manualcommandedspeed=self.currentSpeed #make sure this is good, assume connor sends this back
            self.ui.manualcommandedspeed.setValue(self.currentSpeed)
    def updateVals(self):
        self.ui.power.display(self.power)
        self.ui.currentspeed.display(self.currentSpeed*2.2369362921)
        self.ui.nextstop.setPlainText(self.nextstop)
        self.ui.autocommandedspeed.display(2.23693629*self.automaticcommandedspeed)

        if not self.manualMode:
            self.ui.externallight.setChecked(self.computeExtLights())

        #do not allow duplicate announcements to overpopulate the announcement box
        if self.announcement!=self.ui.announcement.currentText():
            if not any(self.announcement == self.ui.announcement.itemText(i) for i in range(self.ui.announcement.count())):
                self.ui.announcement.addItem(self.announcement)
        self.ui.announcement.setCurrentText(self.announcement)

        self.ui.speedlimit.display(round(self.speedLimit))
        self.ui.authority.display(self.authority*2.23693629)
        
    # def tbreceiveVals(self):
    #     self.setCommandedSpeed(int(self.ui.tbcommandespeed.toPlainText()))
    #     self.setCurrentSpeed(int(self.ui.tbcurrentspeed.toPlainText()))
    #     self.setAuthority(int(self.ui.tbauthority.toPlainText()))
    #     self.computeVals()

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
        self.speedLimit=s*2.2369362921
        if self.speedLimit>43:
            self.speedLimit=43
        
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

    def setTunnel(self,t):
        self.tunnel=t

    def setStationOnLeft(self, s):
        self.stationOnLeft=s

    def getServiceBrake(self):
        return self.serviceBrakeSlide

    def getPower(self):
        return self.power
        
    def init_ui(self):
        self.ui = Ui_MainWindow()           #setup ui
        self.ui.setupUi(self)
        self.modeVals()
        self.ui.temp.setValue(70)
        self.ui.internallight.setChecked(True)
       # self.ui.tbcurrentspeed.textChanged.connect(lambda: self.updateVals) 

        self.ui.textEdit_12.setStyleSheet('background-color: orange')
        self.ui.ebrake.setStyleSheet('background-color: #FF7F7F')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SoftwareTrainControllerGUI()
    window.show()
    sys.exit(app.exec())

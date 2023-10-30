import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime
import math
from sw_train_UI import Ui_MainWindow

class SoftwareTrainController():
    
    def __init__(self):
        self.manualmode=False
        self.ctcSpeed=0                #speed to go in automatic mode when in the middle of a route in m/s
        self.automaticcommandedspeed=0   #desired speed in automatic mode. i edit this as the train is stopping at a station
        self.manualcommandedspeed = 20     #the value of the slide bar. commandedspeed=manualcommandedspeed if manualMode=True 
        self.nextstop="A Stop"
        self.currentSpeed=0      #current speed in manual or auto (max speed is 70km/hr)
        self.speedLimit=43
        self.authority=0         #authority in automatic mode
        self.temperature=70       #temp in degrees fahrenheit
        self.exlights=False     #true=on
        self.intlights=True      #true=on
        self.leftDoor=False       #true=open
        self.rightDoor=False      #true=open
        self.announcement=""
        self.manualMode=False    #true =manual mode on
        self.eBrake=False        #false=not pressed
        self.tunnel=False
        self.stationOnLeft='l' #where to let the passengers out. if stationOnLeft is true, that means the left doors open when the station is reached
        self.serviceBrakeSlide=0
        self.ek=10
        self.ekprev=20
        self.uk=0
        self.kp=0    #proportional gain
        self.ki=0    #integral gain
        self.brakeFailure=False  # false is no failure
        self.engineFailure=False
        self.signalFailure=False
        self.power=20   
        self.interval=.05
        self.dwelling=False
        self.dwellTime=60

    def eBrakePressed(self): 
        if self.currentSpeed==0 and self.eBrake==True:    #ebrake already pressed
            print('Ebrake released')
            self.eBrake=False
        else:
            print('Ebrake pressed')
            self.eBrake=True
    
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

    def setAuthority(self,a):
        self.authority=a

    def setMode(self,b):
        self.manualMode=b
        
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

    def computeExtLights(self):
        if self.tunnel and not self.manualMode:
            self.exlights=True
        if not self.tunnel and not self.manualMode:
            self.exlights=False
        return self.exlights

    def setTunnel(self,t):
        self.tunnel=t

    def setStationOnLeft(self, s):
        self.stationOnLeft=s

    def getServiceBrake(self):
        return self.serviceBrakeSlide

    def getPower(self):
        return self.power
    
    def computePower(self):
        if self.manualMode==True:
            self.ekprev=self.ek
            self.ek=self.manualcommandedspeed-self.currentSpeed
            self.uk=(self.interval/2)*(self.ek+self.ekprev)
            self.power=(self.ek*self.kp+self.ki*self.uk)
            return self.power
        else:
            self.ekprev=self.ek
            self.ek=self.automaticcommandedspeed-self.currentSpeed
            self.uk+=(self.interval/2)*(self.ek+self.ekprev)
            self.power=(self.ek*self.kp+self.ki*self.uk)
            return self.power
            
    def computeDoors(self):
        if self.authority==0 and self.currentSpeed==0 and self.stationOnLeft=='l' and not self.manualMode:
            self.leftDoor=True
            self.rightDoor=False
        if self.authority==0 and self.currentSpeed==0 and self.stationOnLeft=='r' and not self.manualMode:
            self.rightDoor=True
            self.leftDoor=False
        if self.authority==0 and self.currentSpeed==0 and self.stationOnLeft=='b' and not self.manualMode:
            self.rightDoor=True
            self.leftDoor=True
        if not self.manualMode:
            self.leftDoor=False
            self.rightDoor=False
        
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

    def computeManualSpeed(self) ->int:
        if self.serviceBrakeSlide>0:
            self.manualcommandedspeed=self.currentSpeed #make sure this is good, assume connor sends this back
            return self.currentSpeed

        if not self.manualMode:
            return round(self.automaticcommandedspeed*2.2369362921)
        else:
            if self.manualcommandedspeed>=self.speedLimit:
                self.manualcommandedspeed=self.speedLimit*.44704        #convert to m/s
                return self.speedLimit
            else:  
                return self.manualcommandedspeed

    def setManualCommandedSpeed(self,s):
        self.manualcommandedspeed=s

    def setServiceBrakeSlide(self,s):
        self.serviceBrakeSlide=s

    def setTemperature(self,t):
        self.temperature=t

    def setKi(self, k):
        self.ki=k

    def setKp(self, k):
        self.kp=k

    def setExLights(self, l):
        self.exlights=l
    
    def setIntLights(self, l):
        self.intlights=l

    def setLeftDoor(self, d):
        self.leftDoor=d

    def setRightDoor(self, d):
        self.rightDoor=d

    def getCurrentSpeed(self):
        return self.currentSpeed
    
    def getNextStop(self):
        return self.nextstop
    
    def getAutoCommandedSpeed(self):
        return self.automaticcommandedspeed
    
    def getAnnouncement(self):
        return self.announcement
    
    def getSpeedLimit(self):
        return self.speedLimit
    
    def getAuthority(self):
        return self.authority

    def getManualCommandedSpeed(self):
        return self.manualcommandedspeed
    
class SoftwareTrainControllerGUI(QMainWindow):
  
    #meters/sec
    #variables
    
    
        #calculation of kp and ki values?
        #decode beacon messages?
        #inputs in metric
        #if i have a failure does the ebrake get pressed? how do failures get computed? what to do after track failure?

    def __init__(self):
        self.swtrain=SoftwareTrainController()
        super().__init__()
        self.init_ui()


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(50)
        
       # self.ui.tbapply.clicked.connect(self.tbreceiveVals)
        
        self.ui.ebrake.clicked.connect(self.swtrain.eBrakePressed)      #check for if ebrake is pushed in manual or automatic

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
            self.ui.servicebrake.setDisabled(True)
            self.ui.manualcommandedspeed.setDisabled(True)
        else:
            self.swtrain.setMode(True)
            self.ui.rightdoor.setDisabled(False)
            self.ui.leftdoor.setDisabled(False)
            self.ui.externallight.setDisabled(False)
            self.ui.internallight.setDisabled(False)
            self.ui.temp.setDisabled(False)
            self.ui.announcement.setDisabled(False)
            self.ui.servicebrake.setDisabled(False)
            self.ui.manualcommandedspeed.setDisabled(False)      


    def receiveVals(self):
        self.swtrain.setManualCommandedSpeed(self.ui.manualcommandedspeed.value())
        self.swtrain.setServiceBrakeSlide(self.ui.servicebrake.value())
        self.swtrain.setTemperature(self.ui.temp.value())
        self.swtrain.setKi(self.ui.ki.value())
        self.swtrain.setKp(self.ui.kp.value())
        self.swtrain.setExLights(self.ui.externallight.isChecked())
        self.swtrain.setIntLights(self.ui.internallight.isChecked())
        self.swtrain.setLeftDoor(self.ui.leftdoor.isChecked())
        self.swtrain.setRightDoor(self.ui.rightdoor.isChecked())
        self.computeVals()
    
    def computeVals(self):
        self.swtrain.computeManualSpeed()
        self.swtrain.computeAutoSpeed()
        self.swtrain.computeDwellTime()
        self.swtrain.computeDoors()
        self.modeVals()               
        self.updateVals()

    
    def updateVals(self):
        self.ui.power.display(self.swtrain.computePower())
        self.ui.currentspeed.display(self.swtrain.getCurrentSpeed()*2.2369362921)
        self.ui.nextstop.setPlainText(self.swtrain.getNextStop())
        self.ui.autocommandedspeed.display(2.23693629*self.swtrain.getAutoCommandedSpeed())
        self.ui.manualcommandedspeed.setValue(self.swtrain.computeManualSpeed())
        self.ui.leftdoor.setChecked(self.swtrain.getLeftDoor())
        self.ui.rightdoor.setChecked(self.swtrain.getRightDoor())

        
        self.ui.externallight.setChecked(self.swtrain.computeExtLights())

        self.ui.manualcommandedspeed.setValue(self.swtrain.computeManualSpeed())
        self.ui.announcement.setCurrentText(self.computeAnnouncement())

        self.ui.speedlimit.display(round(self.swtrain.getSpeedLimit()))
        self.ui.authority.display(self.swtrain.getAuthority()*2.23693629)
        
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
                self.ui.announcement.addItem(self.swtrain.getAnnouncement())    
        
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
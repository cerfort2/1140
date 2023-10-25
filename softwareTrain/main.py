import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QComboBox, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6 import QtCore, QtGui, QtWidgets
from datetime import datetime

from swtc import Ui_MainWindow


class SoftwareTrainControllerGUI(QMainWindow):
  #self.textEdit_9.setStyleSheet(background-color: orange)
  #self.ebrake.setStyleSheet('background-color: #FF7F7F')


    #variables
    manualmode=False
    automaticcommandedspeed=0
    manualcommandedspeed=0
    nextstop="a stop"
    currentSpeed=0      #current speed in manual or auto (max speed is 70km/hr)
    previousSpeed=0
    commandedSpeed=0    #commanded speed in automatic mode
    speedLimit=43
    authority=0         #authority in automatic mode
    temperature=70       #temp in degrees fahrenheit
    exlights=False     #true=on
    intlights=False      #true=on
    leftDoor=False       #true=open
    rightDoor=False      #true=open
    announcement="hello"
    manualMode=False    #true =manual mode on
    eBrake=False        #false=not pressed
    serviceBrake=False  #false=not pressed
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
    

        #need to implement sliders for velocity (buttons?)
        #collect values with a timer or by signals?
        #need bool values for doors, lights in automatic mode?
        #need an announcement input?

    def __init__(self):
        super().__init__()
        self.init_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(50)


        self.ui.commandedspeed.setMaximumHeight(43) #set maximum speed limit of the train
        
        self.ui.manualspeed.setTickInterval(1) 
       
        self.ui.mode.currentTextChanged.connect(self.modeVals)  #check for change in mode
        self.ui.ebrake.clicked.connect(self.eBrakePressed)      #check for if ebrake is pushed in manual or automatic

        #look for changes in service brake and manual speed     
        self.ui.manualspeed.valueChanged.connect(self.manualspeedPressed)
        self.ui.servicebrake.valueChanged.connect(self.serviceBrakePressed)
    
    def update_time(self):
        self.ui.time.setDateTime(datetime.now())
        self.receiveVals()
        
        
        #cannot edit doors or light statuses in automatic mode
    def modeVals(self):
        if self.ui.mode.currentText()=='Automatic':
            print('In Automatic mode')
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
            print('In Manual mode')
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
            

    def serviceBrakePressed(self):
        if self.manualcommandedspeed-self.ui.servicebrake.value()<=0:
            self.manualcommandedspeed=0
        else:
            self.manualcommandedspeed-=self.ui.servicebrake.value()
            self.updateVals()

    def manualspeedPressed(self):
        if self.manualcommandedspeed+self.ui.manualspeed.value()>=self.speedLimit:
            self.manualcommandedspeed=self.speedLimit
        else:
            self.manualcommandedspeed+=self.ui.manualspeed.value()
        self.updateVals()

    def eBrakePressed(self):  
        if self.currentSpeed==0 & self.eBrake==True:    #ebrake already pressed
            print('Ebrake released')
            self.eBrake=False
            self.computeVals()
        else:
            print('Ebrake pressed')
            self.manualcommandedspeed=0
            self.eBrake=True
            self.computeVals()

    def receiveVals(self):
        self.previousSpeed=self.currentSpeed
        self.currentSpeed=0     #call for current speed from train model
        self.authority=0        #call for authority from train model. either have train model use set functions or call get functions from train model
        self.temperature=int(self.ui.temp.value())
        self.announcement=self.ui.announcement.currentText()
        self.ki=self.ui.ki.value()
        self.kp=self.ui.kp.value()
        self.exlights=self.ui.externallight.isChecked()
        self.intlights=self.ui.internallight.isChecked()
        self.leftDoor=self.ui.leftdoor.isChecked()
        self.rightDoor=self.ui.rightdoor.isChecked()
        self.computeVals()
    
    def computeVals(self):
        self.ekprev=self.ek
        self.ek=self.commandedSpeed-self.currentSpeed
        self.uk+=(self.interval/2)*(self.ek+self.ekprev)
        self.power=(self.ek*self.kp+self.ki*self.uk)

        if self.manualMode==True:
            self.commandedSpeed=self.manualcommandedspeed
        else:
            self.commandedSpeed=self.automaticcommandedspeed
            self.manualcommandedspeed=self.automaticcommandedspeed
            
        self.updateVals()

    def updateVals(self):
        #add in some kind of loop to get the current speed to reach commanded, while calculating power
        self.ui.power.display(self.power)
        self.ui.currentspeed.display(self.currentSpeed)
        self.ui.nextstop.setPlainText(self.nextstop)
        self.ui.commandedspeed.display(self.commandedSpeed)
        self.ui.announcement.setCurrentText(self.announcement)
        self.ui.speedlimit.setPlainText(str(self.speedLimit))
        self.ui.authority.setPlainText(str(self.authority))
        
        
        def setCommandedSpeed(s):
            self.automaticcommandedspeed=s
        def setCurrentSpeed(s):
            self.currentSpeed=s
        def setSpeedLimit(s):
            self.speedLimit=s
        
        def setNextStop(stop):
            self.nextstop=stop
        
        def setAnnouncement(a):
            self.ui.tbannouncement.addItem(a)

        def setAuthority(a):
            self.authority=a

        def getMode():
            return self.manualmode 
        def getEbrake():
            return self.eBrake
        
        def setBrakeFailure(a):
            self.brakeFailure=a
        def setSignalFailure(a):
            self.signalFailure=a
        def setEngineFailure(a):
            self.engineFailure=a

        def getRightDoor():
            return self.rightDoor
        def getLeftDoor():
            return self.leftDoor
        def getExteriorLights():
            return self.exlights
        def getIntLights():
            return self.intlights

        #set time function?

    def init_ui(self):
        self.ui = Ui_MainWindow()           #setup ui
        self.ui.setupUi(self)
        self.modeVals()

       # self.ui.tbcurrentspeed.textChanged.connect(lambda: self.updateVals)

    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SoftwareTrainControllerGUI()
    window.show()
    sys.exit(app.exec())

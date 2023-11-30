from PyQt6.QtCore import QObject, pyqtSignal, QTimer
from trains_interface.SoftwareTrainControllerGUI import *

class SoftwareTrainController():
    
    # trainmodel_SW_servicebrake=pyqtSignal(bool)
    # trainmodel_SW_ebrake=pyqtSignal(bool)
    # trainmodel_SW_rightDoor=pyqtSignal(bool)
    # trainmodel_SW_leftDoor=pyqtSignal(bool)
    # trainmodel_SW_interiorLight=pyqtSignal(bool)
    # trainmodel_SW_exteriorLight=pyqtSignal(bool)
    # trainmodel_SW_announcment=pyqtSignal(str)
    # trainmodel_SW_temperature=pyqtSignal(str)
    # trainmodel_SW_power=pyqtSignal(str)

    # def getServiceBrake(self):
    #     self.trainmodel_SW_servicebrake.emit(self.getServiceBrake())

    # def getEbrake(self):
    #     self.trainmodel_SW_ebrake.emit(self.getEbrake())

    # def getExteriorLights(self):
    #     self.trainmodel_SW_exteriorLight.emit(self.getExteriorLights())

    # def getInteriorLights(self):
    #     self.trainmodel_SW_interiorLight.emit(self.getIntLights())

    # def getRightDoor(self):
    #     self.trainmodel_SW_rightDoor.emit(self.getRightDoor())

    # def getLeftDoor(self):
    #     self.trainmodel_SW_leftDoor.emit(self.getLeftDoor())

    # def getPower(self):
    #     self.trainmodel_SW_power.emit(self.getPower())

    # def getAnnouncement(self):
    #     self.trainmodel_SW_announcment.emit(self.getAnnouncement())

    # def getTemperature(self):
    #     self.trainmodel_SW_temperature.emit(self.getTemperature())


    def __init__(self):
        self.ui=SoftwareTrainControllerGUI()
        self.uiopen=False
        self.manualmode=False
        self.simulationSpeed=1
        self.ctcSpeed=10                #speed to go in automatic mode when in the middle of a route in m/s
        self.manualcommandedspeed=0      #the value of the slide bar. commandedspeed=manualcommandedspeed if manualMode=True 
        self.nextstop="A Stop"
        self.currentSpeed=0      #current speed in manual or auto (max speed is 70km/hr)
        self.speedLimit=43
        self.authority=1         #authority in automatic mode
        self.temperature=70       #temp in degrees fahrenheit
        self.exlights=False     #true=on
        self.intlights=True      #true=on
        self.leftDoor=False       #true=open
        self.rightDoor=False      #true=open
        self.announcement=""
        self.eBrake=False        #false=not pressed
        self.tunnel=False
        self.stationOnLeft='b' #where to let the passengers out. if stationOnLeft is true, that means the left doors open when the station is reached
        self.ek=0
        self.ekprev=0
        self.uk=0
        self.kp=400    #proportional gain
        self.ki=20   #integral gain
        self.brakeFailure=False  # false is no failure
        self.engineFailure=False
        self.signalFailure=False
        self.power=0     
        self.interval=.05
        self.dwelling=False
        self.dwellTime=60
        self.serviceBrake=False
        self.brakeAuthority=0
        self.beaconInfo=''

    def open_GUI(self):
        self.widget2 = QWidget()
        self.ui.setupUi(self.widget2)
        self.ui.connect()
        self.widget2.show()

    def update_time(self):
         self.ui.time.setDateTime(datetime.now())
         self.ui.notify.clicked.connect(self.setAnnouncement)
         self.ui.serviceBrake.clicked.connect(self.serviceBrakePressed)
         self.ui.ebrake.clicked.connect(self.eBrakePressed)
         self.getVals()    

    def getVals(self):
        self.ki=self.ui.ki.value()
        self.kp=self.ui.kp.value()
        self.setManualMode(self.ui.mode.currentText())
        self.temperature=self.ui.temp.value()
        self.manualcommandedspeed=self.ui.manualcommandedspeed.value()
        self.externallight=self.ui.externallight.isChecked()
        self.internallight=self.ui.internallight.isChecked()
        self.leftDoor=self.ui.leftdoor.isChecked()
        self.rightDoor=self.ui.rightdoor.isChecked()
        self.computeVals()

    def setManualMode(self,m):
        if m=='Automatic':
            self.manualmode=False
        else:
            self.manualmode=True

    def computeVals(self):
        self.computeManualSpeed()
        self.computeAuthority()
        self.computeServiceBrake()
        self.computeDwellTime()
        self.computePower()
        self.updateVals()

    def updateVals(self):
        self.ui.power.display(self.getPower())
        self.ui.currentspeed.display(self.getCurrentSpeed()*2.2369362921)
        self.ui.nextstop.setPlainText(self.getNextStop())
        self.ui.autocommandedspeed.display(2.23693629*self.getAutoCommandedSpeed())
        self.ui.manualcommandedspeed.setValue(int(self.getManualCommandedSpeed()))
        self.ui.leftdoor.setChecked(self.getLeftDoor())
        self.ui.rightdoor.setChecked(self.getRightDoor())
        
        self.ui.externallight.setChecked(self.computeExtLights())

        self.ui.speedlimit.display(int(self.getSpeedLimit()))
        self.ui.authority.display(int(self.getAuthority()*3.280839895013123))
        


    #def generateSoftwareTrainUI(self):


    
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
        self.setAnnouncement()
        
    def computeServiceBrake(self):
        if not self.manualmode and self.currentSpeed>0:
            
            self.brakedistance = self.currentSpeed**2/(1.2)

            if self.brakedistance>=self.authority:
                self.serviceBrake=True
                print('engaged')
            else:
                self.serviceBrake=False

    def setAnnouncement(self):
        if self.manualmode:
            self.announcement = self.ui.announcement.toPlainText()
        else:
            self.announcement = "Next Stop " + self.nextstop
        self.ui.announcement.setPlainText(self.announcement)
        

    def setAuthority(self,a):
        self.authority=a

    def setMode(self,b):
        self.manualmode=b

    def getTemperature(self):
        return self.temperature

    def setSimulationSpeed(self, s):
        self.simulationSpeed=s

    def getAutoCommandedSpeed(self):
        return self.ctcSpeed
        
    def getManualMode(self):
        return self.manualmode 
    def getEbrake(self):
        return self.eBrake
        
    def setBrakeFailure(self):
        self.brakeFailure= not self.brakeFailure
    def setSignalFailure(self):
        self.signalFailure= not self.signalFailure
    def setEngineFailure(self):
        self.engineFailure= not self.engineFailure

    def eBrakePressed(self):
        if self.eBrake and self.currentSpeed==0:
            self.eBrake=False
        else:
            self.eBrake=True

    def getExteriorLights(self):
            return self.exlights
    def getIntLights(self):
        return self.intlights

    def computeExtLights(self):
        if self.tunnel and not self.manualmode:
            self.exlights=True
        if not self.tunnel and not self.manualmode:
            self.exlights=False
        return self.exlights

    def setTunnel(self,t):
        self.tunnel=t

    def setStationOnLeft(self, s):
        self.stationOnLeft=s

    def getServiceBrake(self):
        return self.serviceBrake

    def getPower(self):
        return self.power
    
    def computePower(self):
        if self.manualmode==True:
            self.ekprev=self.ek
            self.ek=(self.manualcommandedspeed/2.2369362921-self.currentSpeed)
            self.uk+=(self.interval/2)*(self.ek-self.ekprev)
            self.power=(self.ek*self.kp-self.ki*self.uk)
        else:
            self.ekprev=self.ek
            self.ek=(self.ctcSpeed-self.currentSpeed)
            self.uk+=(self.interval/2)*(self.ek-self.ekprev)
            self.power=(self.ek*self.kp-self.ki*self.uk)

        if self.power>120000:
            self.power=120000

        if self.brakeFailure or self.signalFailure or self.engineFailure or self.eBrake or self.power < 0 or self.serviceBrake==True:
            self.power=0
    
            
    def getLeftDoor(self):
        if self.authority==0 and self.currentSpeed==0 and self.stationOnLeft=='l' and not self.manualmode:
            self.leftDoor=True
            self.rightDoor=False
            return True
        if self.authority==0 and self.currentSpeed==0 and self.stationOnLeft=='r' and not self.manualmode:
            self.rightDoor=True
            self.leftDoor=False
            return False
        if self.authority==0 and self.currentSpeed==0 and self.stationOnLeft=='b' and not self.manualmode:
            self.rightDoor=True
            self.leftDoor=True
            return True
        else:
            return self.leftDoor
    def getRightDoor(self):
        if self.authority==0 and self.currentSpeed==0 and self.stationOnLeft=='l' and not self.manualmode:
            self.leftDoor=True
            self.rightDoor=False
            return False
        if self.authority==0 and self.currentSpeed==0 and self.stationOnLeft=='r' and not self.manualmode:
            self.rightDoor=True
            self.leftDoor=False
            return True
        if self.authority==0 and self.currentSpeed==0 and self.stationOnLeft=='b' and not self.manualmode:
            self.rightDoor=True
            self.leftDoor=True
            return True
        else:
            return self.rightDoor

    def computeDwellTime(self):
        if self.dwelling and not self.manualmode:
            print(self.dwellTime)
            self.ctcSpeed=0
            if self.dwellTime-self.interval>0:   #subtract the time that it takes the timer to time out
                self.dwellTime-=self.interval
            else:
                self.dwelling=False
                self.dwellTime=60     
                self.authority+=10   
    def computeAuthority(self):
        if self.authority<=0 and self.currentSpeed==0:
            if not self.manualmode:
                self.dwelling=True


    def computeManualSpeed(self) ->int:
        if self.serviceBrake==True:
            self.manualcommandedspeed=self.currentSpeed #make sure this is good, assume connor sends this back

        if not self.manualmode:
            if self.ctcSpeed>self.speedLimit:
                self.ctcSpeed=self.speedLimit
                self.manualcommandedspeed=self.ctcSpeed*2.2369362921
            else:
                self.manualcommandedspeed=self.ctcSpeed*2.2369362921
        else:
            if self.manualcommandedspeed>=self.speedLimit:
                self.manualcommandedspeed=self.speedLimit        #convert to m/s

    def setManualCommandedSpeed(self,s):
        self.manualcommandedspeed=s

    def serviceBrakePressed(self):
        if self.serviceBrake==True:
            self.serviceBrake=False
        else:
            self.serviceBrake=True

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
    
    def getAnnouncement(self):
        return self.announcement
    
    def getSpeedLimit(self):
        return self.speedLimit
    
    def getAuthority(self):
        return self.authority

    def getManualCommandedSpeed(self):
        return self.manualcommandedspeed

from PyQt6.QtCore import pyqtSignal





class HardwareTrainController():
    
    #both
    trainmodel_HW_power = pyqtSignal(float)
    trainmodel_HW_servicebrake = pyqtSignal(bool)
    trainmodel_HW_ebrake = pyqtSignal(bool)
    

    #manual
    trainmodel_HW_rightdoor = pyqtSignal(bool)
    trainmodel_HW_leftdoor = pyqtSignal(bool)
    trainmodel_HW_exterior = pyqtSignal(bool)
    trainmodel_HW_interior = pyqtSignal(bool)
    trainmodel_HW_temperature = pyqtSignal(bool)
    trainmodel_HW_annoucements = pyqtSignal(bool)


    
    def __init__(self):

        self.beaconInfo = []
        self.nextstop = ""
        self.annoucement = ""
        self.authority = 0
        self.brakeFailure = False
        self.signalFailure = False
        self.engineFailure = False
        self.tunnel = False
        self.stationOnLeft = False
        self.stationOnRight = False
        self.rightdoor = False
        self.leftdoor = False
        self.manualcommandedspeed = 0
        self.temperature = 0
        self.power = 0
        self.ctcSpeed = 0
        self.currentSpeed = 0
        self.speedLimit = 43
        self.dwelling = False
        self.manualmode = False
        self.exterior = False
        self.interior = False
        self.brakeAuthority = 0
        self.brakeSpeed = 0
        self.serviceBrakeFlag = False
        self.eBrakeFlag = False
        self.dwellTime = 0
        self.e_k = 0
        self.e_k_prev = 0
        self.u_k = 0
        self.u_k_prev = 0
        self.kp = 0
        self.ki = 0

    #emitting signals for both modes automatic/manual

    def getServiceBrake(self):
        self.trainmodel_HW_servicebrake(self.serviceBrakeFlag)

    def getPower(self):
        self.trainmodel_HW_power.emit(self.power)
    
    def getEbrake(self):
        self.trainmodel_HW_ebrake.emit(self.eBrakeFlag)

    #emitting manual signals

    def getRD(self):
        self.trainmodel_HW_rightdoor.emit(self.rightdoor)
    
    def getLD(self):
        self.trainmodel_HW_leftdoor.emit(self.leftdoor)

    def getExterior(self):
        self.trainmodel_HW_exterior.emit(self.exterior)

    def getInterior(self):
        self.trainmodel_HW_interior.emit(self.interior)
    
    def getTemperature(self):
        self.trainmodel_HW_temperature(self.temperature)

    def getAnnoucements(self):
        self.trainmodel_HW_temperature(self.annoucement)

    
    def getManualMode(self):
        return self.manualmode
     
    def getEbrake(self):
        return self.eBrake
    
    def eBrakePressed(self): 
        if self.currentSpeed==0 and self.eBrake==True:    #ebrake already pressed
            print('Ebrake released')
            self.eBrake=False
        else:
            print('Ebrake pressed')
            self.eBrake=True

    def computeExtLights(self):
        if self.tunnel and not self.manualmode:
            self.exlights=True
        if not self.tunnel and not self.manualmode:
            self.exlights=False
        return self.exlights

    def setCTC(self,x):
        self.ctcSpeed = x
        
    def setBeaconInfo(self,s):
        self.beaconInfo=s

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
  
    def setBrakeFailure(self,a):
        self.brakeFailure=a

    def setSignalFailure(self,a):
        self.signalFailure=a

    def setEngineFailure(self,a):
        self.engineFailure=a

    def setTunnel(self,t):
        self.tunnel=t

    def setStationOnLeft(self, s):
        self.stationOnLeft=s

    def setStationOnRight(self,s):
        self.stationOnRight = s

    def setServiceBrakeSlide(self,s):
        self.serviceBrakeSlide=s

    def setTemperature(self,t):
        self.temperature=t

    def setCommanded_speed(self,x):
        self.manualcommandedspeed = x
    

    def computeDwellTime(self):
        if self.dwelling and not self.manualmode:
           # print(self.dwellTime)
            if self.dwellTime-self.interval>0:   #subtract the time that it takes the timer to time out
                self.dwellTime-=self.interval
            else:
                self.dwelling=False
                self.dwellTime=60        
    

    def computeManualSpeed(self) ->int:
        if self.serviceBrakeSlide>0:
            self.manualcommandedspeed=self.currentSpeed #make sure this is good, assume connor sends this back

        if not self.manualmode:
            self.manualcommandedspeed=self.ctcSpeed*2.2369362921
        else:
            if self.manualcommandedspeed>=self.speedLimit:
                self.manualcommandedspeed=self.speedLimit        #convert to m/s

    def calcPower(self):
        
        pmax = 10

        self.e_k_prev = self.e_k

        self.u_k_prev = self.u_k

        if(self.manualmode == False):
            self.e_k = self.ctcSpeed - self.currentSpeed
        else:
            self.e_k = self.manualcommandedspeed - self.currentSpeed()


        self.u_k = self.u_k_prev + (.05)/2 * (self.e_k+self.e_k_prev)

        val = self.kp*self.e_k + self.ki*self.u_k
        
        altPower = self.kp * self.e_k + self.ki * self.u_k_prev

        if(val >= pmax):
            self.power = altPower
        else:
            self.power = val

    def setKi(self, k):
        self.ki=k

    def setKp(self, k):
        self.kp=k

    def getManual_commanded(self):
        return self.manualcommandedspeed
    
    def getCurrent_speed(self):
        return self.currentSpeed
    
    def getSpeedLimit(self):
        return self.speedLimit
    
    def getCTCspeed(self):
        return self.ctcSpeed
    
    def getAuthority(self):
        return self.authority
    
    
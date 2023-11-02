class HardwareTrainController():
    

    
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
        self.serviceBrakeSlide = False
        self.manualcommandedspeed = 0
        self.temperature = 0
        self.power = 0
        self.ctcSpeed = 0
        self.currentSpeed = 0
        self.speedLimit = 43
        self.dwelling = False
        self.manualmode = False
        self.eBrake = False
        self.exlights = False
        self.brakeAuthority = 0
        self.brakeSpeed = 0
        self.serviceBrakeFlag = False
        self.dwellTime = 0
        self.e_k = 0
        self.e_k_prev = 0
        self.u_k = 0
        self.u_k_prev = 0
    



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



    def setBeaconInfo(self,s):
        self.beaconInfo=s
    
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

    def getServiceBrake(self):
        return self.serviceBrakeSlide

    def getPower(self):
        return self.power
    
    def setManualCommandedSpeed(self,s):
        self.manualcommandedspeed=s

    def setServiceBrakeSlide(self,s):
        self.serviceBrakeSlide=s

    def setTemperature(self,t):
        self.temperature=t
    
    def computeServiceBrake(self):
        if not self.manualmode and self.currentSpeed>0 and self.authority > 0:
            if not self.serviceBrakeFlag:
                self.serviceBrakeFlag = self.currentSpeed/0.6 + 1 >= self.authority/self.currentSpeed
                self.brakeSpeed=self.currentSpeed
                self.brakeAuthority=self.authority
            if self.serviceBrakeFlag:
                print('engaged')
                self.serviceBrakeSlide=100 - (100 * (1 - max((self.currentSpeed/self.brakeAuthority), (self.authority/self.brakeAuthority))))
        elif self.currentSpeed < 0:
            self.currentSpeed = 0
            self.brakeAuthority = 0
            self.serviceBrakeFlag = False

    def computeDwellTime(self):
        if self.dwelling and not self.manualmode:
           # print(self.dwellTime)
            if self.dwellTime-self.interval>0:   #subtract the time that it takes the timer to time out
                self.dwellTime-=self.interval
            else:
                self.dwelling=False
                self.dwellTime=60        
    
    def computeAuthority(self):
        if self.authority>0:
            self.authority-=self.currentSpeed*self.interval
        else:
            if not self.manualmode:
                self.dwelling=True
    def computeAutoSpeed(self):
        if self.ctcSpeed>=self.speedLimit:
            self.ctcSpeed=self.speedLimit

                #might need to correct
        #slowing the train down as authority decreases

    def computeManualSpeed(self) ->int:
        if self.serviceBrakeSlide>0:
            self.manualcommandedspeed=self.currentSpeed #make sure this is good, assume connor sends this back

        if not self.manualmode:
            self.manualcommandedspeed=self.automaticcommandedspeed*2.2369362921
        else:
            if self.manualcommandedspeed>=self.speedLimit:
                self.manualcommandedspeed=self.speedLimit        #convert to m/s

    def calcPower(self):
        
        pmax = 10

        self.e_k_prev = self.e_k

        self.u_k_prev = self.u_k

        e_k = self.manualcommandedspeed - self.currentSpeed() #current speed from train model

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

    def getKi(self):
        return self.ki
    
    def getKp(self):
        return self.kp

    def getManual_commanded(self):
        return self.commandedmanualspeed
    
    def getCurrent_speed(self):
        return self.currentSpeed
    
    def getTemperature(self):
        return self.temperature
    
    def getAnnoucements(self):
        return self.annoucement
    
    def getSpeedLimit(self):
        return self.speedLimit
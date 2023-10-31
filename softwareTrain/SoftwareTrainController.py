class SoftwareTrainController():
    
    def __init__(self):
        self.manualmode=False
        self.ctcSpeed=10                #speed to go in automatic mode when in the middle of a route in m/s
        self.automaticcommandedspeed=0   #desired speed in automatic mode. i edit this as the train is stopping at a station
        self.manualcommandedspeed=0      #the value of the slide bar. commandedspeed=manualcommandedspeed if manualMode=True 
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
        self.eBrake=False        #false=not pressed
        self.tunnel=False
        self.stationOnLeft='b' #where to let the passengers out. if stationOnLeft is true, that means the left doors open when the station is reached
        self.serviceBrakeSlide=0
        self.ek=0
        self.ekprev=0
        self.uk=0
        self.kp=11    #proportional gain
        self.ki=12   #integral gain
        self.brakeFailure=False  # false is no failure
        self.engineFailure=False
        self.signalFailure=False
        self.power=9     
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
        self.manualmode=b
        
    def getManualMode(self):
        return self.manualmode 
    def getEbrake(self):
        return self.eBrake
        
    def setBrakeFailure(self,a):
        self.brakeFailure=a
    def setSignalFailure(self,a):
        self.signalFailure=a
    def setEngineFailure(self,a):
        self.engineFailure=a

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
        return self.serviceBrakeSlide

    def getPower(self):
        return self.power
    
    def computePower(self):
        if self.manualmode==True:
            self.ekprev=self.ek
            self.ek=(self.manualcommandedspeed/2.2369362921-self.currentSpeed)
            self.uk+=(self.interval/2)*(self.ek-self.ekprev)
            self.power=(self.ek*self.kp+self.ki*self.uk)
        else:
            self.ekprev=self.ek
            self.ek=(self.automaticcommandedspeed-self.currentSpeed)
            self.uk+=(self.interval/2)*(self.ek-self.ekprev)
            self.power=(self.ek*self.kp+self.ki*self.uk)

        if self.power>120:
            self.power=120

        if self.brakeFailure or self.signalFailure or self.engineFailure or self.eBrake or self.power < 0 or self.serviceBrakeSlide:
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
        if self.authority<1000:
                self.automaticcommandedspeed=0
        else:
            self.automaticcommandedspeed=self.ctcSpeed

    def computeManualSpeed(self) ->int:
        if self.serviceBrakeSlide>0:
            self.manualcommandedspeed=self.currentSpeed #make sure this is good, assume connor sends this back

        if not self.manualmode:
            self.manualcommandedspeed=self.automaticcommandedspeed*2.2369362921
        else:
            if self.manualcommandedspeed>=self.speedLimit:
                self.manualcommandedspeed=self.speedLimit        #convert to m/s

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
    
